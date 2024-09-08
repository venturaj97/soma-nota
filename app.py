import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image
import re

# Título do aplicativo
st.title("Sistema de Captura de Valores de Boletas")

# Carregar a imagem do usuário
file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

if file is not None:
    # Ler a imagem com o PIL
    image = Image.open(file)
    image_np = np.array(image)

    # Exibir a imagem carregada
    st.image(image, caption='Imagem carregada', use_column_width=True)

    # Pré-processamento com OpenCV
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    gray_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
    
    # Equalização do Histograma
    equalized_image = cv2.equalizeHist(gray_image)
    
    # Binarização
    _, binary_image = cv2.threshold(equalized_image, 128, 255, cv2.THRESH_BINARY_INV)
    
    # Dilatação e Erosão (opcional)
    kernel = np.ones((1, 1), np.uint8)
    dilated_image = cv2.dilate(binary_image, kernel, iterations=1)
    eroded_image = cv2.erode(dilated_image, kernel, iterations=1)
    
    # Aplicar Tesseract OCR para extrair o texto
    custom_config = r'--oem 1 --psm 6'
    texto_extraido = pytesseract.image_to_string(eroded_image, lang='por', config=custom_config)

    # Exibir o texto extraído
    st.text_area("Texto Extraído", texto_extraido, height=300)

    # Regex para capturar valores após 'R$' com espaço opcional
    regex_valor = r'R\$\s*([\d,.]+)'
    valores = re.findall(regex_valor, texto_extraido)
    
    # Exibir os valores capturados
    st.write("Valores capturados:", valores)

    # Converter os valores para floats e somar
    valores_float = [float(valor.replace(',', '.')) for valor in valores]
    soma_total = sum(valores_float)
    
    # Exibir soma total
    st.write(f"SOMA TOTAL DOS VALORES: R$ {soma_total:.2f}")
