"""
Utility module for Etap Smart Lock
Contains helper functions and configuration management
"""

from .config import load_config, save_config

__all__ = [
    'load_config',
    'save_config'
]