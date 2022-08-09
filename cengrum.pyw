import subprocess
import os
import sys 
import pystray
import json
import PIL
import PIL.Image
import pyautogui as pag
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("Cengrum")


def restart_program_fromSysTray(icon, item):
    icon.stop()
    os.execl(sys.executable, sys.executable, *sys.argv)

def quit_program_fromSysTray(icon, item):
    icon.stop()
    os._exit(0)


def update_paths():
    if not os.path.isfile("paths.json"):
        f = open("paths.json",'w')
        f.write('{\n\n\n}')
    f = open("paths.json",'r')
    filepaths = json.loads(f.read())
    return filepaths

def build_submenu(filepaths):
    menu = tuple()
    for program_name in list(filepaths.keys()):
        print(filepaths[program_name])
        menu = menu + (pystray.MenuItem(program_name, lambda: run_program_in_new_window(filepaths[program_name])), )
    fullmenu = pystray.Menu(*menu)
    return fullmenu


filepaths_dict = update_paths()
submenu = build_submenu(filepaths_dict)


def open_pathsjsonfile():
    subprocess.check_output(["notepad.exe", "paths.json"])
    restart_program_fromSysTray(icon, None)


im = PIL.Image.open("favicon.ico")
icon_menu = pystray.Menu(
    pystray.MenuItem(
        'Run programs', 
        submenu),
    pystray.MenuItem(
        'Add programs',
        open_pathsjsonfile),
    pystray.MenuItem('Restart', 
        restart_program_fromSysTray),
    pystray.MenuItem(
        'Quit',
        quit_program_fromSysTray))


def run_program_in_new_window(filepath):
    extension = os.path.splitext(filepath)[1]
    print(filepath) 
    print(extension)
    if extension == ".py":
        command = "python"
    elif extension == ".pyw":
        command = "pythonw"
    else:
        pag.alert(text = f"{filepath} extension not supported.", title="Cengrum")
        return
    try:
        subprocess.Popen([command, filepath], shell=True, cwd = os.path.dirname(filepath))
    except Exception as e:
        print(e)
        if type(e).__name__ == "FileNotFoundError":
            pag.alert(text = f"{filepath} not found.", title = "Cengrum")


icon = pystray.Icon("cengrum-icon",im,"Cengrum", menu=icon_menu)
icon.run()

