import cv2

def image_to_bytes(image):
    success, buffer = cv2.imencode(".png", image)
    if not success:
        return None
    return buffer.tobytes()