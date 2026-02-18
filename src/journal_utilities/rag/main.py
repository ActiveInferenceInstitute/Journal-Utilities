"""Main processing pipeline for JournalRAG."""

import asyncio
from collections.abc import Mapping
from datetime import datetime
from pathlib import Path
from typing import Any

import structlog

from journal_utilities.rag.adapters import EntityAdapter
from journal_utilities.rag.extractors import CohereExtractor
from journal_utilities.rag.graph import SurrealDBClient
from journal_utilities.rag.models import Transcript
from journal_utilities.rag.settings import settings
from journal_utilities.rag.utils import setup_logging

logger = structlog.get_logger(__name__)


class JournalRAGPipeline:
    """Main pipeline for extracting entities from transcripts and storing in graph database."""

    def __init__(self) -> None:
        """Initialize the pipeline."""
        setup_logging(debug=settings.debug)
        self.extractor = CohereExtractor()
        self.db_client = SurrealDBClient()
        logger.info("Initialized JournalRAG pipeline")

    async def connect(self) -> None:
        """Connect to the database."""
        await self.db_client.connect()

    async def disconnect(self) -> None:
        """Disconnect from the database."""
        await self.db_client.disconnect()

    async def process_transcript(self, transcript: Transcript) -> Mapping[str, int]:
        """Process a single transcript.

        This method:
        1. Gets or creates the transcript record in the database
        2. Extracts entities using CoreEntities schema
        3. Converts CoreEntities to simple Entity model for storage
        4. Stores entities in the database
        5. Extracts relationships from CoreEntities structure
        6. Stores relationships in the database
        7. Updates transcript as processed

        Args:
            transcript: The transcript to process.

        Returns:
            Dictionary with processing statistics.
        """
        logger.info("Processing transcript", title=transcript.title, source=transcript.source)

        # Get or create transcript record (idempotent)
        transcript_id = await self.db_client.get_or_create_transcript(transcript)
        logger.info("Transcript record ready", transcript_id=transcript_id)

        # Extract entities using new CoreEntities schema
        core_entities = self.extractor.extract_core_entities(transcript.content)
        logger.info("Extracted core entities from transcript")

        # Convert CoreEntities to simple Entity model for storage
        entities = EntityAdapter.convert_core_entities(core_entities)
        logger.info("Converted to storage format", entity_count=len(entities))

        # Store entities
        entity_count = 0
        for entity in entities:
            await self.db_client.create_entity(entity)
            entity_count += 1

        # Extract relationships from CoreEntities structure
        relationships = EntityAdapter.extract_relationships(core_entities)
        logger.info("Extracted relationships", relationship_count=len(relationships))

        # Store relationships
        relationship_count = 0
        for relationship in relationships:
            try:
                await self.db_client.create_relationship(relationship)
                relationship_count += 1
            except Exception as e:
                logger.warning(
                    "Failed to create relationship",
                    source=relationship.source,
                    target=relationship.target,
                    error=str(e),
                )
                continue

        # Mark transcript as processed
        await self.db_client.update_transcript_status(transcript_id, processed=True)

        logger.info(
            "Completed processing transcript",
            title=transcript.title,
            entities=entity_count,
            relationships=relationship_count,
        )

        return {
            "entities": entity_count,
            "relationships": relationship_count,
        }

    async def process_transcript_file(self, file_path: Path) -> Mapping[str, int]:
        """Process a transcript from a file.

        Args:
            file_path: Path to the transcript file.

        Returns:
            Dictionary with processing statistics.
        """
        logger.info("Processing transcript file", file_path=str(file_path))

        # Read transcript content
        content = file_path.read_text(encoding="utf-8")

        # Create transcript object
        transcript = Transcript(
            title=file_path.stem,
            date=datetime.now(),  # You may want to extract date from filename or content
            content=content,
            source=str(file_path),
        )

        return await self.process_transcript(transcript)

    async def process_from_database(self, base_path: Path | None = None) -> Mapping[str, int]:
        """Process all unprocessed transcripts from the database.

        This orchestrator method:
        1. Queries SurrealDB for unprocessed transcript paths
        2. Loads each transcript from the local repository
        3. Processes each transcript (extract entities, store in DB)
        4. Handles errors gracefully to continue processing

        Args:
            base_path: Optional base path for transcript files. If provided, paths from
                      the database will be resolved relative to this base. If None, paths
                      are assumed to be absolute.

        Returns:
            Dictionary with processing statistics including:
            - total: Total transcripts found in DB
            - processed: Number successfully processed
            - failed: Number that failed
            - total_entities: Total entities extracted
            - total_relationships: Total relationships extracted
        """
        logger.info("Starting batch processing from database")

        # Get unprocessed transcript paths from database
        transcript_paths = await self.db_client.get_unprocessed_transcript_paths()
        logger.info("Found unprocessed transcripts", count=len(transcript_paths))

        if not transcript_paths:
            logger.info("No unprocessed transcripts found")
            return {
                "total": 0,
                "processed": 0,
                "failed": 0,
                "total_entities": 0,
                "total_relationships": 0,
            }

        # Process each transcript
        processed_count = 0
        failed_count = 0
        total_entities = 0
        total_relationships = 0

        for source_path in transcript_paths:
            try:
                # Resolve file path
                if base_path:
                    file_path = base_path / source_path
                else:
                    file_path = Path(source_path)

                # Check if file exists
                if not file_path.exists():
                    logger.warning("Transcript file not found", path=str(file_path))
                    failed_count += 1
                    continue

                # Load transcript content
                content = file_path.read_text(encoding="utf-8")

                # Create transcript object
                transcript = Transcript(
                    title=file_path.stem,
                    date=datetime.now(),  # You may want to extract date from filename
                    content=content,
                    source=source_path,
                )

                # Process transcript
                stats = await self.process_transcript(transcript)

                # Update totals
                processed_count += 1
                total_entities += stats["entities"]
                total_relationships += stats["relationships"]

                logger.info(
                    "Processed transcript successfully",
                    path=source_path,
                    entities=stats["entities"],
                    relationships=stats["relationships"],
                )

            except Exception as e:
                logger.error(
                    "Failed to process transcript",
                    path=source_path,
                    error=str(e),
                    exc_info=True,
                )
                failed_count += 1
                continue

        logger.info(
            "Batch processing complete",
            total=len(transcript_paths),
            processed=processed_count,
            failed=failed_count,
            total_entities=total_entities,
            total_relationships=total_relationships,
        )

        return {
            "total": len(transcript_paths),
            "processed": processed_count,
            "failed": failed_count,
            "total_entities": total_entities,
            "total_relationships": total_relationships,
        }


async def main() -> None:
    """Main entry point."""
    pipeline = JournalRAGPipeline()

    try:
        await pipeline.connect()
        logger.info("Pipeline ready")

        # Example: Process a transcript file
        # transcript_path = Path("path/to/transcript.txt")
        # stats = await pipeline.process_transcript_file(transcript_path)
        # logger.info("Processing complete", stats=stats)

    finally:
        await pipeline.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
