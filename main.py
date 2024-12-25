import streamlit as st
# PIl is for python image library
from PIL import Image

st.markdown("<h1 style='text-align: center;'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown('---')

image = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])
size = st.empty()
mode = st.empty()
format_ = st.empty()

if image:
    img = Image.open(image)
    size.markdown(f"<h6>Size: {img.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {img.mode}</h6>", unsafe_allow_html=True)
    format_.markdown(f"<h6>Format: {img.format}</h6>", unsafe_allow_html=True)