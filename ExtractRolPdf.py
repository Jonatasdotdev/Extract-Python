import pandas as pd
import tabula
import zipfile
import os
import chardet

# Definir o caminho do arquivo PDF
pdf_path = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
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

# Função para detectar o encoding correto
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
    return result['encoding']

# Detectar o encoding do arquivo
detected_encoding = detect_encoding(pdf_path)
print(f"Encoding detectado: {detected_encoding}")

# Extrair tabelas do PDF
try:
    # Tente extrair com o encoding detectado
    tabelas = tabula.read_pdf(
        pdf_path, 
        pages="all", 
        multiple_tables=True, 
        encoding=detected_encoding
    )
except Exception as e:
    print(f"Erro ao extrair tabelas do PDF: {e}")
    
    # Se falhar, tente sem especificar encoding
    try:
        tabelas = tabula.read_pdf(
            pdf_path, 
            pages="all", 
            multiple_tables=True
        )
    except Exception as e:
        print(f"Erro fatal ao extrair tabelas: {e}")
        exit()

# Combinar todas as tabelas extraídas
df = pd.concat(tabelas, ignore_index=True)

# Substituir abreviações
df.replace(descricao_abreviacoes, inplace=True)

# Salvar como CSV
try:
    df.to_csv(
        csv_path, 
        index=False, 
        sep=";", 
        encoding='utf-8-sig'  
    )
except Exception as e:
    print(f"Erro ao salvar CSV: {e}")
    exit()

# Compactar em ZIP
try:
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, arcname=os.path.basename(csv_path))
except Exception as e:
    print(f"Erro ao criar ZIP: {e}")
    exit()

# Remover o arquivo CSV após compactação
try:
    os.remove(csv_path)
    print(f"Arquivo compactado criado: {zip_path}")
except Exception as e:
    print(f"Erro ao remover CSV: {e}")