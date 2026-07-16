from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("../yolo11n.pt")

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not found")
    exit()

while True:
    ret, frame = camera.read()

    if not ret:
        break

    # Detect objects
    results = model(frame)

    # Draw detections
    annotated_frame = results[0].plot()

    # Display
    cv2.imshow(
        "AI Camera Detection",
        annotated_frame
    )

    # Press ESC to quit
    if cv2.waitKey(1) == 27:
        break


camera.release()
cv2.destroyAllWindows()