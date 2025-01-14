import re

# Exemplo de texto extraído
texto_extraido = """
R$ 127,00 débito mastercard
R$ 50,00 crédito mastercard
R$ 100,00 débito mastercard
R$ 900,00 crédito visa
"""

# Regex para capturar valor, método e bandeira
padrao = r"R\$\s*(\d+,\d{2})\s*(débito|crédito)\s*(mastercard|visa)"

resultados = re.findall(padrao, texto_extraido, re.IGNORECASE)

# Agrupando os valores por método e bandeira
pagamentos = {}
for valor, metodo, bandeira in resultados:
    chave = (metodo.lower(), bandeira.lower())
    if chave not in pagamentos:
        pagamentos[chave] = 0.0
    # Convertendo o valor para float
    pagamentos[chave] += float(valor.replace(',', '.'))

# Exibir os resultados
for (metodo, bandeira), total in pagamentos.items():
    print(f"{metodo.upper()} {bandeira.upper()} TOTAL: R$ {total:.2f}")

# Soma total
soma_total = sum(pagamentos.values())
print(f"SOMA TOTAL DOS CARTÕES: R$ {soma_total:.2f}")
