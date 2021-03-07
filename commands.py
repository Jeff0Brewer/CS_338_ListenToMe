from functions import *
from language_helpers import *

commands = {
    'toggle my hand': toggle_hand,
    'toggle full screen': toggle_fullscreen,
    'unmute me': unmute,
    'mute me': mute,
    'start my video': start_video,
    'stop my video': stop_video,
    'share my screen': start_share,
    'stop sharing my screen': stop_share,
    'open the chat': open_chat,
    'close the chat': close_chat,
    'send this message': send_chat,
    'stop listening': quit,
    'leave the meeting': leave_meeting,
}

macros = {}
KEYWORD = ""
with open('user_settings.txt') as file:
	text = file.read()
	KEYWORD = sliceBetweenSubstr(text, 'SYSTEM_KEYWORD_\n', '\n\nZOOM_SHORTCUTS_').lower()
	for line in text.split('MACRO_COMMANDS_\n')[1].split('\n'):
		command, content = line.split(': ')
		commands['send ' + command] = send_chat
		macros['send ' + command] = content + '\n'

main_commands = commands.copy()

