import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import re

# Instanciar o leitor
reader = easyocr.Reader(['pt'])  # Use o idioma desejado

# Título do aplicativo
st.title("Sistema de Captura de Valores de Boletas")

# Carregar a imagem do usuário
file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

if file is not None:
    # Ler a imagem com o PIL
    image = Image.open(file)
    image_np = np.array(image)  # Converter para NumPy array

    # Exibir a imagem carregada
    st.image(image, caption='Imagem carregada', use_column_width=True)

    # Aplicar OCR
    results = reader.readtext(image_np)

    # Extrair e exibir texto
    texto_extraido = ' '.join([result[1] for result in results])
    st.text_area("Texto Extraído", texto_extraido, height=300)

    # Regex para capturar valores após 'R$' com possíveis variações
    regex_valor = r'(?:R\s*\$|RS\s*|\sR\s*)\s*([\d,.]+)'
    valores = re.findall(regex_valor, texto_extraido, re.IGNORECASE)
    
    # Exibir os valores capturados
    st.write("Valores capturados:", valores)

    # Converter os valores para floats e somar
    valores_float = []
    for valor in valores:
        # Remove caracteres indesejados e substitui ',' por '.'
        valor_limpo = re.sub(r'[^\d,]', '', valor).replace(',', '.')
        try:
            valor_float = float(valor_limpo)
            valores_float.append(valor_float)
        except ValueError:
            st.warning(f"Não foi possível converter o valor '{valor}' para float.")

    # Exibir os valores capturados
    st.write("Valores capturados:", valores_float)

    # Calcular a soma total
    soma_total = sum(valores_float)
    
    # Exibir soma total
    st.write(f"SOMA TOTAL DOS VALORES: R$ {soma_total:.2f}")
