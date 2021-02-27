import threading
import speech_recognition as sr

text_stream = ['']
listening = False

r = sr.Recognizer()
r.dynamic_energy_threshold = False
r.pause_threshold = .6
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source, duration=3)
print(r.energy_threshold)

def recognize_callback(audio):
	global text_stream
	try:
		text_stream[0] += r.recognize_google(audio).lower() + ' '
	except:
		pass

def listen_loop():
	while listening:
		with sr.Microphone() as source:
			audio = r.listen(source, phrase_time_limit=10)
		recognize_thread = threading.Thread(
			target=recognize_callback, 
			name='recognize_thread', 
			args=[audio])
		recognize_thread.start()

def start_listen():
	global listening
	listening = True
	listen_thread = threading.Thread(
		target=listen_loop,
		name='listen_thread')
	listen_thread.start()

def stop_listen():
	global listening
	listening = False
