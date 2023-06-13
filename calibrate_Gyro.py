import os
import pandas as pd

# Pasta de entrada
pasta_entrada = "HuGaDB_RF_CalibratedAccGyro"

# Pasta de saída
pasta_saida = "HuGaDB_RF_CalibratedAccGyro/gyrov2"

# Verificar se a pasta de saída existe, caso contrário, criá-la
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Listar todos os arquivos .xlsx na pasta de entrada
arquivos_xlsx = [arquivo for arquivo in os.listdir(pasta_entrada) if arquivo.endswith(".xlsx")]

# Loop pelos arquivos .xlsx
for arquivo in arquivos_xlsx:
    # Caminho completo do arquivo de entrada
    caminho_entrada = os.path.join(pasta_entrada, arquivo)
    
    # Ler o arquivo .xlsx usando o Pandas
    df = pd.read_excel(caminho_entrada)
    
    # Normalizar as colunas "rfax", "rfay" e "afaz"
    df["rfgx"] = (df["rfgx"] - df["rfgx"].mean()) / df["rfgx"].std()
    df["rfgy"] = (df["rfgy"] - df["rfgy"].mean()) / df["rfgy"].std()
    df["rfgz"] = (df["rfgz"] - df["rfgz"].mean()) / df["rfgz"].std()
    
    # Nome do arquivo de saída
    nome_arquivo_saida = arquivo.split("new.xlsx")[0] + "CalibratedAccGyro.xlsx"
    
    # Caminho completo do arquivo de saída
    caminho_saida = os.path.join(pasta_saida, nome_arquivo_saida)
    
    # Salvar os dados normalizados em um novo arquivo .xlsx
    df.to_excel(caminho_saida, index=False)

print("Processamento concluído.")
