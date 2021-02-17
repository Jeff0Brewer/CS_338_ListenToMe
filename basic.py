import speech_recognition as sr # ref: https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
from shortcut_control import shortcut

keywords = {
	'key_phrase': 'hey listen to me',
	'toggle_audio': 'audio',
	'toggle_video': 'video',
	'toggle_chat': 'chat',
	'start_meeting': 'new meeting',
	'toggle_minimal': 'minimal',
	'toggle_hand_raise': 'hand',
	'send_chat': 'send message',
	'quit': 'stop listening'
}

r = sr.Recognizer()
while True:
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	text = ''
	try:
		text = r.recognize_google(audio);
		print(text);
	except:
		print('NO SPEECH DETECTED')

	if keywords['key_phrase'] in text:

		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)

		text = ''
		try:
			text = r.recognize_google(audio);
			print(text);
		except:
			print('SORRY I DID NOT CATCH THAT')


		if keywords['toggle_audio'] in text:
			shortcut('toggle_audio')
		if keywords['toggle_video'] in text:
			shortcut('toggle_video')
		if keywords['start_meeting'] in text:
			shortcut('start_meeting')
		if keywords['toggle_minimal'] in text:
			shortcut('toggle_minimal')
		if keywords['toggle_hand_raise'] in text:
			shortcut('toggle_hand_raise')
		if keywords['send_chat'] in text:
			shortcut('toggle_chat', content = text.split(keywords['send_chat'])[1][1:] + '\n')
			shortcut('toggle_chat')
		if keywords['quit'] in text:
			exit()
