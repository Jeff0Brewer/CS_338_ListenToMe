import speech_recognition as sr
from shortcut_control import shortcut
from state_track import state, start_state_checking, stop_state_checking
import time
from language_helpers import *

KEYWORD = "hey montana"

keywords = {
	'toggle_audio': 'toggle my audio',
	'toggle_video': 'toggle my video',
	'toggle_chat': 'toggle the chat',
	'start_meeting': 'start a new meeting',
	'toggle_minimal': 'switch to minimal window',
	'toggle_hand_raise': 'toggle my hand raise',
	'send_chat': 'send this message',
	'quit': 'stop listening'
}

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=3)
r.dynamic_energy_threshold = False


start_state_checking(3)
while True:
	with sr.Microphone() as source:
		print(r.energy_threshold)
		audio = r.listen(source)

	text = ''
	try:
		text = r.recognize_google(audio)
		print(text)
	except:
		print('NO SPEECH DETECTED')

	if text: shortcut('focus')
	time.sleep(.1)

	if KEYWORD in text:
		text = sliceAfterSubstr(text, KEYWORD)
		for command, kw in keywords:
			if kw in text:
				if command not in ['toggle_chat', 'send_chat', 'quit']:
					shortcut(command)
				if command == 'send_chat':
					if state['chat'] == 1:
						shortcut('toggle_chat')
					shortcut('toggle_chat', content=text.split(
						keywords['send_chat'])[1][1:] + '\n')
					if state['chat'] == 0:
						shortcut('toggle_chat')
				if command == 'quit':
					stop_state_checking()
					exit()

	print(state)