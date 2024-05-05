import cv2
cap = cv2.VideoCapture(0)  # First camera
if cap.isOpened():
    print("Camera 0 is available")
else:
    print("Failed to open camera 0")
