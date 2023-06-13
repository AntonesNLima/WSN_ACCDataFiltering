import os
import pandas as pd

# Defina o caminho da pasta "walking" que contém os arquivos .xlsx
caminho_pasta = "original_11_08/"

# Defina o caminho da pasta onde os novos arquivos serão salvos
caminho_pasta_novos = "final_11_08/"

# Obtenha uma lista de todos os arquivos .xlsx na pasta "walking"
arquivos_xlsx = [f for f in os.listdir(caminho_pasta) if f.endswith('.xlsx')]

# Loop através de todos os arquivos .xlsx na pasta "walking"
for arquivo in arquivos_xlsx:

    # Leia o arquivo em um dataframe pandas
    df = pd.read_excel(caminho_pasta + arquivo)

    # Selecione apenas as linhas que contêm o valor "walking" na coluna "activity"
    df_walking = df[df["activity"] == "walking"]

    # Salve as linhas selecionadas em um novo arquivo na pasta "walkingOnly"
    os.makedirs(caminho_pasta_novos, exist_ok=True)
    novo_arquivo = caminho_pasta_novos + "RF_walkingOnly.xlsx"
    df_walking.to_excel(novo_arquivo, index=False)
