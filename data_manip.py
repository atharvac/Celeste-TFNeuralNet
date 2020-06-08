import pandas as pd
import numpy as np
import cv2
from collections import Counter
import random


combos = ['L', 'R', 'C', 'X', 'Z', 'CR', 'CU', 'CL', 'CD', 'UZ', 'DZ', 'RX',
			  'LX', 'RUX', 'LUX', 'DRX', 'DLX', 'CDRX', 'NaN']
data = np.load("training_data.npy", allow_pickle=True)
d = pd.DataFrame(data)

count = Counter(d[1].apply(np.argmax))


print(count)
for x in count.keys():
	print(f"{combos[x]} : {count[x]}, ", end='')
print()
np.random.shuffle(data)

idxs = []
for i, x in enumerate(data):
	if np.argmax(x[1]) == 1:
		idxs.append(i)

print(f"\nIndexes are {len(idxs)}")
print(f"Total Data: {len(data)}")

#data = np.delete(data, idxs[:1600], axis=0)
#np.save("training_data", data)