import random
import cv2
import os


async def capture_image() -> str:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return 'Error: Unable to open webcam'

    # Capture a single frame
    ret, frame = cap.read()

    if not ret:
        return 'Error: Unable to capture frame'

    # Generate a random filename
    filename = f'webcam_image_{random.randint(1, 100000)}.jpg'

    # Save the captured frame
    save_dir = '../../media'
    file_path = os.path.normpath(os.path.join(save_dir, filename))

    cv2.imwrite(file_path, frame)
    cap.release()

    return file_path
