import streamlit as st
import cv2

from processing.flip import flip_image
from processing.save import image_to_bytes

def flip_ui(opencv_image, image):
    st.header("Flip Image")
    direction = st.radio(
        "Select flip directions",
        [
            "None",
            "Horizontal",
            "Vertical",
            "Both"
        ],
        horizontal=True
    )
    flipped_image = flip_image(opencv_image,direction)
    flipped_rgb = cv2.cvtColor(
        flipped_image,
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
        st.subheader("Flipped Image")
        st.image(
            flipped_rgb,
            caption="Flipped Image",
            use_container_width=True
        )

    image_bytes = image_to_bytes(flipped_rgb)
    if image_bytes:
        st.download_button(
            label="⬇️ Download Flipped Image",
            data=image_bytes,
            file_name="flipped_image.png",
            mime="image/png"
        )