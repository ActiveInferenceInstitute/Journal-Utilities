"""Cohere-based entity extraction using JSON Schema mode."""

from collections.abc import Mapping
import json
from typing import Any

import cohere
import structlog

from journal_utilities.rag.models.entities import CoreEntities, DetailedAnalysis, ExtractedEntities
from journal_utilities.rag.schemas import load_core_schema, load_detailed_schema
from journal_utilities.rag.settings import settings

logger = structlog.get_logger(__name__)


class CohereExtractor:
    """Extract entities from Active Inference transcripts using Cohere with JSON Schema mode."""

    def __init__(self, api_key: str | None = None, model: str | None = None) -> None:
        """Initialize the Cohere extractor.

        Args:
            api_key: Cohere API key. If None, uses settings.
            model: Model name to use. If None, uses settings.
        """
        self.api_key: str = api_key or settings.cohere_api_key
        self.model: str = model or settings.cohere_model
        self.client: cohere.ClientV2 = cohere.ClientV2(api_key=self.api_key)

        # Load schemas once at initialization
        self._core_schema: Mapping[str, Any] = load_core_schema()
        self._detailed_schema: Mapping[str, Any] = load_detailed_schema()

        logger.info("Initialized CohereExtractor", model=self.model)

    def extract_core_entities(self, transcript: str) -> CoreEntities:
        """Extract core entities from transcript.

        Extracts: concepts, researchers, citations, technical terms, and key insights.
        This is faster and should be run first on every transcript.

        Args:
            transcript: The transcript text to extract entities from.

        Returns:
            CoreEntities model with validated extracted data.

        Raises:
            Exception: If extraction fails.
        """
        logger.info("Extracting core entities", text_length=len(transcript))

        try:
            response = self.client.chat(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": """You are an expert at extracting structured information from Active Inference and neuroscience academic presentations.
Extract entities accurately and comprehensively. For concepts, provide clear definitions.
For researchers, identify their roles and contributions. Only include citations if specific details are mentioned.""",
                    },
                    {
                        "role": "user",
                        "content": f"Extract all core entities from this transcript:\n\n{transcript}",
                    },
                ],
                response_format={"type": "json_object", "schema": self._core_schema},
                temperature=0.3,  # Lower temperature for more consistent extraction
            )

            # Parse response and validate with Pydantic model
            data = json.loads(response.message.content[0].text)
            core_entities = CoreEntities(**data)

            logger.info(
                "Extracted core entities",
                concepts=len(core_entities.concepts),
                researchers=len(core_entities.researchers),
                citations=len(core_entities.citations),
                terms=len(core_entities.technical_terms),
                insights=len(core_entities.key_insights),
            )

            return core_entities

        except Exception as e:
            logger.error("Failed to extract core entities", error=str(e))
            raise

    def extract_detailed_analysis(self, transcript: str) -> DetailedAnalysis:
        """Extract detailed technical analysis from transcript.

        Extracts: methods/techniques, mathematical notation, equations,
        tools/resources, research problems, and applications.
        Run this separately, especially for highly technical transcripts.

        Args:
            transcript: The transcript text to extract details from.

        Returns:
            DetailedAnalysis model with validated extracted data.

        Raises:
            Exception: If extraction fails.
        """
        logger.info("Extracting detailed analysis", text_length=len(transcript))

        try:
            response = self.client.chat(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": """You are an expert at extracting technical details from Active Inference and neuroscience presentations.
Focus on methodologies, mathematical notation, equations, software tools, research problems, and applications.
Only include equations if they are explicitly discussed. Capture implementation details when mentioned.""",
                    },
                    {
                        "role": "user",
                        "content": f"Extract all technical details and methods from this transcript:\n\n{transcript}",
                    },
                ],
                response_format={"type": "json_object", "schema": self._detailed_schema},
                temperature=0.3,
            )

            # Parse response and validate with Pydantic model
            data = json.loads(response.message.content[0].text)
            detailed_analysis = DetailedAnalysis(**data)

            logger.info(
                "Extracted detailed analysis",
                methods=len(detailed_analysis.methods_techniques),
                notation=len(detailed_analysis.mathematical_notation),
                equations=len(detailed_analysis.equations),
                tools=len(detailed_analysis.tools_resources),
                problems=len(detailed_analysis.research_problems),
                applications=len(detailed_analysis.applications),
            )

            return detailed_analysis

        except Exception as e:
            logger.error("Failed to extract detailed analysis", error=str(e))
            raise

    def extract_complete(
        self, transcript: str, transcript_id: str | None = None, include_detailed: bool = True
    ) -> ExtractedEntities:
        """Extract both core entities and detailed analysis from transcript.

        Args:
            transcript: The transcript text to extract from.
            transcript_id: Optional ID for the transcript.
            include_detailed: Whether to include detailed analysis (default: True).

        Returns:
            ExtractedEntities model combining core and detailed extraction.

        Raises:
            Exception: If extraction fails.
        """
        logger.info(
            "Extracting complete entities",
            text_length=len(transcript),
            transcript_id=transcript_id,
            include_detailed=include_detailed,
        )

        # Extract core entities
        core_entities = self.extract_core_entities(transcript)

        # Optionally extract detailed analysis
        detailed_analysis = None
        if include_detailed:
            detailed_analysis = self.extract_detailed_analysis(transcript)

        # Combine into ExtractedEntities
        extracted = ExtractedEntities(
            core=core_entities,
            detailed=detailed_analysis,
            transcript_id=transcript_id,
        )

        logger.info("Completed extraction", transcript_id=transcript_id)
        return extracted

    # Backward compatibility methods (deprecated)
    def extract_entities(self, text: str) -> CoreEntities:
        """Extract core entities (backward compatibility).

        Deprecated: Use extract_core_entities() instead.

        Args:
            text: The text to extract entities from.

        Returns:
            CoreEntities model.
        """
        logger.warning("extract_entities() is deprecated, use extract_core_entities() instead")
        return self.extract_core_entities(text)
