"""Tests for journal_utilities.data.coda_client (stubbed network)."""

import io
import json

import pytest

from journal_utilities.data import coda_client


def _response(payload: dict):
    class _Resp(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

    return _Resp(json.dumps(payload).encode())


class TestFetchTableRows:
    def test_pagination_follows_next_page_link(self, monkeypatch):
        pages = {
            "https://coda.io/apis/v1/docs/D/tables/T/rows?limit=200&useColumnNames=true": {
                "items": [{"name": "row1"}],
                "nextPageLink": "https://coda.io/apis/v1/next",
            },
            "https://coda.io/apis/v1/next": {"items": [{"name": "row2"}]},
        }
        seen_auth = []

        def fake_urlopen(req, timeout=None):
            seen_auth.append(req.get_header("Authorization"))
            return _response(pages[req.full_url])

        monkeypatch.setattr(coda_client.urllib.request, "urlopen", fake_urlopen)
        rows = coda_client.fetch_table_rows(doc_id="D", table_id="T", token="tok")
        assert [r["name"] for r in rows] == ["row1", "row2"]
        assert seen_auth == ["Bearer tok", "Bearer tok"]

    def test_missing_token_raises(self, monkeypatch):
        monkeypatch.delenv("CODA_API_TOKEN", raising=False)
        with pytest.raises(coda_client.CodaAuthError):
            coda_client.fetch_table_rows(doc_id="D", table_id="T")


class TestLoadRows:
    def test_falls_back_to_snapshot_without_token(self, monkeypatch, tmp_path):
        monkeypatch.delenv("CODA_API_TOKEN", raising=False)
        snapshot = tmp_path / "snap.json"
        snapshot.write_text(json.dumps({"items": [{"name": "snapped"}]}))
        rows, source = coda_client.load_rows(
            snapshot_path=snapshot, cache_path=tmp_path / "cache.json", fetch=True
        )
        assert rows == [{"name": "snapped"}]
        assert "snapshot" in source

    def test_prefers_cache_over_snapshot(self, monkeypatch, tmp_path):
        monkeypatch.delenv("CODA_API_TOKEN", raising=False)
        snapshot = tmp_path / "snap.json"
        snapshot.write_text(json.dumps({"items": [{"name": "snapped"}]}))
        cache = tmp_path / "cache.json"
        cache.write_text(json.dumps({"items": [{"name": "cached"}]}))
        rows, source = coda_client.load_rows(snapshot_path=snapshot, cache_path=cache, fetch=True)
        assert rows == [{"name": "cached"}]
        assert "cache" in source

    def test_fetch_writes_cache(self, monkeypatch, tmp_path):
        monkeypatch.setattr(coda_client, "fetch_table_rows", lambda: [{"name": "live"}])
        cache = tmp_path / "cache.json"
        rows, source = coda_client.load_rows(
            snapshot_path=tmp_path / "missing.json", cache_path=cache, fetch=True
        )
        assert rows == [{"name": "live"}]
        assert json.loads(cache.read_text())["items"] == [{"name": "live"}]
        assert "api" in source

    def test_no_fetch_uses_snapshot(self, tmp_path):
        snapshot = tmp_path / "snap.json"
        snapshot.write_text(json.dumps({"items": [{"name": "snapped"}]}))
        rows, _ = coda_client.load_rows(
            snapshot_path=snapshot, cache_path=tmp_path / "cache.json", fetch=False
        )
        assert rows == [{"name": "snapped"}]
