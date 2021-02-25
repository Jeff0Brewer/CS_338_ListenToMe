import time
import speech_recognition as sr
from shortcut_control import shortcut
from state_track import state, start_state_checking
from commands import commands
from functions import *
from language_helpers import *
from nlp import mostSimilar, vectorized_commands

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
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration=3)
	r.dynamic_energy_threshold = False

	start_state_checking(2)
	while True:
		with sr.Microphone() as source:
			print(r.energy_threshold)
			audio = r.listen(source)

		text = ''
		try:
			text = r.recognize_google(audio).lower()
			print(text)
		except:
			print('NO SPEECH DETECTED')

		if KEYWORD in text:
			shortcut('focus')
			time.sleep(.1)
			text = sliceAfterSubstr(text, KEYWORD)
			if not text.strip(): continue
			if 'send' not in text:
				text = mostSimilar(text, [x for x in vectorized_commands])[0]
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
		print(state)


if __name__ == '__main__':
	main()
