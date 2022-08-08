# local-program-launcher (Cengrum)

User can quickly start scripts up from the system tray.

## Prerequisites
- Python 3+
- pip modules
	- pystray
	- pillow 
	- ctypes

## Setting it up
1. Run the program. If you want, you can create a shortcut to it in the startup folder of your system.
2. An icon will appear in the notification area (system tray). Right-click on the icon.
3. A list of your scripts will be visible in the options. Clicking on any script will launch it immediately. Note that to view these, you'll have to add the scripts' paths to the `path.json` file first.

### Adding your scripts' paths
In the `paths.json` file:
```json
{
	"name_of_script1": "path/to/script1",
	"name_of_script2": "path/to/script2"
}
```
