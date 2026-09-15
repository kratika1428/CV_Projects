import streamlit as st
from processing.resize import resize_image
import cv2
from processing.save import image_to_bytes

def resize_ui(opencv_image, image):
    #resizing the image
    st.header("Resize Image")
    keep_aspect_ratio = st.checkbox(
        "Maintain Aspect Ratio",
        value=True
    )
    if keep_aspect_ratio:
        new_width = st.number_input(
            "New Width",
            min_value=1,
            value=image.width
        )
        aspect_ratio = image.height / image.width
        new_height = int(new_width * aspect_ratio)
    else:
        new_width = st.number_input(
            "New Width",
            min_value=1,
            value=image.width
        )
        new_height = st.number_input(
            "New Height",
            min_value=1,
            value=image.height
        )

    #calling resize function 
    resized_image = resize_image(
        opencv_image,
        new_width,
        new_height
    )

    #displaying opencv and original image
    resized_rgb = cv2.cvtColor(
        resized_image,
        cv2.COLOR_BGR2RGB
    )

    st.subheader("Resized Image")
    st.image(
        resized_rgb,
        caption="Resized Image",
        use_container_width=True
    )
    #image information
    st.subheader("Resized Image Information")
    st.write("Width:", resized_rgb.shape[1])
    st.write("Height:", resized_rgb.shape[0])

    image_bytes = image_to_bytes(resized_image)
    if image_bytes:
        st.download_button(
            label="⬇️ Download Resized Image",
            data=image_bytes,
            file_name="resized_image.png",
            mime="image/png"
        )