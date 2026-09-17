import cv2

def detect_edges(frame, lower_threshold=100, upper_threshold=200):
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )
    edges = cv2.Canny(
        gray,
        lower_threshold,
        upper_threshold
    )
    return edges