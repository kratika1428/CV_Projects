import streamlit as st
import cv2
from datetime import datetime

from processing.grayscale import convert_to_grayscale
from processing.blur import convert_to_blurmode
from processing.edge_detection import detect_edges
from processing.brightness_adjustment import brightness_adjustment

st.set_page_config(
    page_title="Webcam Image Processing",
    layout="centered"
)

#operations sidebar panel
mode = st.sidebar.radio(
    "Processing Mode",
    [
        "Original Mode",
        "Grayscale Mode",
        "Blur Mode",
        "Edge Detection",
        "Brightness Adjustment"
    ]
)

st.title("Webcam Image Processing App")
st.write("A Real time Computer Vision Application")

#camera and capture session state
if "camera_on" not in st.session_state:
    st.session_state.camera_on = False
if "capture" not in st.session_state:
    st.session_state.capture = False

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Start Camera"):
        st.session_state.camera_on = True
with col2:
    if st.button("Stop Camera"):
        st.session_state.camera_on = False
with col3:
    if st.button("Capture Screenshot"):
        st.session_state.capture = True

#blur intensity slider
if mode == "Blur Mode":
    kernel_size = st.sidebar.slider(
        "Blur Intensity",
        min_value = 3,
        max_value = 30,
        value = 15,
        step = 2
    )

#edge threshold slider
if mode == "Edge Detection":
    lower_threshold = st.sidebar.slider(
        "Select lower threshold",
        min_value=0,
        max_value=255,
        value=100
    )
    upper_threshold = st.sidebar.slider(
        "Select upper threshold",
        min_value=0,
        max_value=255,
        value=200
    )

#brightness slider
brightness = 0
if mode == "Brightness Adjustment":
    brightness = st.sidebar.slider(
        "Brightness",
        min_value=-100,
        max_value=100,
        value=0,
        step=1
    )

frame_holder = st.empty()
if st.session_state.camera_on:
    cap = cv2.VideoCapture(0)
    while st.session_state.camera_on:
        ret, frame = cap.read()
        if not ret:
            st.error("Could not access webcam")
            break
        processed_frame = frame.copy()
        if mode == "Original Mode":
            pass

        elif mode == "Grayscale Mode":
            processed_frame = convert_to_grayscale(processed_frame)

        elif mode == "Blur Mode":
            processed_frame = convert_to_blurmode(processed_frame, kernel_size)

        elif mode == "Edge Detection":
            if lower_threshold < upper_threshold:
                processed_frame = detect_edges(processed_frame,lower_threshold,upper_threshold)

        elif mode == "Brightness Adjustment":
            processed_frame = brightness_adjustment(processed_frame, brightness)

        if st.session_state.capture:
            filename = datetime.now().strftime(
                "screenshot_%Y%m%d_%H%M%S.jpg"
            )
            filepath = f"screenshots/{filename}"
            cv2.imwrite(filepath, processed_frame)
            st.success(f"Screenshot Saved {filename}")
            st.session_state.capture = False

        display_frame = cv2.cvtColor(
            processed_frame,
            cv2.COLOR_BGR2RGB
        )
        frame_holder.image(
            display_frame,
            channels="RGB"
        )
    cap.release()
else:
    st.info("Click 'Start Camera' to begin")