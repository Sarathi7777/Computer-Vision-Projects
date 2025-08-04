import cv2
import numpy as np
import time

# Window setup
window_name = "Concentric Circles"
width, height = 600, 600
center = (width // 2, height // 2)
canvas = np.zeros((height, width, 3), dtype=np.uint8)

# Circle parameters
num_circles = 8
max_radius = min(width, height) // 2 - 20
radii = np.linspace(40, max_radius, num_circles, dtype=int)

# Colors for circles (BGR)
colors = [
    (0, 0, 255),    # Red
    (0, 255, 0),    # Green
    (255, 0, 0),    # Blue
    (0, 255, 255),  # Yellow
    (255, 0, 255),  # Magenta
    (255, 255, 0),  # Cyan
    (128, 0, 128),  # Purple
    (0, 128, 255),  # Orange
]

cv2.namedWindow(window_name)

for i in range(num_circles):
    canvas = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.circle(canvas, center, radii[i], colors[i % len(colors)], 3)
    cv2.imshow(window_name, canvas)
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break