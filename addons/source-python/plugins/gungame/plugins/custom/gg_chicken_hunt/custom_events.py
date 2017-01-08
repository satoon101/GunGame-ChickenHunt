# ../gungame/plugins/custom/gg_chicken_hunt/custom_events.py

"""Events used by gg_chicken_hunt."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from events.custom import CustomEvent
from events.variable import ShortVariable

# GunGame
from gungame.core.events.resource import GGResourceFile

# Plugin
from .info import info


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    'GG_Chicken_Hunt',
)


# =============================================================================
# >> CLASSES
# =============================================================================
class GG_Chicken_Hunt(CustomEvent):

    variable = ShortVariable('Description of the variable')


# =============================================================================
# >> RESOURCE FILE
# =============================================================================
GGResourceFile(info.name, GG_Chicken_Hunt)
