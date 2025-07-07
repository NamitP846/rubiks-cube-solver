import cv2
import numpy as np
from pathlib import Path

img = str(Path(__file__).parent) + '//WIN_20250706_17_03_00_Pro.jpg'
#img = str(Path(__file__).parent) + '//testimg.png'

frame = cv2.imread(img)
HSVimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

delta = 100
delta = 85

x1, y1, x2, y2 = 25, 25, 75, 75

red = 180
orange = 10

for i in range(3):
    x01 = x1 + i*delta
    x02 = x2 + i*delta
    for j in range(3):
        y01 = y1 + j*delta
        y02 = y2 + j*delta
        cv2.rectangle(frame, (x01, y01), (x02, y02), (0, 0, 255), 5)
        avghue = np.mean(HSVimage[y01:y02, x01:x02, 0])
        avgsat = np.mean(HSVimage[y01:y02, x01:x02, 1])
        avgval = np.mean(HSVimage[y01:y02, x01:x02, 2])
        print(str(avghue), str(avgsat), str(avgval))

while True:
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()