import cv2

def flip_image(image, direction):
    if direction == "Horizontal":
        flipped = cv2.flip(
            image,
            1
        )
    elif direction == "Vertical":
        flipped = cv2.flip(
            image,
            0
        )
    elif direction == "Both":
        flipped = cv2.flip(
            image,
            -1
        )
    else:
        flipped = image
    return flipped