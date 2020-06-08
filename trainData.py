import numpy as np
from getkeys import key_check
import d3dshot
import os
import cv2
import time

#(350, 208)
OUT_SIZE = (250, 149)


def out_keys(keys=[]):
	combos = ['L', 'R', 'C', 'X', 'Z', 'CR', 'CU', 'CL', 'CD', 'UZ', 'DZ', 'RX',
			  'LX', 'RUX', 'LUX', 'DRX', 'DLX', 'CDRX']
	output = np.eye(len(combos)+1)
	keys.sort()
	key_combo = "".join(keys)
	for i, x in enumerate(combos):
		if key_combo == x:
			return output[i]
	return output[-1]



file_name = "training_data.npy"

if os.path.isfile(file_name):
	print("Loading previous data!")
	data = list(np.load(file_name, allow_pickle=True))
else:
	print("Previous data not found. Generating new file!")
	data = []

screen = d3dshot.create(capture_output="numpy")

def start():
	while True:
		still = screen.screenshot((0,40,960,570))
		still = cv2.cvtColor(still, cv2.COLOR_BGR2GRAY)
		still = cv2.resize(still, OUT_SIZE)/255.0
		keys = key_check()
		keys = out_keys(keys)
		data.append([still, keys])

		size = len(data)
		if size % 2000 == 0:
			np.save(file_name, data)
			print(f"Data length: {size}")


for x in range(5):
	time.sleep(1)
	print(x)
start()
#print(out_keys(['C', 'R', 'D', 'X']))