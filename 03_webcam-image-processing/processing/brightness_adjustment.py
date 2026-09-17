import cv2

def brightness_adjustment(frame,brightness):
    adjusted = cv2.convertScaleAbs(
        frame,
        alpha=0.1,
        beta=brightness
    )
    return adjusted