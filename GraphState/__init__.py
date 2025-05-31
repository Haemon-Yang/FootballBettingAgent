"""
GraphState Package

This package provides state management classes for building AI agents workflow.
It includes classes for managing main graph states, report states, and various section states.

"""

# Type hints for better IDE support
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .main_state import MainGraphState
    from .deep_research_state import (
        Section,
        Sections,
        SearchQuery,
        Queries,
        ReportState,
        SectionState,
        SectionOutputState,
        ReportStateInput,
        ReportStateOutput
    )

# Main state imports
from .main_state import MainGraphState

# Deep research state imports
from .deep_research_state import (
    Section,
    Sections,
    SearchQuery,
    Queries,
    ReportState,
    SectionState,
    SectionOutputState,
    ReportStateInput,
    ReportStateOutput
)

# Public API declaration
__all__ = [
    "Section",
    "Sections",
    "SearchQuery",
    "Queries",
    "ReportState",
    "SectionState",
    "SectionOutputState",
    "ReportStateInput",
    "ReportStateOutput",
]