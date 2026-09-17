import cv2

def convert_to_blurmode(frame, kernel_size=15):
    blur = cv2.GaussianBlur(
        frame,
        (kernel_size,kernel_size),
        0
    )
    return blur