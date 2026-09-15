import cv2

def rotate_image(image, angle):
    if angle == 90:
        rotated = cv2.rotate(
            image,
            cv2.ROTATE_90_CLOCKWISE
        )
    elif angle == 180:
        rotated = cv2.rotate(
            image,
            cv2.ROTATE_180
        )
    elif angle == 270:
        rotated = cv2.rotate(
            image,
            cv2.ROTATE_90_COUNTERCLOCKWISE
        )
    else:
        rotated = image
    return rotated