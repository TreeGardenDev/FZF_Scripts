#!/usr/bin/python3
##Purpose: List all execuatble desktop applications in the system
import subprocess
import os
import glob
import configparser

desktop_dict= {}
def get_desktop_files():
    
    desktop_files = []
    for path in ['/usr/share/applications', '/usr/local/share/applications', os.path.expanduser('~/.local/share/applications')]:
        desktop_files.extend(glob.glob(os.path.join(path, '*.desktop')))
    return desktop_files

def parse_desktop_file(file_path):
    config = configparser.ConfigParser(interpolation=None)
    config.read(file_path)
    try:
        name = config.get('Desktop Entry', 'Name')

        if 'Exec' not in config['Desktop Entry']:
            return None, None

        command = config.get('Desktop Entry', 'Exec').replace('%u', '').replace('%U', '').replace('%f', '').replace('%F', '').strip()
        if 'Terminal' in config['Desktop Entry'] and config.getboolean('Desktop Entry', 'Terminal'):
            command = f"alacritty -e {command}"
        #if the 
        
        
        return name, command
    finally:
        #Closed
        a=1
def show_all_applications():
    echo_string = []
    for name, command in desktop_dict.items():
        echo_string.append(str(name))

    result = subprocess.run(["fzf", "--layout=reverse-list", "--border=rounded", "--border-label='Fuzzy Menu'"], input=" \n".join(echo_string), text=True, capture_output=True)
    if result.returncode != 0:
        print("No application selected.")
        return

    result=result.stdout.strip()

    execute=desktop_dict[result]
    print(execute)
    _=run_executable(execute)



def run_executable(command):
    result = subprocess.run(['xargs', '-r', 'swaymsg', 'exec', '--'], input=command, text=True, capture_output=True)

    return result.stdout
def main():
    files= get_desktop_files()
    for file in files:  
        name, command = parse_desktop_file(file)
        desktop_dict[name] = command
    show_all_applications()

    
if __name__ == "__main__":
    main()
