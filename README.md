# FZF_Scripts

# Collection of some hacky-ass fzf scripts. Intended for Sway originally. Assume FZF and Ripgrep as Dependencies. Still a WIP.

## Script list/description:

### fzf-power-menu:

Very similar to power menu in something like rofi/wofi. No crazy dependencies besides systemd and sway here

### fzf-clipboard:

Simple clipboard manager. Works well and fast. Stores a bunch of whatever you copy.

To run this, I use the following command in my sway config:

exec_always --no-startup-id wl-paste --watch cliphist store

### fzf-menu-py:

This works really similarly to how I think dmenu does it. Essentially grabs desktop files,
parses the desktop files for the entry, and executable message. Removes some  commands that were a
PITA for me. 

Works surprisingly quickly for all it has to do and haven't had issues running anything it gives
as an option. It can show more than you may want, however. Could probably tweak as needed.

Requires subprocess, os, configparser, and glob imports if you don't have these for osme reason
Could probably do this with less, but more of a ease versus dependencies thing.

### fzf-switch-bluetooth:

Think of this like a dumb light switch that looks at previously connected bluetooth devices
and switches it on or off. Requires bluetoothctl, which I think is reasonable for a 
bluetooth tool

### fzf-change-audio:

Don't know how important for those who don't have a laptop that's possessed like I apparently
do, but it allows you to easily choose your default sink if it gets switched for some reason.

Requires pactl here to work.

### fzf-list-system:

This is a big fat pig of a shell script. Some of this stuff I could probably get from some 
obscure files that I don't know. Let me know if you have something I could use instead.

Requires: timedatectl, acpi (battery), iostat, lscpu, lm-sensors, light, pactl, iwconfig

Has the ability to go to workspace switcher from here. Just have home environment variable set
and change the path as you need to for the script

###  fzf-changeworkspace:

This parses get_tree from swaymsg with jq for active nodes. Has the functions for searching grouped
workspaces and floating nodes.

Obviously requires sway running and swaymsg. Also requires jq.

### fzf-activeworkspaces:

This is a more stable version of the above but it only goes to workspace level and not window leve.

Requires sway and swaymsg as well as jq like before.

### fzfspotify:

This is very much a work in progress still. Currently, allows Full Playlist, Play Artist, Single song,
Previous, Skip, Play, Pause. Spotify deprecated their similar songs api and as such I've decided
to opt for looking through last fm for similar songs. This all works up until i use the /me to add to queue.
Requires a type of authentication that I still haven't implemented yet. We'll get to it.

Requires spotifyd compiled with mpris functionality.

Python imports: os, psutil, sys, time, requests, subprocess

Requires SPOTIFY_CLIENT_ID, SPOTIFY_SECRET_ID, and LASTFM_API Environment variables.

Full disclosure: I had my home directory hard coded originally. I added the home get_env_var 
call for this to seem professional. If it doesn't work, that's probably the issue.

Make sure to change the path for spotifyd. It is ~/.local/bin/spotifyd for me.

# Overall:

Most of the scripts are ugly but work for me. Feel free to change and update as you want.

The launcher scripts and scripts that do something run well in a sway(maybe wlroots I dunno) 
keybind that opens a terminal the script. This is because of the automagic that 
sway does that allows the terminal to detach and close unlike many other DE's/WM's.
