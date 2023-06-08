##altera os nomes das colunas
import os
import pandas as pd

def transfer_data():
    source_folder = "NonCorruptedGyro"
    destination_folder = "HuGaDB_RFOnly"
    columns = [
        "accelerometer_right_foot_x",
        "accelerometer_right_foot_y",
        "accelerometer_right_foot_z",
        "gyroscope_right_foot_x",
        "gyroscope_right_foot_y",
        "gyroscope_right_foot_z"
    ]
    new_columns = ["rfax", "rfay", "rfaz", "rfgx", "rfgy", "rfgz"]
    
    # Verificar se a pasta de destino existe, senão, criá-la
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Percorrer todos os arquivos XLSX na pasta de origem
    for filename in os.listdir(source_folder):
        if filename.endswith(".xlsx"):
            file_path = os.path.join(source_folder, filename)
            
            # Ler o arquivo XLSX
            df = pd.read_excel(file_path)
            
            # Renomear as colunas
            df = df.rename(columns=dict(zip(columns, new_columns)))
            
            # Salvar o novo arquivo XLSX na pasta de destino
            new_filename = filename.replace(".xlsx", "_new.xlsx")
            new_file_path = os.path.join(destination_folder, new_filename)
            df.to_excel(new_file_path, index=False)


transfer_data()