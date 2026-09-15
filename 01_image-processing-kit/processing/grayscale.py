import cv2

def grayscale_image(image):
    grayscale = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )
    return grayscale