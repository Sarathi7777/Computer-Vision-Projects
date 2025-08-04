import cv2
import numpy as np
video_source = ("C:/Users/sarat/Downloads/AMD Radeon PRO x Blender _ Mercedes-AMG Petronas F1 Team 8 x F1 Champions of the World.mp4")
capture = cv2.VideoCapture(video_source)
while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Canny Edge Detection', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()