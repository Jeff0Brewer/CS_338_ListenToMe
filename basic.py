import time
import speech_recognition as sr
from shortcut_control import shortcut
from state_track import state, start_state_checking
from commands import *
from language_helpers import *

KEYWORD = "hey tony"

commands = {
	'toggle my hand': toggle_hand,
	'toggle fullscreen': toggle_fullscreen,
	'mute me': mute,
	'unmute me': unmute,
	'start my video': start_video,
	'stop my video': stop_video,
	'open the chat': open_chat,
	'close the chat': close_chat,
	'send this message': send_chat,
	'stop listening': quit
}

macros = {}
with open('user_settings.txt') as file:
	text = file.read()
	KEYWORD = sliceBetweenSubstr(text, 'SYSTEM_KEYWORD_\n', '\n\nMACRO_COMMANDS_')
	for line in text.split('MACRO_COMMANDS_\n')[1].split('\n'):
		command, content = line.split(': ')
		commands['send ' + command] = send_chat
		macros['send ' + command] = content + '\n'

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
		for command, callback in commands.items():
			if command in text:
				if 'send' in command:
					if 'message' in command:
						callback(sliceAfterSubstr(text, command + ' ') + '\n')
					else:
						callback(macros[command])
				else:
					callback()
	print(state)
