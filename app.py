import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Título do aplicativo
st.title("Sistema de Importação de Boletas")

# Carregar a imagem do usuário
file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

# Verificar se uma imagem foi carregada
if file is not None:
    # Ler a imagem com o PIL
    image = Image.open(file)

    # Converter a imagem para um array do OpenCV
    image_np = np.array(image)

    # Exibir a imagem no Streamlit
    st.image(image, caption='Imagem carregada', use_column_width=True)

    # Se quiser processar a imagem com o OpenCV, pode aplicar algumas operações
    # Exemplo: Converter para escala de cinza
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

    # Exibir a imagem processada em escala de cinza
    st.image(gray_image, caption='Imagem em Escala de Cinza', use_column_width=True)
