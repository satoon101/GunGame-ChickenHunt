# ../gungame/plugins/custom/gg_chicken_hunt/rules.py

"""Creates the gg_chicken_hunt rules."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame
from gungame.core.rules.instance import GunGameRules
from gungame.core.rules.strings import rules_translations

# Plugin
from .info import info


# =============================================================================
# >> RULES
# =============================================================================
chicken_hunt_rules = GunGameRules(info.name)
