import cv2

# Open the default camera (0 = first webcam)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Cannot access camera")
    exit()

while True:
    # Read frame from camera
    success, frame = camera.read()

    if not success:
        print("Failed to capture image")
        break

    # Show camera feed
    cv2.imshow("My Camera", frame)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

# Release camera
camera.release()
cv2.destroyAllWindows()