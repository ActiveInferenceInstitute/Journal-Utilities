"""
JSON schemas for entity extraction from Active Inference transcripts.
"""
from collections.abc import Mapping
import json
from pathlib import Path
from typing import Any

__all__ = ["load_core_schema", "load_detailed_schema", "SCHEMAS_DIR"]

SCHEMAS_DIR = Path(__file__).parent


def load_core_schema() -> Mapping[str, Any]:
    """
    Load the core entity extraction schema.

    Returns schema for extracting: concepts, researchers, citations,
    technical_terms, and key_insights.
    """
    schema_path = SCHEMAS_DIR / "active_inference_schema_core.json"
    with open(schema_path) as f:
        return json.load(f)


def load_detailed_schema() -> Mapping[str, Any]:
    """
    Load the detailed analysis schema.

    Returns schema for extracting: methods_techniques, mathematical_notation,
    equations, tools_resources, research_problems, and applications.
    """
    schema_path = SCHEMAS_DIR / "active_inference_schema_detailed.json"
    with open(schema_path) as f:
        return json.load(f)
