import cv2

def resize_image(image, width, height):
    """
    Resize an image using OpenCV.

    Parameters:
        image: OpenCV image in BGR format
        width: target width
        height: target height

    Returns:
        resized image
    """

    resized = cv2.resize(
        image,
        (int(width), int(height)),
        interpolation=cv2.INTER_AREA
    )

    return resized