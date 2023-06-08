import os
import pandas as pd
import matplotlib.pyplot as plt
import math

# Função para calcular a magnitude
def calcular_magnitude(ax, ay, az):
    return math.sqrt(ax ** 2 + ay ** 2 + az ** 2)

# Criar as pastas de destino, se não existirem
pasta_dados_fundidos = "Dados_fundidos"
pasta_graficos = "graficos_pos_fusao_Gyro"
os.makedirs(pasta_dados_fundidos, exist_ok=True)
os.makedirs(pasta_graficos, exist_ok=True)

# Ler os arquivos .xlsx da pasta "Dados_tratados"
pasta_dados_tratados = "Dados_tratados"
arquivos_xlsx = [arquivo for arquivo in os.listdir(pasta_dados_tratados) if arquivo.endswith(".xlsx")]

for arquivo in arquivos_xlsx:
    # Caminho completo para o arquivo de origem
    caminho_arquivo_origem = os.path.join(pasta_dados_tratados, arquivo)

    # Caminho completo para o arquivo de destino fundido
    nome_arquivo_fundido = f"{arquivo}_Gyro_fundido"
    caminho_arquivo_fundido = os.path.join(pasta_dados_fundidos, nome_arquivo_fundido)

    # Ler o arquivo .xlsx
    df = pd.read_excel(caminho_arquivo_origem)

    # Extrair os valores dos eixos
    valores_x = df['rfax']
    valores_y = df['rfay']
    valores_z = df['rfaz']

    # Calcular a magnitude
    magnitudes = [calcular_magnitude(ax, ay, az) for ax, ay, az in zip(valores_x, valores_y, valores_z)]

    # Adicionar a coluna de magnitudes aos dados originais
    df['Magnitude'] = magnitudes

    # Salvar os dados fundidos em um novo arquivo .xlsx
    df.to_excel(caminho_arquivo_fundido, index=False)

    print(f"Arquivo {arquivo} processado com sucesso.")

print("Processamento concluído.")
