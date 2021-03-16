import time, threading, platform, os
from nlp import mostSimilar, vectorized_commands
from speechrecog import text_stream, start_listen
from state_track import state, start_state_checking
from shortcut_control import shortcut
from commands import KEYWORD, commands, macros
from functions import *
from language_helpers import *
from boot import bootZoom
from preferences import commandLineControlMac

curr_system = platform.system()

def main():
	commandLineControlMac()
	bootZoom()

	global text_stream

	start_state_checking(1)
	start_listen()
	while True:
		while KEYWORD not in text_stream[0]:
			time.sleep(.25)
		raw_text = text_stream[0]
		text_stream[0] = ''

		print(raw_text)
		print(state)

		if curr_system == 'Darwin':
			os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "zoom.us" to true' ''')
		else:
			shortcut('focus')

		time.sleep(.1)

		raw_text = sliceAfterSubstr(raw_text, KEYWORD)
		if " and " in raw_text:
			texts = [sliceUpToSubstr(raw_text, " and "), sliceAfterSubstr(raw_text, " and ")]
		else:
			texts = [raw_text]
		for text in texts:
			if not text.strip(): continue
			compared = mostSimilar(text, [x for x in vectorized_commands])[0]
			if 'send this message' not in compared:
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