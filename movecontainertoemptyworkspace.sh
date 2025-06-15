#!/bin/sh

#Move the currently focused container to the next empty workspace
next_ws=$(swaymsg -t get_workspaces | jq '[.[].num] | max + 1')
current_ws=$(swaymsg -t get_tree | jq -r '.. | select(.focused? == true) | .workspace')

swaymsg move container to workspace $next_ws
swaymsg workspace $next_ws
