from pykeyboard import PyKeyboard # git: https://github.com/SavinaRoja/PyUserInput/blob/master/pykeyboard
import keyboard # doc: https://pypi.org/project/keyboard/
import platform

# Check if Mac or Windows
system = platform.system() 

k = PyKeyboard()

if system == 'Darwin':
	# Mac OS shortcuts
	shortcuts = {
		'toggle_video': ['shift', 'command', 'v'],
		'toggle_audio': ['shift', 'command', 'a'],
		'toggle_chat': ['shift', 'command', 'h'],
		'start_meeting': ['control', 'command', 'v'],
		'toggle_minimal': ['shift', 'command', 'm'],
		'toggle_hand_raise': ['control', 'y'],
		'focus': [],
		'fullscreen': ['shift', 'command', 'f']
	}
else:
	# Windows shortcuts
	shortcuts = {
		'toggle_video': [k.alt_key, 'v'],
		'toggle_audio': [k.alt_key, 'a'],
		'toggle_chat': [k.alt_key, 'h'],
		'start_meeting': [],
		'toggle_minimal': [k.alt_key, 'm'],
		'toggle_hand_raise': [k.alt_key, 'y'],
		'focus': [k.control_key, k.alt_key, k.shift_key],
		'fullscreen': [k.alt_key, 'f']
	}

# function to call a shortcut and optionally type out a string
def shortcut(identifier, content = ''):
	k.press_keys(shortcuts[identifier])
	if(len(content) > 0):
		keyboard.write(content)

