import os, time, threading
from python_imagesearch.imagesearch import imagesearch
import platform

state = {
	'audio': 0,
	'video': 0,
	'chat': 0,
	'share': 0
}

# images may need to change for different ui settings
img_path = 'img'
if platform.system != 'Darwin':
	img_path = os.path.join(img_path, 'win')
checks = [
	[os.path.join('img', 'unmute.png'), 'audio', 0],
	[os.path.join('img', 'mute.png'), 'audio', 1],
	[os.path.join('img', 'start_video.png'), 'video', 0],
	[os.path.join('img', 'stop_video.png'), 'video', 1],
	[os.path.join('img', 'chat_menu.png'), 'chat', 1, 0],
	[os.path.join('img', 'stop_share.png'), 'share', 1, 0]
]

checking = False

def start_state_checking(wait_time):
	global checking
	checking = True
	for check in checks:
		check_state(check, wait_time)

def stop_state_checking():
	global checking
	checking = False

def check_state(check, wait_time):
	search_thread = threading.Thread(
		target=search_loop, 
		name='search_' + check[0], 
		args=[
			check[0], 
			check[1], 
			check[2], 
			-1 if len(check) != 4 else check[3], 
			wait_time])
	search_thread.start()

def search_loop(image_path, state_key, check_value, alt_value, wait_time):
	global checking
	global state

	while checking:
		pos = imagesearch(image_path, .8)
		if pos[0] != -1:
			state[state_key] = check_value
		else: 
			if alt_value != -1:
				state[state_key] = alt_value
		time.sleep(wait_time)
