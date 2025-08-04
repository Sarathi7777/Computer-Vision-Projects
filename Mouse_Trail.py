import cv2
import numpy as np
import time

# Window setup
window_name = "Mouse Trail"
width, height = 800, 600
canvas = np.zeros((height, width, 3), dtype=np.uint8)

# Store trail points with timestamps
trail_points = []

def draw_trail(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        trail_points.append((x, y, time.time()))

cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, draw_trail)

while True:
    # Fade effect: draw semi-transparent black rectangle
    canvas = cv2.addWeighted(canvas, 0.7, np.zeros_like(canvas), 0.3, 0)
    now = time.time()
    # Draw only points from last 1 second
    trail_points = [(x, y, t) for (x, y, t) in trail_points if now - t < 0.3]
    for x, y, t in trail_points:
        cv2.circle(canvas, (x, y), 5, (0, 255, 0), -1)
    cv2.imshow(window_name, canvas)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        canvas[:] = 0
        trail_points.clear()
    elif key == ord('q'):
        break

cv2.destroyAllWindows()