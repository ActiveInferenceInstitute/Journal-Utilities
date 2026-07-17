"""Tests for journal_utilities.data.enrichment."""

from pathlib import Path

import pytest

from journal_utilities.data.enrichment import (
    map_coda_row,
    merge_enrichment,
    parse_split_file,
    prefer_url,
    split_names,
)


class TestPreferUrl:
    def test_keeps_valid_primary(self):
        assert prefer_url("https://a.example", "https://b.example") == "https://a.example"

    def test_falls_back_when_primary_is_junk(self):
        assert prefer_url("#2022.2", "https://b.example") == "https://b.example"
        assert prefer_url("", "https://b.example") == "https://b.example"

    def test_keeps_junk_primary_when_no_url_fallback(self):
        assert prefer_url("#2022.2", "") == "#2022.2"
        assert prefer_url("", "") == ""


FIXTURES = Path(__file__).parent.parent / "fixtures"


class TestSplitNames:
    def test_simple_split(self):
        assert split_names("Daniel Friedman,Bert Berkers") == ["Daniel Friedman", "Bert Berkers"]

    def test_credential_suffix_rejoined(self):
        assert split_names("Alexey Tolchinsky, Psy.D.") == ["Alexey Tolchinsky, Psy.D."]
        assert split_names("Jane Doe, PhD,John Smith") == ["Jane Doe, PhD", "John Smith"]

    def test_empty_and_nonstring(self):
        assert split_names("") == []
        assert split_names(None) == []
        assert split_names(False) == []

    def test_alias_normalization(self):
        assert split_names("Ivan Metelkin,Sasha Mikhailova") == [
            "Ivan Metelkin",
            "Alexandra Mikhailova",
        ]


class TestMapCodaRow:
    FULL_ROW = {
        "Unique event name": "GuestStream #128.1",
        "Title or name of stream": "Learning in Physical Systems",
        "Date": "2025-11-05T00:00:00.000-08:00",
        "Guests": "Marcelo Guzman",
        "Other Participants": "Daniel Friedman,Bert Berkers",
        "Github": "https://github.com/x",
        "Slides": "https://slides.example",
        "Paper link": "https://paper.example",
        "DOI": "10.5281/zenodo.1",
        "Zenodo Link": "https://zenodo.org/1",
        "Keywords": "active inference, physics",
        "Thumbnail Image": "https://img.example/t.jpg",
        "Human Summary": "A summary.",
        "Copypasta": "should be ignored",
        "Caption Status": "should be ignored",
    }

    def test_full_row(self):
        out = map_coda_row(self.FULL_ROW)
        assert out["title"] == "GuestStream #128.1 ~ Learning in Physical Systems"
        assert out["date"] == "2025-11-05"
        assert out["guests"] == ["Marcelo Guzman"]
        assert out["other_participants"] == ["Daniel Friedman", "Bert Berkers"]
        assert out["slides_url"] == "https://slides.example"
        assert out["keywords"] == ["active inference", "physics"]
        assert out["thumbnails"] == {"thumbnail": "https://img.example/t.jpg"}
        assert out["summaries"] == {"human": "A summary."}
        assert "copypasta" not in {k.lower() for k in out}

    def test_empty_cells_omitted(self):
        out = map_coda_row({"Title or name of stream": "X", "Guests": "", "DOI": "  "})
        assert out == {"title": "X"}

    def test_slides_url_fallback_column(self):
        out = map_coda_row({"Slides URL": "https://alt.example"})
        assert out["slides_url"] == "https://alt.example"

    def test_link_labels_do_not_enter_url_fields(self):
        out = map_coda_row(
            {
                "Slides": "#023",
                "Slides URL": "https://slides.example",
                "Paper link": "Embodied skillful performance",
            }
        )
        assert out["slides_url"] == "https://slides.example"
        assert out["slides_label"] == "#023"
        assert out["paper_title"] == "Embodied skillful performance"
        assert "paper_link" not in out

    def test_placeholder_links_are_omitted(self):
        out = map_coda_row({"Slides": "n/a", "Paper link": "n/a"})
        assert "slides_url" not in out
        assert "slides_label" not in out
        assert "paper_link" not in out
        assert "paper_title" not in out

    def test_abstract_lands_in_summaries(self):
        out = map_coda_row({"Abstract": "An abstract."})
        assert out["summaries"] == {"abstract": "An abstract."}

    def test_nonstring_cells_ignored(self):
        out = map_coda_row({"Guests": False, "Date": 42, "Title or name of stream": "T"})
        assert out == {"title": "T"}


