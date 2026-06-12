"""
Can't Stop Win - World Cup 2026 Prediction Skill
Build prediction models for FIFA World Cup matches
"""

__version__ = "1.0.0"
__author__ = "Can't Stop Win Team"

from .predictor import Predictor
from .data_fetcher import DataFetcher
from .simulator import TournamentSimulator

__all__ = [
    "Predictor",
    "DataFetcher", 
    "TournamentSimulator",
]
