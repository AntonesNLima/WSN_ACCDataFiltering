import os
import pandas as pd

def transfer_data_to_new_files(columns):
    input_path = "data/nonCorruptedGyro"
    output_path = "HuGaDB_RFOnly"

    # Verificar se o diretório de saída existe, caso contrário, criar
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Obter lista de arquivos .xlsx no diretório de entrada
    files = [file for file in os.listdir(input_path) if file.endswith(".xlsx")]

    # Loop através de cada arquivo
    for file in files:
        # Ler o arquivo .xlsx
        df = pd.read_excel(os.path.join(input_path, file))

        # Renomear as colunas
        df.columns = columns

        # Criar o nome do arquivo de saída
        output_file = os.path.join(output_path, file)

        # Salvar o dataframe atualizado em um novo arquivo .xlsx
        df.to_excel(output_file, index=False)

        print(f"Transferido arquivo {file} para {output_file}")

# Exemplo de uso
columns = [
    "accelerometer_right_foot_x",
    "accelerometer_right_foot_y",
    "accelerometer_right_foot_z",
    "gyroscope_right_foot_x",
    "gyroscope_right_foot_y",
    "gyroscope_right_foot_z"
]

transfer_data_to_new_files(columns)
