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
    'allow_knife_kills',
    'allow_nade_kills',
    'max_chickens',
)


# =============================================================================
# >> CONFIGURATION
# =============================================================================
with GunGameConfigManager(info.name) as _config:

    with _config.cvar('max_chickens', 20) as max_chickens:
        max_chickens.add_text()

    with _config.cvar('allow_nade_kills') as allow_nade_kills:
        allow_nade_kills.add_text()

    with _config.cvar('allow_knife_kills') as allow_knife_kills:
        allow_knife_kills.add_text()
