import pandas as pd
import PyPDF2
import zipfile
import os
import re

# Definir o caminho do arquivo PDF
pdf_path = "/mnt/data/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csv_path = "Rol_Procedimentos.csv"
zip_path = "Teste_Jonatas.zip"

# Dicionário para substituir abreviações
descricao_abreviacoes = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial",
    "HCO": "Seg. Hospitalar Com Obstetrícia",
    "HSO": "Seg. Hospitalar Sem Obstetrícia",
    "REF": "Plano Referência",
    "PAC": "Procedimento de Alta Complexidade",
    "DUT": "Diretriz de Utilização"
}

# Função para extrair texto do PDF
def extrair_texto(pdf_path):
    texto = ""
    with open(pdf_path, "rb") as pdf_file:
        leitor = PyPDF2.PdfReader(pdf_file)
        for pagina in leitor.pages:
            texto += pagina.extract_text() + "\n"
    return texto

# Função para processar os dados extraídos
def processar_dados(texto):
    linhas = texto.split("\n")
    dados = []
    for linha in linhas:
        if re.match(r"^\S+", linha):  # Filtra linhas com conteúdo
            dados.append(linha.split())
    return dados

# Extrair texto e processar os dados
texto_extraido = extrair_texto(pdf_path)
dados_tabela = processar_dados(texto_extraido)

# Criar DataFrame
df = pd.DataFrame(dados_tabela)

# Substituir as abreviações
df.replace(descricao_abreviacoes, inplace=True)

# Salvar como CSV
df.to_csv(csv_path, index=False, sep=";")

# Compactar em ZIP
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_path)

# Remover o arquivo CSV após compactação
os.remove(csv_path)

print(f"Arquivo compactado criado: {zip_path}")
