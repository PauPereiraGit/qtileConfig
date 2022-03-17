from libqtile import widget, qtile
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='light', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-3
    )


def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['dark'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),


    # Updates
    powerline('focus', 'dark'),

    icon(bg="focus", text=' '), # Icon: nf-fa-download

    widget.CheckUpdates(
        update_interval=300,
        background=colors['focus'],
        colour_have_updates=colors['urgent'],
        colour_no_updates=colors['light'],
        no_update_string='0 Updates',
        display_format='{updates} Updates',
        padding=8,
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('alacritty -e sudo pacman -Syu')}
    ),


    # Net
    powerline('color9', 'focus'),

    widget.Net(**base(bg='color9'), interface='enp3s0', format='{down} ↓↑ {up} '),


    # CPU
    powerline('focus', 'color9'),

    icon(bg="focus", text='  CPU'), # nf-fa-desktop

    widget.CPU(**base(fg="light", bg='focus'), format='{load_percent}% '),


    # RAM
    powerline('color9', 'focus'),

    icon(bg="color9", text='  RAM'),

    widget.Memory(
        **base(bg='color9'),
        format='{MemUsed: .0f}{mm} ',
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')},
        padding=-2
    ),


    # Layout
    powerline('focus', 'color9'),

    widget.CurrentLayoutIcon(**base(bg='focus'), scale=0.65),

    widget.CurrentLayout(**base(bg='focus'), padding=5),


    # Calendar & Clock
    powerline('color9', 'focus'),

    icon(bg="color9", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(fg="text", bg="color9"), format='%A, '),

    widget.Clock(**base(fg="light", bg="color9"), format='%d/%m/%Y - %H:%M '),


    # Volume
    powerline('focus', 'color9'),

    icon(bg="focus", fontsize=17, text=' '), # Icon: nf-mdi-volume_high

    widget.PulseVolume(
        background=colors['focus'],
        mute_command="pamixer --toggle-mute",
        limit_max_volume=True,
        volume_down_command="pamixer --decrease 5",
        volume_up_command="pamixer --increase 5",
        volume_app="pavucontrol",
        update_interval=0.1,
        padding=8
    )
]


secondary_widgets = [
    *workspaces(),

    separator(),


    # Updates
    powerline('focus', 'dark'),

    icon(bg="focus", text=' '), # Icon: nf-fa-download

    widget.CheckUpdates(
        update_interval=300,
        background=colors['focus'],
        colour_have_updates=colors['urgent'],
        colour_no_updates=colors['light'],
        no_update_string='0 Updates',
        display_format='{updates} Updates',
        padding=8,
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('alacritty -e sudo pacman -Syu')}
    ),


    # Net
    powerline('color9', 'focus'),

    widget.Net(**base(bg='color9'), interface='enp3s0', format='{down} ↓↑ {up} '),


    # CPU
    powerline('focus', 'color9'),

    icon(bg="focus", text='  CPU'), # nf-fa-desktop

    widget.CPU(**base(fg="light", bg='focus'), format='{load_percent}% '),


    # RAM
    powerline('color9', 'focus'),

    icon(bg="color9", text='  RAM'),

    widget.Memory(
        **base(bg='color9'),
        format='{MemUsed: .0f}{mm} ',
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')},
        padding=-2
    ),


   # Layout
    powerline('focus', 'color9'),

    widget.CurrentLayoutIcon(**base(bg='focus'), scale=0.65),

    widget.CurrentLayout(**base(bg='focus'), padding=5),


    # Calendar & Clock
    powerline('color9', 'focus'),

    icon(bg="color9", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(fg="text", bg="color9"), format='%A, '),

    widget.Clock(**base(fg="light", bg="color9"), format='%d/%m/%Y - %H:%M '),


    # Volume
    powerline('focus', 'color9'),

    icon(bg="focus", fontsize=17, text=' '), # Icon: nf-mdi-volume_high

    widget.PulseVolume(
        background=colors['focus'],
        mute_command="pamixer --toggle-mute",
        limit_max_volume=True,
        volume_down_command="pamixer --decrease 5",
        volume_up_command="pamixer --increase 5",
        volume_app="pavucontrol",
        update_interval=0.1,
        padding=8
    )
]


widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}


extension_defaults = widget_defaults.copy()
