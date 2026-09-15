import streamlit as st
import cv2

from processing.rotate import rotate_image
from processing.save import image_to_bytes

def rotate_ui(opencv_image, image):
    st.header("Rotate Image")
    angle = st.radio(
        "Select Rotation Angle",
        [
            0,
            90,
            180,
            270
        ],
        horizontal=True
    )
    rotated_image = rotate_image(
        opencv_image,
        angle
    )
    rotated_rgb = cv2.cvtColor(
        rotated_image,
        cv2.COLOR_BGR2RGB
    )
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(
            image,
            caption="Original Image",
            use_container_width=True
        )
    with col2:
        st.subheader("Rotated Image")
        st.image(
            rotated_rgb,
            caption=f"Rotated Image at {angle}",
            use_container_width=True
        )

    image_bytes = image_to_bytes(rotated_rgb)
    if image_bytes:
        st.download_button(
            label="⬇️ Download Rotated Image",
            data=image_bytes,
            file_name="rotated_image.png",
            mime="image/png"
        )