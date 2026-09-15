import streamlit as st
from PIL import Image
import numpy as np
import cv2

from UI.resize_ui import resize_ui
from UI.crop_ui import crop_ui
from UI.rotate_ui import rotate_ui
from UI.flip_ui import flip_ui
from UI.grayscale_ui import grayscale_ui
from UI.adjustments_ui import adjust_contrast_ui, adjust_brightness_ui

st.set_page_config(
    page_title="Image Processing Toolkit",
    layout="wide"
)
st.title("Image Processing Toolkit")
st.write(
    "Upload an image and select an image-processing operation "
    "from the sidebar."
)
st.header("Upload Image")

operations = st.sidebar.radio(
    "Select Operations",
    [
        "Home",
        "Resize Image",
        "Crop Image",
        "Rotate Image",
        "Flip Image",
        "Grayscale Image",
        "Brightness",
        "Contrast"
    ]
)

#creates upload interface
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpeg","jpg","png"]
)

if uploaded_file is not None:

    #uses pillow to read uploaded image
    image = Image.open(uploaded_file)

    #image array information
    image_array = np.array(image)
    st.write("Array shape:", image_array.shape)
    st.write("Data type:", image_array.dtype)

    #convert to BGR color as expected by opencv
    opencv_image = cv2.cvtColor(
        image_array,
        cv2.COLOR_RGB2BGR
    )
    pixel = opencv_image[0,0] #numpy uses image[y,x]
    st.write("Pixel at [0,0]:",pixel)

    if operations == "Home":
        st.subheader("Original Image")
        st.image(
            image,
            caption="Original Image",
            use_container_width=True
        )

        #image information
        st.subheader("Image Information")
        st.write("Format:", image.format)
        st.write("Mode:", image.mode)
        st.write("Width:", image.width)
        st.write("Height:", image.height)

    elif operations == "Resize Image":
        resize_ui(opencv_image, image)

    elif operations == "Crop Image":
        crop_ui(opencv_image, image)

    elif operations == "Rotate Image":
        rotate_ui(opencv_image, image)

    elif operations == "Flip Image":
        flip_ui(opencv_image, image)

    elif operations == "Grayscale Image":
        grayscale_ui(opencv_image, image)

    elif operations == "Brightness":
        adjust_brightness_ui(opencv_image, image)

    elif operations == "Contrast":
        adjust_contrast_ui(opencv_image, image)

    else:
        st.error("Invalid Operation")