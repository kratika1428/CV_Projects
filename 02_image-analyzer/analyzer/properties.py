import cv2
import numpy as np

def get_info(image):
    height, width = image.shape[:2]

    if image.ndim == 2:
        channels = 1
    else:
        channels = image.shape[2]

    return {
        "height":height,
        "width":width,
        "channels":channels,
        "dimensions":image.ndim,
        "pixels":height * width,
        "dtype":image.dtype,
        "size_bytes":image.nbytes
    }

def get_pixel_value(image,x,y):
    return image[int(y),int(x)]