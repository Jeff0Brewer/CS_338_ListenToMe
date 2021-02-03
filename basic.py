import speech_recognition as sr
from shortcut_control import shortcut

keywords = {
	'audio': 'audio',
	'video': 'video',
	'send_chat': 'send message',
	'toggle_chat': 'chat',
	'screen_share': 'screen share',
	'start_meeting': 'new meeting',
	'toggle_minimal': 'minimal',
	'toggle_hand_raise': 'hand',
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

	if keywords['audio'] in text:
		shortcut('toggle_audio')
	if keywords['video'] in text:
		shortcut('toggle_video')
	if keywords['screen_share'] in text:
		shortcut('toggle_screen_share')
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