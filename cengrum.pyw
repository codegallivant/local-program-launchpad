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


iconpath = "favicon.ico"
im = PIL.Image.open(iconpath)


def run_program_in_new_window(icon, filepath):
    def real_run_program_in_new_window_func(icon):
        try:
            subprocess.Popen([filepath], shell=True, cwd = os.path.dirname(filepath))
        except Exception as e:
            print(e)
            if type(e).__name__ == "FileNotFoundError":
                pag.alert(text = f"{filepath} not found.", title = "Cengrum")
            else:
                pag.alert(text = e, title = "Cengrum - Error")
    return real_run_program_in_new_window_func



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
        menu =  pystray.Menu(*menu, pystray.MenuItem(program_name, run_program_in_new_window(iconpath, filepaths[program_name])))
    return menu


filepaths_dict = update_paths()
submenu = build_submenu(filepaths_dict)
print(submenu)


def open_pathsjsonfile():
    subprocess.check_output(["notepad.exe", "paths.json"])
    restart_program_fromSysTray(icon, None)


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



icon = pystray.Icon("cengrum-icon",im,"Cengrum", menu=icon_menu)
icon.run()
