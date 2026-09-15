import streamlit as st
import cv2

from processing.adjustments import adjust_brightness, adjust_contrast
from processing.save import image_to_bytes

def adjust_brightness_ui(opencv_image, image):
    st.header("Brightness Adjustment")
    brightness = st.slider(
        "Brightness",
        min_value=-100,
        max_value=100,
        value=0
    )
    brightness_image = adjust_brightness(
        opencv_image,
        brightness
    )
    adjusted_rgb = cv2.cvtColor(
        brightness_image,
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
        st.subheader("Brightness Adjusted Image")
        st.image(
            adjusted_rgb,
            caption="Brightness Adjusted",
            use_container_width=True
        )

    image_bytes = image_to_bytes(adjusted_rgb)
    if image_bytes:
        st.download_button(
            label="⬇️ Download Brighted Image",
            data=image_bytes,
            file_name="brighted_image.png",
            mime="image/png"
        )

def adjust_contrast_ui(opencv_image, image):
    st.header("Contrast Adjustment")
    contrast = st.slider(
        "Contrast",
        min_value=0.5,
        max_value=3.0,
        value=1.0,
        step=0.1
    )
    contrast_image = adjust_contrast(
        opencv_image,
        contrast
    )
    adjusted_rgb = cv2.cvtColor(
        contrast_image,
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
        st.subheader("Contrast Adjusted Image")
        st.image(
            adjusted_rgb,
            caption="Contrast Adjusted",
            use_container_width=True
        )

    image_bytes = image_to_bytes(adjusted_rgb)
    if image_bytes:
        st.download_button(
            label="⬇️ Download Contrasted Image",
            data=image_bytes,
            file_name="contrast_image.png",
            mime="image/png"
        )