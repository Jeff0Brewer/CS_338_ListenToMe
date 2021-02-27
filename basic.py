import time, threading
from nlp import mostSimilar, vectorized_commands
from speechrecog import text_stream, start_listen
from state_track import state, start_state_checking
from shortcut_control import shortcut
from commands import commands
from functions import *
from language_helpers import *

KEYWORD = "hey tony"

macros = {}
with open('user_settings.txt') as file:
	text = file.read()
	KEYWORD = sliceBetweenSubstr(text, 'SYSTEM_KEYWORD_\n', '\n\nZOOM_SHORTCUTS_')
	for line in text.split('MACRO_COMMANDS_\n')[1].split('\n'):
		command, content = line.split(': ')
		commands['send ' + command] = send_chat
		macros['send ' + command] = content + '\n'

def main():
	global text_stream

	start_state_checking(3)
	start_listen()
	while True:
		while KEYWORD not in text_stream[0]:
			time.sleep(.25)
		text = text_stream[0]
		text_stream[0] = ''

		print(text)
		print(state)

		shortcut('focus')
		time.sleep(.1)

		text = sliceAfterSubstr(text, KEYWORD)
		if not text.strip(): continue
		compared = mostSimilar(text, [x for x in vectorized_commands])[0]
		if 'send' not in compared:
			text = compared
		for command, callback in commands.items():
			if command in text:
				if 'send' in command:
					if 'message' in command:
						callback(sliceAfterSubstr(text, command + ' ') + '\n')
					else:
						callback(macros[command])
				else:
					callback()
				break


if __name__ == '__main__':
	main()