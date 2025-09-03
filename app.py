# import streamlit as st
# from PIL import Image
# import cv2
# import pytesseract
# import numpy as np


# st.title("Sistema soma-nota")


# uploaded_file = st.file_uploader("Carregue a imagem da nota fiscal", type=["png", "jpg", "jpeg", "bmp", "tiff"])

# if uploaded_file is not None:

#     image = Image.open(uploaded_file)
#     st.image(image, caption='Imagem Carregada', use_container_width=True)

#     if st.button("Processar Imagem"):
#             img_cv = np.array(image.convert('RGB'))
#             img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

#             gray_image = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
#             processed_image = cv2.adaptiveThreshold(
#                 gray_image,
#                 255, # Valor máximo que um pixel pode ter (branco)
#                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                 cv2.THRESH_BINARY,
#                 13, # Tamanho do bloco (experimente 11, 13, 15...)
#                 9  # Constante C (experimente valores entre 2 e 10)
#             )
#             st.image(processed_image, caption='2. Imagem após Thresholding Adaptativo', use_container_width=True)

#             extracted_text = pytesseract.image_to_string(processed_image, lang='por', config='--psm 6')
#             st.subheader("Texto Extraído:")
#             st.text(extracted_text if extracted_text else "Nenhum texto detectado.")

#             #TODO NO TEXTO EXTRAIDO NÃO É ACHADO O VALOR DA PRIMEIRA BOLETA
#             #TODO PRECISA DE REFINAMENTO COM O OPENCV PARA SABER SE O TESSERACT MELHORA A PRECISÃO


texto_mock = """
Getnet                            Via Cliente         VISA
05/09/24 20:55:27                   **** 6928
BOTECO DO MANOLO CHOPERIA LTDA
CNPJ: 05.966.310/0001-63
AUT:798280                           TBRM:139V394T

CREDITO                             R$ 122,75

EM CASO DE DUVIDAS, ENTRE EM CONTATO COM A CENTRAL
----------------------------------------------------
Getnet          Via Cliente                 PIX
                05/09/24 20:37:32           TBRM:13953864

ID/TRANSACAO
010010000000002961239544R000
VALOR                               R$ 19,30

DADOS DO ESTABELECIMENTO
INSTITUICAO: Banco Santander (Brasil) S.A.
NOME: BOTECO DO MANOLO CHOPERIA LTDA

----------------------------------------------------
Getnet      Via Cliente             PIX
            05/09/24 21:30:51       TBRM: 13953983

ID/TRANSACAO
0100100000000029612395488604
VALOR                           R$ 36,72
CPF/CNPJ: 05.966.310/0001-63

----------------------------------------------------
Getnet         Via Cliente              MASTERCARD
               05/09/24 19:56:58        **** 9460
BOTECO DO MANOLO CHOPERIA LTDA
RIO DE JANEIRO - RJ
AUT: 984465                        TBRM:13549281

DEBITO                          R$ 238,11

COMPROVANTE DE PAGAMENTO VIA CARTAO
----------------------------------------------------

Getnet      Via Cliente         MASTERCARD
            05/09/24 21:36:56   **** 6028
BOTECO DO MANOLO CHOPERIA LTDA
RIO DE JANEIRO - RJ
AUT: 984465                     TBRM:13549292

DEBITO                          R$ 27,88

"""

print(texto_mock)
print(type(texto_mock))