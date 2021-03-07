from language_helpers import *
from pykeyboard import PyKeyboard # git: https://github.com/SavinaRoja/PyUserInput/blob/master/pykeyboard
import keyboard # doc: https://pypi.org/project/keyboard/
import platform
import time

# Check if Mac or Windows
curr_system = platform.system() 

k = PyKeyboard()
shortcuts = {}

windows_keymap = {}
if curr_system != 'Darwin':
	windows_keymap = {
		'alt': k.alt_key,
		'control': k.control_key,
		'shift': k.shift_key,
	}
	shortcuts['focus'] = [k.control_key, k.alt_key, k.shift_key]
else:
	shortcuts['focus'] = []

with open('user_settings.txt') as file:
	text = file.read()
	shortcut_settings = sliceBetweenSubstr(text, 'ZOOM_SHORTCUTS_\n', '\n\nMACRO_COMMANDS_').split('\n')
	for line in shortcut_settings: 
		name, keys = line.split(': ')
		name = 'toggle_' + name
		keys = keys.split(', ')
		if curr_system != 'Darwin':
			for i in range(len(keys)):
				if keys[i] in windows_keymap:
					keys[i] = windows_keymap[keys[i]]
		shortcuts[name] = keys

# function to call a shortcut and optionally type out a string
def shortcut(identifier, content = ''):
	k.press_keys(shortcuts[identifier])
	if(len(content) > 0):
		keyboard.write(content)
	time.sleep(.2)
