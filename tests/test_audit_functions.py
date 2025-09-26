import unittest
import asyncio
import os
import sys
from dotenv import load_dotenv
from datetime import datetime

sys.path.append('src')
from ingest_db_create_wav import (
    get_recent_import_runs,
    get_import_summary,
    get_failed_imports,
    insert_missing_sessions_from_json,
    rollback_import
)

load_dotenv('.env')


class TestAuditFunctions(unittest.TestCase):
    """Test suite for audit trail functions"""

    @classmethod
    def setUpClass(cls):
        """Set up database connection parameters"""
        cls.DB_URL = os.getenv("DB_URL")
        cls.DB_USER = os.getenv('DB_USER')
        cls.DB_PASSWORD = os.getenv('DB_PASSWORD')
        cls.DB_NAME = os.getenv('DB_NAME')
        cls.DB_NAMESPACE = os.getenv('DB_NAMESPACE')

    def test_get_recent_import_runs(self):
        """Test getting recent import runs"""
        async def run_test():
            runs = await get_recent_import_runs(
                self.DB_URL, self.DB_USER, self.DB_PASSWORD,
                self.DB_NAME, self.DB_NAMESPACE, limit=5
            )

            # Check that we get a list
            self.assertIsInstance(runs, list)

            # If there are runs, check their structure
            if runs:
                first_run = runs[0]
                self.assertIn('import_run_id', first_run)
                self.assertIn('timestamp', first_run)
                self.assertIn('source_file', first_run)
                self.assertIn('stats', first_run)

                # Check stats structure
                stats = first_run['stats']
                self.assertIn('total', stats)
                self.assertIn('inserted', stats)
                self.assertIn('skipped', stats)
                self.assertIn('failed', stats)

            return runs

        runs = asyncio.run(run_test())
        print(f"Found {len(runs)} import runs")

    def test_get_import_summary(self):
        """Test getting import summary for a specific run"""
        async def run_test():
            # First get a recent run to test with
            runs = await get_recent_import_runs(
                self.DB_URL, self.DB_USER, self.DB_PASSWORD,
                self.DB_NAME, self.DB_NAMESPACE, limit=1
            )

            if not runs:
                self.skipTest("No import runs found in database")

            import_run_id = runs[0]['import_run_id']

            # Get the summary
            summary = await get_import_summary(
                import_run_id, self.DB_URL, self.DB_USER,
                self.DB_PASSWORD, self.DB_NAME, self.DB_NAMESPACE
            )

            # Check summary structure
            self.assertIsInstance(summary, dict)
            self.assertIn('total', summary)
            self.assertIn('inserted', summary)
            self.assertIn('skipped', summary)
            self.assertIn('failed', summary)

            # Check that numbers are non-negative
            self.assertGreaterEqual(summary['total'], 0)
            self.assertGreaterEqual(summary['inserted'], 0)
            self.assertGreaterEqual(summary['skipped'], 0)
            self.assertGreaterEqual(summary['failed'], 0)

            # Check that components add up to total (approximately)
            components_sum = summary['inserted'] + summary['skipped'] + summary['failed']
            self.assertLessEqual(components_sum, summary['total'])

            return summary

        summary = asyncio.run(run_test())
        print(f"Import summary: {summary}")

    def test_get_failed_imports(self):
        """Test getting failed imports from a run"""
        async def run_test():
            # Get a recent run
            runs = await get_recent_import_runs(
                self.DB_URL, self.DB_USER, self.DB_PASSWORD,
                self.DB_NAME, self.DB_NAMESPACE, limit=1
            )

            if not runs:
                self.skipTest("No import runs found in database")

            import_run_id = runs[0]['import_run_id']

            # Get failed imports
            failed = await get_failed_imports(
                import_run_id, self.DB_URL, self.DB_USER,
                self.DB_PASSWORD, self.DB_NAME, self.DB_NAMESPACE
            )

            # Check that we get a list
            self.assertIsInstance(failed, list)

            # If there are failures, check their structure
            if failed:
                first_failure = failed[0]
                self.assertIn('session_name', first_failure)
                self.assertIn('operation', first_failure)
                self.assertIn('error', first_failure)
                self.assertIn('timestamp', first_failure)
                self.assertIn('data_attempted', first_failure)

            return failed

        failed = asyncio.run(run_test())
        print(f"Found {len(failed)} failed imports")

    def test_audit_trail_creation(self):
        """Test that audit records are created during import"""
        async def run_test():
            from surrealdb import AsyncSurreal

            # Create a test JSON file with minimal data
            test_json = {
                "items": [
                    {
                        "values": {
                            "YouTube": "https://www.youtube.com/watch?v=TEST12345AB",
                            "Unique event name": "Test Event",
                            "Title or name of stream": "Test Stream"
                        }
                    }
                ]
            }

            # Write test JSON to temporary file
            import json
            import tempfile
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                json.dump(test_json, f)
                test_file = f.name

            try:
                # Run the import
                await insert_missing_sessions_from_json(
                    test_file, self.DB_URL, self.DB_USER,
                    self.DB_PASSWORD, self.DB_NAME, self.DB_NAMESPACE
                )

                # Check that audit records were created
                async with AsyncSurreal(self.DB_URL) as db:
                    await db.signin({
                        'username': self.DB_USER,
                        'password': self.DB_PASSWORD
                    })
                    await db.use(self.DB_NAMESPACE, self.DB_NAME)

                    # Find audit records for this import
                    result = await db.query(f"""
                        SELECT * FROM import_audit
                        WHERE source_file = '{test_file}'
                        ORDER BY timestamp DESC
                    """)

                    self.assertIsNotNone(result)
                    self.assertGreater(len(result), 0)

                    # Should have at least a summary record
                    summary_found = False
                    for record in result:
                        if record.get('operation') == 'import_summary':
                            summary_found = True
                            break

                    self.assertTrue(summary_found, "No import summary record found")

                    # Clean up: delete the test session if it was created
                    await db.query("DELETE session WHERE session_name = 'TEST12345AB'")

            finally:
                # Clean up temporary file
                os.unlink(test_file)

        asyncio.run(run_test())
        print("Audit trail creation test passed")


if __name__ == '__main__':
    unittest.main()
