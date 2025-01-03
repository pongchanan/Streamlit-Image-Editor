import streamlit as st
# PIl is for python image library
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align: center;'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown('---')

image = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])
info = st.empty()
size = st.empty()
mode = st.empty()
format_ = st.empty()

if image:
    img = Image.open(image)
    info.markdown("<h2 style='text-align: center;'>Information</h2>", unsafe_allow_html=True)
    size.markdown(f"<h6>Size: {img.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {img.mode}</h6>", unsafe_allow_html=True)
    format_.markdown(f"<h6>Format: {img.format}</h6>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center;'>Resizing</h2>", unsafe_allow_html=True)
    st.markdown('---')
    width = st.number_input("Width", value=img.width)
    height = st.number_input("Height", value=img.height)
    
    st.markdown("<h2 style='text-align: center;'>Rotation</h2>", unsafe_allow_html=True)
    st.markdown('---')
    degree = st.number_input("Degree")
    
    st.markdown("<h2 style='text-align: center;'>Filter</h2>", unsafe_allow_html=True)
    st.markdown('---')
    filter_ = st.selectbox("Filters", options=("None", "Blur", "Detail", "Emboss", "Smooth"))
    
    s_btn = st.button("Submit")
    if s_btn:
        edited = img.resize((width, height)).rotate(degree)
        filtered = edited
        if filter_ != "None":
            if filter_ == "Blur":
                filtered = edited.filter(BLUR)
            elif filter_ == "Detail":
                filtered =edited.filter(DETAIL)
            elif filter_ == "Emboss":
                filtered = edited.filter(EMBOSS)
            elif filter_ == "Smooth":
                filtered = edited.filter(SMOOTH)
        st.image(filtered)