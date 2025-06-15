#!/bin/sh

#Move the focused container to the specific workspace as shown by fzf
current_ws=$(swaymsg -t get_tree | jq -r '
  def windows:
    if (.nodes // []) != [] then
     (
       (.nodes // [] | map(windows) | add) +
       (.floating_nodes // [] | map(windows) | add)
     )
    elif .name != null then
      [ {id: .id, name: .name} ]
    else
      []
    end;
  .nodes // [] | map(windows) | add | map("\(.id) \(.name)") | .[]
' | fzf --layout=reverse-list --border=rounded --border-label='Fuzzy Switcher')

if [ -z "$current_ws" ]; then
  echo "No container selected."
  exit 1
fi

result=$(echo "$current_ws" | awk '{print $1}')


destination_workspace=$(swaymsg -t get_workspaces | jq -r '.[] | .name' | fzf --layout=reverse-list --border=rounded --border-label='Select Destination Workspace')

if [ -z "$destination_workspace" ]; then
  echo "No destination workspace selected."
  exit 1
fi

swaymsg -q [con_id="$result"] move to workspace $destination_workspace, focus
