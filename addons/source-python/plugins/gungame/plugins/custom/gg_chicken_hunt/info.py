# ../gungame/plugins/custom/gg_chicken_hunt/info.py

"""Provides/stores information about the plugin."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from cvars.public import PublicConVar
from plugins.info import PluginInfo


# =============================================================================
# >> PLUGIN INFO
# =============================================================================
info = PluginInfo()
info.title = 'GunGame Chicken Hunt'
info.author = ''
info.version = '1.0'
info.name = 'gg_chicken_hunt'
info.variable = info.name + '_version'
info.url = ''
info.convar = PublicConVar(
    info.variable, info.version, info.title + ' Version',
)
