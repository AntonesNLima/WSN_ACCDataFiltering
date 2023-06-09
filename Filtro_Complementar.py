import os
import pandas as pd

def complementar_filter(accelerometer_data, gyroscope_data, alpha=0.98):
    fused_data = pd.DataFrame()
    
    # Aplicar o filtro complementar para cada eixo
    for axis in ['x', 'y', 'z']:
        accel_axis = 'rfa' + axis
        gyro_axis = 'rfg' + axis
        
        # Obter as séries de dados para o eixo atual
        accel_series = accelerometer_data[accel_axis]
        gyro_series = gyroscope_data[gyro_axis]
        
        # Inicializar a lista de dados filtrados para o eixo atual
        filtered_data = []
        
        # Aplicar o filtro complementar
        for accel_val, gyro_val in zip(accel_series, gyro_series):
            fused_val = alpha * gyro_val + (1 - alpha) * accel_val
            filtered_data.append(fused_val)
        
        # Adicionar os dados filtrados ao DataFrame resultante
        fused_data['rf' + axis] = pd.Series(filtered_data)
    
    return fused_data

# Caminho da pasta que contém os arquivos XLSX
folder_path = "HuGaDB_RF_CalibratedAccGyro"

# Caminho da pasta onde serão salvos os arquivos resultantes
output_folder = folder_path + "/Complementar"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lista para armazenar os nomes dos arquivos processados
processed_files = []

# Percorrer todos os arquivos na pasta
for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(folder_path, filename)
        
        # Ler os dados do acelerômetro e giroscópio do arquivo XLSX
        data = pd.read_excel(file_path)
        accelerometer_data = data[['rfax', 'rfay', 'rfaz']]
        gyroscope_data = data[['rfgx', 'rfgy', 'rfgz']]
        
        # Aplicar o filtro complementar aos dados
        fused_data = complementar_filter(accelerometer_data, gyroscope_data)
        
        # Criar o nome do arquivo de saída
        output_filename =  filename[:-5] + "_complementar.xlsx"
        output_path = os.path.join(output_folder, output_filename)
        
        # Salvar os dados filtrados em um novo arquivo XLSX
        fused_data.to_excel(output_path, index=False)
        
        processed_files.append(output_filename)

# Imprimir os arquivos processados
print("Arquivos processados:")
for filename in processed_files:
    print(filename)
