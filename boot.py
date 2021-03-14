import subprocess
import platform

curr_system = platform.system()


def is_running(name):
	c = int(subprocess.check_output(['osascript', 
		'-e', 'tell application \"System Events\"', 
		'-e', 'count (every process whose name is \"' + name + '\")', 
		'-e', 'end tell']).strip())
	return c > 0

def mac_boot():
	if not is_running('zoom.us'):
		subprocess.call(['/usr/bin/open', '-n', '-a', '/Applications/zoom.us.app'])


def windows_boot():
	subprocess.run('%HOMEPATH%\AppData\Roaming\Zoom\\bin\Zoom.exe', shell=True)

def bootZoom():
	if curr_system != "Darwin":
		windows_boot()
	else:
		mac_boot()