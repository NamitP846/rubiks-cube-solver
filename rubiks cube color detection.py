import cv2
import numpy as np
from pathlib import Path

img = str(Path(__file__).parent) + '//testimg.png'

frame = cv2.imread(img)
HSVimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
facehsv = np.array([[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]])

h, w, _ = frame.shape

deltax = int(w/6)
deltay = int(h/6)
x1, y1 = int(w/12), int(h/12)

for i in range(3):
    x01 = x1 + 2*i*deltax
    x02 = x1 + 2*i*deltax + deltax
    for j in range(3):
        y01 = y1 + 2*j*deltay
        y02 = y1 + 2*j*deltay + deltay
        cv2.rectangle(frame, (x01, y01), (x02, y02), (0, 0, 255), 5)
        avghue = float(np.median(HSVimage[y01:y02, x01:x02, 0]))
        avgsat = float(np.median(HSVimage[y01:y02, x01:x02, 1]))
        avgval = float(np.median(HSVimage[y01:y02, x01:x02, 2]))
        facehsv[i][j][0] = avghue
        facehsv[i][j][1] = avgsat
        facehsv[i][j][2] = avgval

print(facehsv)

while True:
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()