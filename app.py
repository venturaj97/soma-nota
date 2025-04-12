import streamlit as st
from PIL import Image



st.title("Sistema soma-nota")


uploaded_file = st.file_uploader("Carregue a imagem da nota fiscal", type=["png", "jpg", "jpeg", "bmp", "tiff"])

if uploaded_file is not None:
    # Mostrar a imagem carregada
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagem Carregada', use_container_width=True)