"""Pytest configuration and fixtures specific to the journal_utilities.rag tests."""

import os
from pathlib import Path

import pytest
from dotenv import load_dotenv

# Load .env file first to get real API keys if present
env_file = Path(__file__).parent.parent.parent / ".env"
if env_file.exists():
    load_dotenv(env_file)

# Only set mock values if not already set (from .env or environment)
if "COHERE_API_KEY" not in os.environ:
    os.environ["COHERE_API_KEY"] = "test-api-key"
if "SURREALDB_PASSWORD" not in os.environ:
    os.environ["SURREALDB_PASSWORD"] = "test-password"

from journal_utilities.rag.models import (
    Citation,
    CitationType,
    Concept,
    ConceptCategory,
    CoreEntities,
    Researcher,
    ResearcherRole,
    TechnicalTerm,
    TermDomain,
)


@pytest.fixture
def sample_concept() -> Concept:
    """Create a sample concept for testing."""
    return Concept(
        name="Free Energy Principle",
        definition="A theoretical framework that explains how biological agents minimize surprise",
        category=ConceptCategory.THEORETICAL,
        related_concepts=["Active Inference", "Predictive Coding"],
    )


@pytest.fixture
def sample_researcher() -> Researcher:
    """Create a sample researcher for testing."""
    return Researcher(
        name="Karl Friston",
        affiliation="University College London",
        role=ResearcherRole.CITED_AUTHOR,
        contribution="Developed the Free Energy Principle and Active Inference framework",
    )


@pytest.fixture
def sample_citation() -> Citation:
    """Create a sample citation for testing."""
    return Citation(
        type=CitationType.PAPER,
        title="The Free Energy Principle: A Unified Brain Theory?",
        authors=["Karl Friston"],
        venue="Nature Reviews Neuroscience",
        year=2010,
        context="Foundational paper on the Free Energy Principle",
    )


@pytest.fixture
def sample_technical_term() -> TechnicalTerm:
    """Create a sample technical term for testing."""
    return TechnicalTerm(
        term="Variational Free Energy",
        explanation="A mathematical quantity that bounds surprise in a Bayesian setting",
        domain=TermDomain.MATHEMATICS,
        synonyms=["Free Energy", "Variational Bound"],
    )


@pytest.fixture
def sample_core_entities() -> CoreEntities:
    """Create sample core entities for testing."""
    return CoreEntities(
        concepts=[
            Concept(
                name="Active Inference",
                definition="A framework for understanding action and perception",
                category=ConceptCategory.THEORETICAL,
            ),
            Concept(
                name="Predictive Coding",
                definition="A theory of brain function based on prediction errors",
                category=ConceptCategory.NEUROSCIENCE,
            ),
        ],
        researchers=[
            Researcher(
                name="Karl Friston",
                affiliation="UCL",
                role=ResearcherRole.SPEAKER,
            ),
            Researcher(
                name="Maxwell Ramstead",
                affiliation="McGill University",
                role=ResearcherRole.COLLABORATOR,
            ),
        ],
        citations=[
            Citation(
                type=CitationType.PAPER,
                title="Active Inference: A Process Theory",
                authors=["Karl Friston", "Thomas Parr", "Bert de Vries"],
                year=2017,
            ),
        ],
        technical_terms=[
            TechnicalTerm(
                term="Markov Blanket",
                explanation="A statistical boundary that separates internal and external states",
                domain=TermDomain.STATISTICS,
            ),
        ],
        key_insights=[
            "Active inference unifies perception and action under a single principle",
            "The brain can be understood as performing approximate Bayesian inference",
        ],
    )
