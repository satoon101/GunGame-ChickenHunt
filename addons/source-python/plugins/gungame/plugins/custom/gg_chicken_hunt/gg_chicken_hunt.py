# ../gungame/plugins/custom/gg_chicken_hunt/gg_chicken_hunt.py

"""Level players up only on chicken kills."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from entities.entity import Entity
from events import Event
from listeners import OnLevelInit
from weapons.manager import weapon_manager

# GunGame
from gungame.core.players.attributes import AttributePreHook
from gungame.core.players.dictionary import player_dictionary
from gungame.core.status import GunGameMatchStatus, GunGameStatus
from gungame.core.weapons.groups import (
    all_grenade_weapons, incendiary_weapons, melee_weapons,
)

# Plugin
from .configuration import allow_knife_kills, allow_nade_kills, max_chickens


# =============================================================================
# >> CLASSES
# =============================================================================
class _ChickenManager(object):
    allow_level = False

    def should_allow_level(self, player, level):
        """Disable leveling if the player did not just kill a chicken."""
        if player.level and player.level < level and self.allow_level:
            return False
        return None

    def level_up_player(self, game_event):
        """Level the player if they killed a chicken."""
        if game_event['othertype'] != 'chicken':
            return

        try:
            player = player_dictionary[game_event['attacker']]
        except ValueError:
            return

        try:
            weapon = weapon_manager[game_event['weapon']]
        except KeyError:
            return

        weapon = weapon.basename
        if weapon == 'molotov' and player.level_weapon in incendiary_weapons:
            weapon = player.level_weapon

        if weapon != player.level_weapon:
            if weapon in all_grenade_weapons:
                if not allow_nade_kills.get_bool():
                    return

            elif weapon in melee_weapons:
                if not allow_knife_kills.get_bool():
                    return

            else:
                return

        self.allow_level = True
        player.increase_level(1, reason='chicken')
        self.allow_level = False

_chicken_manager = _ChickenManager()


# =============================================================================
# >> HOOKS
# =============================================================================
@AttributePreHook('level')
def _pre_level_change(player, attribute, new_value):
    return _chicken_manager.should_allow_level(
        player=player,
        level=new_value,
    )


# =============================================================================
# >> EVENTS
# =============================================================================
@Event('other_death')
def _level_on_chicken_kill(game_event):
    if GunGameStatus.MATCH is GunGameMatchStatus.ACTIVE:
        _chicken_manager.level_up_player(game_event=game_event)


# =============================================================================
# >> LISTENERS
# =============================================================================
@OnLevelInit
def load(map_name=None):
    """Set the chickens for the map."""
    map_info = Entity.find_or_create('info_map_parameters')
    map_info.pet_population = max_chickens.get_int()
