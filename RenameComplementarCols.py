import os
import pandas as pd

caminhos = [
    "HuGaDB_RFOnly/Complementar",
    "HuGaDB_RF_CalibratedAccGyro/Complementar",
    "Single/Kalman/Complementar",
    "Single/LowPass/Complementar"
]

def renomear_colunas_arquivo_xlsx(caminho_arquivo):
    # Carrega o arquivo xlsx em um DataFrame do pandas
    df = pd.read_excel(caminho_arquivo)
    
    # Verifica se as colunas "rfx", "rfy" e "rfz" estão presentes
    if "rfx" in df.columns and "rfy" in df.columns and "rfz" in df.columns:
        # Renomeia as colunas para "rfax", "rfay" e "rfaz"
        df.rename(columns={"rfx": "rfax", "rfy": "rfay", "rfz": "rfaz"}, inplace=True)
        
        # Salva as alterações no arquivo
        df.to_excel(caminho_arquivo, index=False)

# Percorre todos os caminhos especificados
for caminho in caminhos:
    # Obtém a lista de arquivos no caminho
    arquivos = os.listdir(caminho)
    
    # Percorre todos os arquivos no caminho
    for arquivo in arquivos:
        # Verifica se é um arquivo xlsx
        if arquivo.endswith(".xlsx"):
            # Caminho completo do arquivo
            caminho_arquivo = os.path.join(caminho, arquivo)
            
            # Renomeia as colunas no arquivo xlsx
            renomear_colunas_arquivo_xlsx(caminho_arquivo)
