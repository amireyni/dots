#Qtile ?

import os
from libqtile.config import Key , Match , Group , Screen
from libqtile.command import lazy
from libqtile import layout , bar , widget , extension , hook
import iwlib



mod = "mod4"
terminal = "kitty"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod , "shift"], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "g" , lazy.spawn("google-chrome-stable"), desc="open chrome"), 
    Key([mod], "t" , lazy.spawn("telegram-desktop") , desc="open telegram"),
    Key([mod], "c" , lazy.spawn("code"), desc="open Vscode"),
    Key([mod] , "f" , lazy.window.toggle_fullscreen(), desc="fullscreen"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl -- set-sink-volume 0 -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl -- set-sink-volume 0 +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle") ),
    #Key([], "XF86AudioMicMute", lazy.spawn("amixer set Capture togglemute")),
    #Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight-5")),
    #Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight +5")),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
    Key([mod],"1",lazy.group[""].toscreen(),desc="Switch to group " ,),
    Key([mod],"2",lazy.group["爵"].toscreen(),desc="Switch to group 爵" ,),
    Key([mod],"3",lazy.group[""].toscreen(),desc="Switch to group ",),
    Key([mod],"4",lazy.group[""].toscreen(),desc="Switch to group ",),
    Key([mod] , "z" , lazy.spawn("picom")),
    Key([mod] ,"r", lazy.spawn("rofi -no-lazy-grab -show drun -modi run,drun,window -theme ~/.config/rofi/style -drun-icon-theme 'candy-icons'"))
]


groups = [
    Group("" , matches=[Match(wm_class=[terminal])] ,  label=" "),
    Group("爵", matches=[Match(wm_class=["google-chrome-stable"])] ,  label="爵 "),
    Group("", matches=[Match(wm_class=["telegram-desktop"])], label=" "),
    Group("", matches=[Match(wm_class=["code-oss"])]  , label=" "),

]





layouts = [
    layout.Columns(
        border_focus="#669999",
        border_focus_stack = "#669999",
        border_normal="#c1dadb",
        border_normal_stack="c1dadb",
        border_on_single=True,
        border_width = 4,
        margin=[20 , 20 , 20 , 20],
        margin_on_single=[180 , 270 , 180 , 270],
    ),

]




screens = [ 
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    background="#668a87",
                    borderwidth=2,
                    fontsize=16,
                    highlight_method="line"
                ),
                widget.WidgetBox(widgets=[
                    widget.TaskList(
                        background="#2c2e4a",
                        highlight_method="block",
                    )],
                    text_closed="   ",
                    text_open="    ",
                    foreground="#35385e",
                    background="#dfe0eb",
                    fontsize=17,
                ),
                widget.Spacer(),
                widget.Sep(
                    foreground="2a2e2d"
                ),
                widget.Wttr(
                    background="#696969",
                    location={"Marand":"  "},
                    font="JetBrains Mono Bold Italic Nerd Font Complete Mono",
                    fontsize=16,
                    foreground="#80b3ff"
                ),
                widget.Memory(
                    measure_mem="G",
                    format=' {MemUsed: .0f}/{MemTotal: .0f} GB',
                    foreground="#003300",
                    background="#808080",
                    fontsize=16,
                    font="JetBrains Mono Bold Italic Nerd Font Complete Mono",
                    ),
                widget.PulseVolume(
                    background="#909090",
                    emoji=True,
                    font="JetBrains Mono Bold Italic Nerd Font Complete Mono",
                    fontsize=17,
                    foreground="#006666"
                ),
                widget.PulseVolume(
                    background="#909090",
                    emoji=False,
                    font="JetBrains Mono Bold Italic Nerd Font Complete Mono",
                    fontsize=17,
                    foreground="#006666"
                ),
                widget.Battery(
                    background="#A0A0A0",
                    foreground="#33334d",
                    charge_char="    ",
                    discharge_char="    ",
                    empty_char="    ",
                    format='{char}  {percent:2.0%}',
                    font="JetBrains Mono Bold Italic Nerd Font Complete Mono",
                    fontsize=16,
                    full_char="",
                    low_background="#8a1b03",
                    low_percentage=0.3
                ),
                widget.Wlan(
                    background="#B0B0B0",
                    foreground="#267373",
                    interface="wlo1",
                    format='   {percent:2.0%}',
                    disconnected_message="睊  ",
                    fontsize=16,
                    font="JetBrains Mono Bold Italic Nerd Font Complete Mono"
                ),
                widget.KeyboardLayout(
                    background="#BEBEBE",
                    configured_keyboards=["us" , "ir"],
                    display_map={"us":"   " , "ir" : "   "},
                    fontsize=16,
                    foreground="#334d4d"
                ),
                widget.Clock(
                    background="#C8C8C8",
                    foreground="#05262e",
                    fontsize=17,
                    font="JetBrains Mono Bold Italic Nerd Font Complete Mono"
                ),
                widget.QuickExit(
                    default_text="  ",
                    fontsize=18,
                    foreground="#c96d9e",
                    countdown_format='{} 羽',
                    background="#D3D3D3"  
                ),
                widget.Systray(
                    background="#FFFFFF"
                ),

            ],
            35,
            # border_width=[1, 0, 1, 0], 
            #border_color="#484d4c",
            background="#2a2e2d",
            margin=[8 ,18 , 0, 18],
            opacity=0.9,
            
        ),
        wallpaper="~/wallpapers/wallpaper.jpg",
        wallpaper_mode="fill",
    )

]

reconfigure_screens = True
wmname="Qtile"

