import cv2
import numpy as np

cam = cv2.VideoCapture(0)
x1, y1, x2, y2 = 25, 25, 75, 75

while True:
    ret, frame = cam.read()
    HSVimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
    avghue = np.median(HSVimage[y1:y2, x1:x2, 0])
    avgsat = np.median(HSVimage[y1:y2, x1:x2, 1])
    avgval = np.median(HSVimage[y1:y2, x1:x2, 2])

    if avgsat <= 100 and avgval >= 150:
        color = 'W'
    elif 8 <= avghue <= 24 and avgval >= 240:
        color = 'O'
    elif 25 <= avghue <= 30 and 140 <= avgsat <= 175 and 165 <= avgval:
        color = 'Y'
    elif 55 <= avghue <= 80:
        color = 'G'
    elif 85 <= avghue <= 100:
        color = 'B'
    elif 160 <= avghue:
        color = 'R'
    elif avghue <= 20:
        color = 'R'

    cv2.putText(frame, color, (200, 200), 0, 5, (0, 0, 255), 5)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()