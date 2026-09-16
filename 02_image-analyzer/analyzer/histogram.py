import cv2
import matplotlib.pyplot as plt

def generate_histogram(image):
    fig, ax = plt.subplots()
    channels = [
        ("Blue", 0),
        ("Green", 1),
        ("Red", 2)
    ]
    for name, channel in channels:
        histogram = cv2.calcHist(
            [image],
            [channel],
            None,
            [256],
            [0, 256]
        )
        ax.plot(
            histogram,
            label=name
        )
    ax.set_title("Color Histogram")
    ax.set_xlabel("Pixel Intensity")
    ax.set_ylabel("Frequency")
    ax.legend()

    return fig