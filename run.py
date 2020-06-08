import win32api as wapi
import numpy as np
import d3dshot
import pyautogui
import time
import os
import cv2


screen = d3dshot.create(capture_output="numpy")
import tensorflow as tf
OUT_SIZE = (250, 149)
model = tf.keras.models.load_model("Colab Trained/model")

combos = [['left'],
		  ['right'],
		  ['c'],
		  ['x'],
		  ['z', 'up'],
		  ['c','right'],
		  ['c','up'],
		  ['c','left'],
		  ['c','down'],
		  ['up','z'],
		  ['down','z'],
		  ['right,x'],
		  ['left','x'],
		  ['right','up','x'],
		  ['left','up','x'],
		  ['down','right','x'],
		  ['down','left','x'],
		  ['c','down','right','x'],
		  ['NaN']
]

def keypress(key, delay=0.001):
	print(f"Pressing keys: {key}")
	if key[0] == 'NaN':
		#time.sleep(delay)
		return
	else:
		for x in key:
			pyautogui.keyDown(x)
		#time.sleep(delay)
		for x in key:
			pyautogui.keyUp(x)


def start():
	while True:
		still = screen.screenshot((0,40,960,570))
		still = cv2.cvtColor(still, cv2.COLOR_BGR2GRAY)
		still = cv2.resize(still, OUT_SIZE)/255.0

		still = still.reshape(1, 149, 250, 1)

		keys = np.argmax(model.predict([still]), axis=-1)
		print(keys[0])
		keys = combos[keys[0]]
		keypress(keys)
		if wapi.GetAsyncKeyState(ord('Q')):
			pause=input()



for x in range(0, 4, -1):
	time.sleep(1)
	print(f"Starting in : {x}")

start()



"""		cv2.imshow("a", still)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
"""