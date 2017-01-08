# ../gungame/plugins/custom/gg_chicken_hunt/gg_chicken_hunt.py

"""Level players up only on chicken kills."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from entities.entity import Entity
from events import Event
from listeners import OnLevelInit

# GunGame
from gungame.core.players.attributes import AttributePreHook
from gungame.core.players.dictionary import player_dictionary

# Plugin
from .configuration import max_chickens


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
_allow_level = False


# =============================================================================
# >> HOOKS
# =============================================================================
@AttributePreHook('level')
def _pre_level_change(player, value):
    """"""
    if player.level < value and not _allow_level:
        return False


# =============================================================================
# >> EVENTS
# =============================================================================
@Event('other_death')
def _level_on_chicken_kill(game_event):
    """"""
    global _allow_level
    if game_event['othertype'] != 'chicken':
        return
    player = player_dictionary[game_event['attacker']]
    weapon = game_event['weapon']
    # TODO: allow knife kills
    # if weapon in knife_weapons:
    #     if not allow_knife_kills.get_bool():
    #         return
    # TODO: allow nade kills
    # elif weapon in nade_weapons:
    #     if not allow_nade_kills.get_bool():
    #         return
    # elif game_event['weapon'] != player.level_weapon:
    if weapon != player.level_weapon:
        return
    _allow_level = True
    player.increase_level(1, reason='chicken')
    _allow_level = False


# =============================================================================
# >> LISTENERS
# =============================================================================
@OnLevelInit
def load(map_name=None):
    map_info = Entity.find_or_create('info_map_parameters')
    map_info.pet_population = max_chickens.get_int()
