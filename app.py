import streamlit as st
from PIL import Image
import cv2
import numpy as np


st.title("Sistema soma-nota")


uploaded_file = st.file_uploader("Carregue a imagem da nota fiscal", type=["png", "jpg", "jpeg", "bmp", "tiff"])

if uploaded_file is not None:
    # Mostrar a imagem carregada
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagem Carregada', use_container_width=True)

    if st.button("Processar Imagem"):
        with st.spinner('Processando...'):

            img_cv = np.array(image)
            img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR) 

            # 1. Pré-processamento (Exemplo: escala de cinza) - Refinar depois!
            gray_image = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
            processed_image = gray_image # Começar simples


            st.image(img_cv, caption='Imagem Processada', use_container_width=True)
