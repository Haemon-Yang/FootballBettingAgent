"""
Football Agents Package
A comprehensive package for football data analysis and betting agent system.
"""

from .system_init import (
    system_initialization,
    update_PremierLeague_data,
    setup_scheduled_updates,
    stop_scheduled_updates,
    get_initial_graph_state
)

from .node import Nodes
from .graph import Workflow

__version__ = "0.1.0"
__author__ = "Haemon"

__all__ = [
    'system_initialization',
    'update_PremierLeague_data',
    'setup_scheduled_updates',
    'stop_scheduled_updates',
    'get_initial_graph_state',
    'create_agent',
    'Node',
    'Graph'
] 