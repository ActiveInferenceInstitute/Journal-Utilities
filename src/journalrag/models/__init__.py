"""Data models for JournalRAG."""

from .entities import (
    Application,
    ApplicationStatus,
    Citation,
    CitationType,
    Concept,
    ConceptCategory,
    CoreEntities,
    DetailedAnalysis,
    Entity,
    Equation,
    ExtractedEntities,
    MathematicalNotation,
    MethodTechnique,
    Relationship,
    Researcher,
    ResearcherRole,
    ResearchProblem,
    ResourceType,
    TechnicalTerm,
    TermDomain,
    ToolResource,
    Transcript,
)

__all__ = [
    # Core schema models
    "Concept",
    "ConceptCategory",
    "Researcher",
    "ResearcherRole",
    "Citation",
    "CitationType",
    "TechnicalTerm",
    "TermDomain",
    "CoreEntities",
    # Detailed schema models
    "MethodTechnique",
    "MathematicalNotation",
    "Equation",
    "ToolResource",
    "ResourceType",
    "ResearchProblem",
    "Application",
    "ApplicationStatus",
    "DetailedAnalysis",
    # Combined result
    "ExtractedEntities",
    # Simple storage models
    "Transcript",
    "Entity",
    "Relationship",
]
