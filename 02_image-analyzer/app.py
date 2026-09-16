import streamlit as st
import cv2
import numpy as np

from analyzer.properties import get_info, get_pixel_value
from analyzer.histogram import generate_histogram

st.set_page_config(
    page_title="Image Analyzer",
    layout="centered"
)
st.title("Image Analyzer")
st.write("Analyze an image as an NumPy Array")
st.header("Upload Image")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=['jpeg','jpg','png']
)

if uploaded_file is not None:
    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype = np.uint8
    )
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(
        image,
        channels="BGR",
        use_container_width=True
    )

    st.subheader("Image Information")
    info = get_info(image)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("width:",f"{info["width"]}px")
        st.metric("height:",f"{info["height"]}px")
    with col2:
        st.metric("channels:",info["channels"])
        st.metric("dimensions:",info["dimensions"])
    with col3:
        st.metric("pixels:",f"{info["pixels"]:,}")
        st.metric("dtype:",info["pixels"])
    st.write(
        "Numpy Array Size: "
        f"{info["size_bytes"]:,} bytes"
    )

    st.metric("Average Pixel Intensity:",f"{image.mean():.2f}")

    height, width = image.shape[:2]
    col1, col2 = st.columns(2)
    with col1:
        x = st.number_input(
            "X coordinate",
            min_value=0,
            max_value=width - 1,
            value=1
        )
    with col2:
        y = st.number_input(
            "Y coordinate",
            min_value=0,
            max_value=height-1,
            value=1
        )

    pixel = get_pixel_value(image, int(x), int(y))
    st.write("BGR pixel value:")
    st.write(pixel)

    st.subheader("Histogram")
    fig = generate_histogram(image)
    st.pyplot(fig)