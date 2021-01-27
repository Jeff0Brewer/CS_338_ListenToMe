from pykeyboard import PyKeyboard # git: https://github.com/SavinaRoja/PyUserInput/blob/master/pykeyboard
import keyboard # doc: https://pypi.org/project/keyboard/

k = PyKeyboard()

# shortcuts only currently defined for mac os
shortcuts = {
	'toggle_video': ['shift', 'command', 'v'],
	'toggle_audio': ['shift', 'command', 'a'],
	'toggle_screen_share': ['shift', 'command', 's'],
	'toggle_chat': ['shift', 'command', 'h'],
	'join_meeting': ['command', 'j'],
	'start_meeting': ['control', 'command', 'v'],
	'toggle_minimal': ['shift', 'command', 'm'],
	'toggle_hand_raise': ['control', 'y']
}

# function to call a shortcut and optionally type out a string
def shortcut(identifier, content = ''):
	for key in shortcuts[identifier]:
		k.press_key(key)
	for key in shortcuts[identifier]:
		k.release_key(key)
	if(len(content) > 0):
		keyboard.write(content)
