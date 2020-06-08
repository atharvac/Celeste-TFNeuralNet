#import tensorflow as tf
import numpy as np
import cv2
import time
import pyautogui
from pyautogui import keyDown, keyUp, press

data = np.load("training_data.npy", allow_pickle=True)


def show_data():
	for x in data:
		img = x[0]
		cv2.imshow("a", img/255.0)
		print(x[1])
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

#show_data()

cv2.imshow('a', data[2][0].reshape(250,149)/255.0)
cv2.waitKey(0)
cv2.destroyAllWindows()