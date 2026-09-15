import cv2

def adjust_brightness(image, brightness):
    adjusted_image = cv2.convertScaleAbs(
        image,
        alpha=1.0,
        beta=brightness
    )
    return adjusted_image

def adjust_contrast(image, contrast):
    adjusted_image = cv2.convertScaleAbs(
        image,
        alpha=contrast,
        beta=0
    )
    return adjusted_image