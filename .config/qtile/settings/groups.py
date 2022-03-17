# Qtile workspaces

from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-fa-chrome,
# nf-fa-code,
# nf-dev-terminal, 
# nf-mdi-language_cpp, 
# nf-fae-python, 
# nf-fa-spotify,
# nf-mdi-discord, 

groups = [Group(i) for i in [
    "   ",  "   ", "   ", "  ﭱ ", "   ", "   ", "  ﭮ "
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
