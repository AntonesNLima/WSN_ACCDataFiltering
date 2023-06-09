import os
import pandas as pd

# Função para calibração do giroscópio (compensação de viés)
def calibrate_gyroscope(data):
    bias = data.mean()  # Estimativa do viés
    return data - bias  # Compensação do viés

# Pasta de entrada e saída
pasta_entrada = "HuGaDB_RF_CalibratedAccGyro"
pasta_saida = "HuGaDB_RF_CalibratedAccGyro"

# Criar pasta de saída se não existir
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Lista de arquivos XLSX na pasta de entrada
arquivos = os.listdir(pasta_entrada)

# Loop pelos arquivos XLSX
for arquivo in arquivos:
    # Verificar se o arquivo é XLSX
    if arquivo.endswith(".xlsx"):
        # Ler o arquivo XLSX original
        caminho_entrada = os.path.join(pasta_entrada, arquivo)
        df_original = pd.read_excel(caminho_entrada)
        
        # Calibração dos dados do giroscópio
        df_calibrado = df_original.copy()
        df_calibrado["rfgx"] = calibrate_gyroscope(df_original["rfgx"])
        df_calibrado["rfgy"] = calibrate_gyroscope(df_original["rfgy"])
        df_calibrado["rfgz"] = calibrate_gyroscope(df_original["rfgz"])
        
        # Salvar o arquivo XLSX calibrado na pasta de saída
        caminho_saida = os.path.join(pasta_saida, arquivo)
        df_calibrado.to_excel(caminho_saida, index=False)

        print(f"Arquivo '{arquivo}' calibrado e salvo em '{caminho_saida}'")
