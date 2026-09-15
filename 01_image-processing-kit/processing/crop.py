def crop_image(image, x1, y1, x2, y2):
    """
    Crop an image using the given coordinates.
    Parameters:
        image: OpenCV image
        x1: starting x-coordinate
        y1: starting y-coordinate
        x2: ending x-coordinate
        y2: ending y-coordinate
    Returns:
        cropped image
    """
    cropped = image[y1:y2, x1:x2] #image[y-coordinate range, x-coordinate range]
    return cropped