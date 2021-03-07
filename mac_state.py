from pyautogui import*
from python_imagesearch.imagesearch import imagesearch
from AppKit import NSWorkspace
import os, time, threading
# from shortcut_control import curr_system
# if curr_system == Darwin:

counter = 0
for apps in NSWorkspace.sharedWorkspace().launchedApplications():
	# print([apps["NSApplicationName"]])
	counter = counter + 1

precision = .8
#might need to change out png depending on dark mode or not
img_path = 'img'

check_image = os.path.join(img_path, 'zoomus.png')
pos = imagesearch(check_image, precision)

if pos[0] != -1:
    print("zoom open")

else:
	for i in range(1, counter):
		keyDown('command')
		press('Tab', presses=i)
		keyUp('command')
		pos = imagesearch(check_image, precision)
		if pos[0] != -1:
			print("now on zoom window")
			break
