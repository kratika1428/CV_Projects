import streamlit as st
import cv2

from processing.grayscale import grayscale_image
from processing.save import image_to_bytes

def grayscale_ui(opencv_image, image):
    st.header("Grayscale Image")
    grayscale = grayscale_image(opencv_image)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(
            image,
            caption="Original Image",
            use_container_width=True
        )
    with col2:
        st.subheader("Grayscale Image")
        st.image(
            grayscale,
            caption="Grayscale Image",
            use_container_width=True,
            clamp=True
        )

    image_bytes = image_to_bytes(grayscale)
    if image_bytes:
        st.download_button(
            label="⬇️ Download Grayscale Image",
            data=image_bytes,
            file_name="grayscale_image.png",
            mime="image/png"
        )