class TestParseSplitFile:
    @pytest.fixture()
    def result(self):
        return parse_split_file((FIXTURES / "split_sample.txt").read_text(encoding="utf-8"))

    def test_counts_and_target(self, result):
        assert len(result.sessions) == 3
        assert result.category == "Applied Active Inference Symposium/2024"
        assert result.series == "part 1"
        assert result.video_id == "cIBIecj7UZE"

    def test_session_fields(self, result):
        first = result.sessions[0]
        assert first["index"] == 1
        assert first["session_name"] == "cIBIecj7UZE_sess01"
        assert first["start"] == "0:00:00"
        assert first["guests"] == ["Karl Friston"]
        # curly quotes normalized, title from the chapter list
        assert "From pixels to planning" in first["title"]
        assert "“" not in first["title"]

    def test_start_normalization(self, result):
        assert result.sessions[1]["start"] == "1:59:35"
        assert result.sessions[2]["start"] == "2:59:25"

    def test_common_description_strips_session_line(self, result):
        assert "4th Applied Active Inference Symposium" in result.description
        assert "Session 1:" not in result.description
        assert "Session 2:" not in result.description

    def test_count_mismatch_raises(self):
        text = (FIXTURES / "split_sample.txt").read_text(encoding="utf-8")
        truncated = text[: text.rindex("CREATE session")]
        with pytest.raises(ValueError, match="mismatch"):
            parse_split_file(truncated)


class TestMergeEnrichment:
    BASE = {
        "series": "GuestStream",
        "item": "GuestStream_094",
        "source": "youtube",
        "channel": "ActiveInferenceInstitute",
        "category": "GuestStream",
        "episode": "1",
        "parts": [{"video_id": "abcdefghijk", "url": "u", "title": "YouTube Title"}],
    }

    def test_adds_enrichment_keys(self):
        new, changed = merge_enrichment(self.BASE, {"guests": ["A"], "date": "2024-01-01"})
        assert changed
        assert new["guests"] == ["A"]
        assert new["parts"][0]["title"] == "YouTube Title"  # untouched

    def test_idempotent(self):
        enrichment = {"guests": ["A"], "summaries": {"human": "s"}}
        once, changed1 = merge_enrichment(self.BASE, enrichment)
        twice, changed2 = merge_enrichment(once, enrichment)
        assert changed1 and not changed2
        assert once == twice

    def test_empty_values_never_clobber(self):
        meta = dict(self.BASE, github="https://keep.example")
        new, changed = merge_enrichment(meta, {"github": "", "guests": []})
        assert not changed
        assert new["github"] == "https://keep.example"

    def test_foreign_keys_survive(self):
        meta = dict(self.BASE, custom_field="daniel's")
        new, _ = merge_enrichment(meta, {"guests": ["A"]})
        assert new["custom_field"] == "daniel's"

    def test_fill_parts_only_when_empty(self):
        fill = [{"video_id": "x" * 11, "url": "u", "title": "t"}]
        empty = dict(self.BASE, parts=[])
        filled, changed = merge_enrichment(empty, {}, fill_parts=fill)
        assert changed and filled["parts"] == fill
        kept, _ = merge_enrichment(self.BASE, {}, fill_parts=fill)
        assert kept["parts"] == self.BASE["parts"]

    def test_sessions_seed_only_never_overwrite(self):
        seed = [{"index": 1, "session_name": "abcdefghijk_sess01", "start": "0:00:00"}]
        edited = [
            {
                "index": 1,
                "session_name": "abcdefghijk_sess01",
                "start": "0:00:00",
                "guests": ["Hand Edit"],
            }
        ]
        seeded, changed = merge_enrichment(self.BASE, {"sessions": seed})
        assert changed and seeded["sessions"] == seed
        kept, changed2 = merge_enrichment(dict(self.BASE, sessions=edited), {"sessions": seed})
        assert not changed2
        assert kept["sessions"] == edited

    def test_replace_parts_overrides_bogus_ids(self):
        meta = dict(self.BASE, parts=[{"video_id": "Int1-Sess01", "url": "", "title": ""}])
        fill = [{"video_id": "rIemcswLfGg", "url": "u", "title": "t"}]
        new, changed = merge_enrichment(meta, {}, fill_parts=fill, replace_parts=True)
        assert changed and new["parts"] == fill
        again, changed2 = merge_enrichment(new, {}, fill_parts=fill, replace_parts=True)
        assert not changed2

    def test_part_slides_label_never_replaces_url(self):
        meta = dict(
            self.BASE,
            parts=[{"video_id": "abcdefghijk", "slides_url": "https://docs.google.com/x"}],
        )
        new, changed = merge_enrichment(
            meta, {}, part_updates={"abcdefghijk": {"slides_url": "#035.1"}}
        )
        assert not changed
        assert new["parts"][0]["slides_url"] == "https://docs.google.com/x"

    def test_invalid_owned_links_are_normalized_without_data_loss(self):
        meta = dict(self.BASE, slides_url="#023", paper_link="Paper title")
        new, changed = merge_enrichment(meta, {})
        assert changed
        assert "slides_url" not in new
        assert new["slides_label"] == "#023"
        assert "paper_link" not in new
        assert new["paper_title"] == "Paper title"

    def test_part_updates_target_by_video_id(self):
        new, changed = merge_enrichment(
            self.BASE, {}, part_updates={"abcdefghijk": {"date": "2024-05-01"}}
        )
        assert changed
        assert new["parts"][0]["date"] == "2024-05-01"

    def test_reorder_alone_is_not_a_change(self):
        scrambled = {k: self.BASE[k] for k in reversed(list(self.BASE))}
        _, changed = merge_enrichment(scrambled, {})
        assert not changed
