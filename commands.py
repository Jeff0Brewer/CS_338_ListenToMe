from shortcut_control import shortcut
from state_track import state, stop_state_checking

def toggle_hand():
	shortcut('toggle_hand')

def toggle_fullscreen():
	shortcut('toggle_fullscreen')

def unmute():
	if state['audio'] == 0:
		shortcut('toggle_audio')

def mute():
	if state['audio'] == 1:
		shortcut('toggle_audio')

def start_video():
	if state['video'] == 0:
		shortcut('toggle_video')

def stop_video():
	if state['video'] == 1:
		shortcut('toggle_video')

def open_chat():
	if state['chat'] == 0:
		shortcut('toggle_chat')

def close_chat():
	if state['chat'] == 1:
		shortcut('toggle_chat')

def send_chat(message):
	if state['chat'] == 1:
		shortcut('toggle_chat')
	shortcut('toggle_chat', content=message)
	if state['chat'] == 0:
		shortcut('toggle_chat')

def quit():
	stop_state_checking()
	exit()
