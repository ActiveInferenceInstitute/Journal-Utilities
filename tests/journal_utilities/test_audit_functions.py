"""Test suite for audit trail functions in journal_utilities."""

import json
import os
import tempfile
from typing import Any

import pytest
from surrealdb import AsyncSurreal

from journal_utilities.ingest_db_create_wav import (
    get_failed_imports,
    get_import_summary,
    get_recent_import_runs,
    insert_missing_sessions_from_json,
    rollback_import,
)


@pytest.mark.asyncio
async def test_get_recent_import_runs(
    db_url: str,
    db_user: str,
    db_password: str,
    db_name: str,
    db_namespace: str,
) -> None:
    """Test getting recent import runs."""
    runs = await get_recent_import_runs(
        db_url, db_user, db_password, db_name, db_namespace, limit=5
    )

    # Check that we get a list
    assert isinstance(runs, list)

    # If there are runs, check their structure
    if runs:
        first_run = runs[0]
        assert "import_run_id" in first_run
        assert "timestamp" in first_run
        assert "source_file" in first_run
        assert "stats" in first_run

        # Check stats structure
        stats = first_run["stats"]
        assert "total" in stats
        assert "inserted" in stats
        assert "skipped" in stats
        assert "failed" in stats

        print(f"Found {len(runs)} import runs")


@pytest.mark.asyncio
async def test_get_import_summary(
    db_url: str,
    db_user: str,
    db_password: str,
    db_name: str,
    db_namespace: str,
) -> None:
    """Test getting import summary for a specific run."""
    # First get a recent run to test with
    runs = await get_recent_import_runs(
        db_url, db_user, db_password, db_name, db_namespace, limit=1
    )

    if not runs:
        pytest.skip("No import runs found in database")

    import_run_id = runs[0]["import_run_id"]

    # Get the summary
    summary = await get_import_summary(
        import_run_id, db_url, db_user, db_password, db_name, db_namespace
    )

    # Check summary structure
    assert isinstance(summary, dict)
    assert "total" in summary
    assert "inserted" in summary
    assert "skipped" in summary
    assert "failed" in summary

    # Check that numbers are non-negative
    assert summary["total"] >= 0
    assert summary["inserted"] >= 0
    assert summary["skipped"] >= 0
    assert summary["failed"] >= 0

    # Check that components add up to total (approximately)
    components_sum = summary["inserted"] + summary["skipped"] + summary["failed"]
    assert components_sum <= summary["total"]

    print(f"Import summary: {summary}")


@pytest.mark.asyncio
async def test_get_failed_imports(
    db_url: str,
    db_user: str,
    db_password: str,
    db_name: str,
    db_namespace: str,
) -> None:
    """Test getting failed imports from a run."""
    # Get a recent run
    runs = await get_recent_import_runs(
        db_url, db_user, db_password, db_name, db_namespace, limit=1
    )

    if not runs:
        pytest.skip("No import runs found in database")

    import_run_id = runs[0]["import_run_id"]

    # Get failed imports
    failed = await get_failed_imports(
        import_run_id, db_url, db_user, db_password, db_name, db_namespace
    )

    # Check that we get a list
    assert isinstance(failed, list)

    # If there are failures, check their structure
    if failed:
        first_failure = failed[0]
        assert "session_name" in first_failure
        assert "operation" in first_failure
        assert "error" in first_failure
        assert "timestamp" in first_failure
        assert "data_attempted" in first_failure

        print(f"Found {len(failed)} failed imports")


@pytest.mark.asyncio
async def test_audit_trail_creation(
    db_url: str,
    db_user: str,
    db_password: str,
    db_name: str,
    db_namespace: str,
) -> None:
    """Test that audit records are created during import."""
    # Create a test JSON file with minimal data
    test_json = {
        "items": [
            {
                "values": {
                    "YouTube": "https://www.youtube.com/watch?v=TEST12345AB",
                    "Unique event name": "Test Event",
                    "Title or name of stream": "Test Stream",
                }
            }
        ]
    }

    # Write test JSON to temporary file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(test_json, f)
        test_file = f.name

    try:
        # Run the import
        await insert_missing_sessions_from_json(
            test_file, db_url, db_user, db_password, db_name, db_namespace
        )

        # Check that audit records were created
        async with AsyncSurreal(db_url) as db:
            await db.signin({"username": db_user, "password": db_password})
            await db.use(db_namespace, db_name)

            # Find audit records for this import
            result = await db.query(
                f"""
                SELECT * FROM import_audit
                WHERE source_file = '{test_file}'
                ORDER BY timestamp DESC
            """
            )

            assert result is not None
            assert len(result) > 0

            # Should have at least a summary record
            summary_found = False
            for record in result:
                if record.get("operation") == "import_summary":
                    summary_found = True
                    break

            assert summary_found, "No import summary record found"

            # Clean up: delete the test session if it was created
            await db.query("DELETE session WHERE session_name = 'TEST12345AB'")

    finally:
        # Clean up temporary file
        os.unlink(test_file)

    print("Audit trail creation test passed")
