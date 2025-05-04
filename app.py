import streamlit as st
from PIL import Image
import cv2
import pytesseract
import numpy as np


st.title("Sistema soma-nota")


uploaded_file = st.file_uploader("Carregue a imagem da nota fiscal", type=["png", "jpg", "jpeg", "bmp", "tiff"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption='Imagem Carregada', use_container_width=True)

    if st.button("Processar Imagem"):
            img_cv = np.array(image.convert('RGB'))
            img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

            gray_image = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
            processed_image = cv2.adaptiveThreshold(
                gray_image,
                255, # Valor máximo que um pixel pode ter (branco)
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,
                13, # Tamanho do bloco (experimente 11, 13, 15...)
                9  # Constante C (experimente valores entre 2 e 10)
            )
            st.image(processed_image, caption='2. Imagem após Thresholding Adaptativo', use_container_width=True)

            extracted_text = pytesseract.image_to_string(processed_image, lang='por', config='--psm 6')
            st.subheader("Texto Extraído:")
            st.text(extracted_text if extracted_text else "Nenhum texto detectado.")

            #TODO NO TEXTO EXTRAIDO NÃO É ACHADO O VALOR DA PRIMEIRA BOLETA
            #TODO PRECISA DE REFINAMENTO COM O OPENCV PARA SABER SE O TESSERACT MELHORA A PRECISÃO
