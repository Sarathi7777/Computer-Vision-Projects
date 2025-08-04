import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break
    mirror_frame = cv2.flip(frame, 1) # Flip the frame horizontally
    cv2.imshow('Webcam Mirror Effect', mirror_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
