import os, time, threading
from python_imagesearch.imagesearch import imagesearch
from shortcut_control import curr_system

state = {
	'audio': 0,
	'video': 0,
	'chat': 0,
	'share': 0
}

# images may need to change for different ui settings
img_path = 'img'
if curr_system != 'Darwin':
	img_path = os.path.join(img_path, 'win')
checks = [
	[os.path.join(img_path, 'unmute.png'), 'audio', 0, -1],
	[os.path.join(img_path, 'mute.png'), 'audio', 1, -1],
	[os.path.join(img_path, 'start_video.png'), 'video', 0, -1],
	[os.path.join(img_path, 'stop_video.png'), 'video', 1, -1],
	[os.path.join(img_path, 'chat_menu.png'), 'chat', 1, 0],
	[os.path.join(img_path, 'stop_share.png'), 'share', 1, 0]
]

checking = False

def start_state_checking(wait_time):
	global checking
	checking = True
	search_thread = threading.Thread(
		target=search_loop, 
		name='state_search', 
		args=[checks, wait_time])
	search_thread.start()

def stop_state_checking():
	global checking
	checking = False
	
def search_loop(checks, wait_time):
	global checking
	global state

	while checking:
		precision = .8 if curr_system == 'Darwin' else .9
		for check in checks:
			if imagesearch(check[0], precision)[0] != -1:
				state[check[1]] = check[2]
			else: 
				if check[3] != -1:
					state[check[1]] = check[3]
			time.sleep(wait_time)

