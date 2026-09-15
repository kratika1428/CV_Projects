import streamlit as st
import cv2

from processing.crop import crop_image
from processing.save import image_to_bytes

def crop_ui(opencv_image, image):

    #cropping the image
    st.header("Crop Image")

    col1, col2 = st.columns(2)
    with col1:
        x1 = st.number_input(
            'Start X',
            min_value=0,
            max_value=image.width - 1,
            value=0
        )
        y1 = st.number_input(
            'Start Y',
            min_value=0,
            max_value=image.height - 1,
            value=0
        )
    with col2:
        x2 = st.number_input(
            'End X',
            min_value=1,
            max_value=image.width,
            value=image.width
        )
        y2 = st.number_input(
            'End Y',
            min_value=1,
            max_value=image.height,
            value=image.height
        )

    if x2 <= x1:
        st.error("End X must be greater than Start X")
        return
    if y2 <= y1:
        st.error("End Y must be greater than Start Y")
        return

    #calling cropping function
    cropped_image = crop_image(
        opencv_image,
        int(x1),
        int(y1),
        int(x2),
        int(y2)
    )

    cropped_rgb = cv2.cvtColor(
        cropped_image,
        cv2.COLOR_BGR2RGB
    )

    st.subheader("Cropped Image")
    st.image(
        cropped_rgb,
        caption="Cropped Image",
        use_container_width=True
    )
    #image information
    st.subheader("Cropped Image Information")
    st.write("Width:", cropped_rgb.shape[1])
    st.write("Height:", cropped_rgb.shape[0])

    image_bytes = image_to_bytes(cropped_rgb)
    if image_bytes:
        st.download_button(
            label="⬇️ Download Cropped Image",
            data=image_bytes,
            file_name="cropped_image.png",
            mime="image/png"
        )