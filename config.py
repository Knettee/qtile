# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
mod1 = "alt"
mod2 = "control"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    #Sound
    Key([],"XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([],"XF86AudioLowerVolume", lazy.spawn("amixer -c 1 sset Master 1- unmute")),
    Key([],"XF86AudioRaiseVolume", lazy.spawn("amixer -c 1 sset Master 1+ unmute")),

    #lumi
    Key([],"XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([],"XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

#groups = [Group(i) for i in "123456789"]
#
#for i in groups:
#    keys.extend(
#        [
#            # mod1 + letter of group = switch to group
#            Key(
#                [mod],
#                i.name,
#                lazy.group[i.name].toscreen(),
#                desc="Switch to group {}".format(i.name),
#            ),
#            # mod1 + shift + letter of group = switch to & move focused window to group
#            Key(
#                [mod, "shift"],
#                i.name,
#                lazy.window.togroup(i.name, switch_group=True),
#                desc="Switch to & move focused window to group {}".format(i.name),
#            ),
#            # Or, use below if you prefer not to switch to that group.
#            # # mod1 + shift + letter of group = move focused window to group
#            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#            #     desc="move focused window to group {}".format(i.name)),
#        ]
#    )


groups = []

# FOR AZERTY KEYBOARDS
group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft",]

group_labels = ["1", "2", "3", "4", "5",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(border_focus='A89984',border_normal='282828', border_width=4,margin=15, ratio=0.60),
]

widget_defaults = dict(
    font="PxPlus IBM VGA 8x16",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [   
                #widget.TextBox(foreground='A5A5A5',fmt=''),
                widget.GroupBox(
                    fontsize=16,
                    rounded=False,
                    active='504945',
                    inactive='504945',
                    borderwidth=5,
                    highlight_method="block",
                    block_highlight_text_color='665C54',
                    this_screen_border='EBDBB2',
                    this_current_screen_border='EBDBB2'),
                widget.TextBox(foreground='D65D0E',fmt='>>',padding=3),
                widget.WindowName(foreground='EBDBB2',fmt='{}',padding=3),
                widget.Wallpaper(directory='/home/knette/Images/wallpaper/',label='',padding=5),
                #widget.Chord(chords_colors={"launch": ("#ff0000", "#ffffff"),},name_transform=lambda name: name.upper(),),
                widget.TextBox(foreground='D79921',fmt='Volume:',padding=0),
                widget.Volume(fmt='{}',foreground='FABD2F',padding=5),
                widget.TextBox(foreground='CC241D',fmt='|',padding=3),
                widget.TextBox(foreground='98971A',fmt='Battery:',padding=5),
                widget.Battery(foreground='B8BB26',format='{percent:2.0%}', low_foreground='FF0000', low_percentage=0.15,padding=5),
                widget.TextBox(foreground='CC241D',fmt='|',padding=3),
                widget.Wlan(interface='wlan0',foreground='83A598',disconnected_message='Disconnected',padding=5),
                widget.TextBox(foreground='CC241D',fmt='|',padding=3),
                widget.Clock(foreground='8EC07C',format="%I:%M",padding=5),
                widget.TextBox(foreground='CC241D',fmt='|',padding=3),
                widget.QuickExit(foreground='EBDBB2',default_text='[shutdown]',countdown_format='[   {}s   ]',padding=3),
                #widget.TextBox(foreground='A5A5A5',fmt=''),
            ],
            24,
            #border_width=[3, 3, 3, 3],  # Draw top, right, bottom, left border
            #border_color=["EBDBB2", "EBDBB2", "EBDBB2", "EBDBB2"],  # Borders are magenta
            background='1D2021'
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
