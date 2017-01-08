# ../gungame/plugins/included/gg_chicken_hunt/configuration.py

"""Creates the gg_chicken_hunt configuration."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame
from gungame.core.config.manager import GunGameConfigManager

# Plugin
from .info import info


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    'max_chickens',
)


# =============================================================================
# >> CONFIGURATION
# =============================================================================
with GunGameConfigManager(info.name) as _config:
    with _config.cvar('max_chickens', 20) as max_chickens:
        max_chickens.add_text()
