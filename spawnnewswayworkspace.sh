#!/bin/sh

# Find the next unused workspace number and switch to it
next_ws=$(swaymsg -t get_workspaces | jq '[.[].num] | max + 1')
swaymsg workspace number $next_ws
