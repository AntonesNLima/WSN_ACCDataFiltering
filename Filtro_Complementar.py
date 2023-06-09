import os
import pandas as pd
import numpy as np

# Função para aplicar o filtro complementar aos dados
def aplicar_filtro_complementar(acelerometro, giroscopio, alfa, dt):
    angulo = np.zeros(3)
    velocidade_angular = np.zeros(3)
    angulos_filtrados = []

    for i in range(len(acelerometro)):
        aceleracao = acelerometro[i]
        velocidade_angular += (giroscopio[i] - velocidade_angular) * dt
        angulo += dt * (velocidade_angular + alfa * aceleracao)
        angulos_filtrados.append(angulo)

    return np.array(angulos_filtrados)

# Pasta de origem dos arquivos XLSX
pasta_origem = "caminho/da/pasta"

# Pasta de destino para os arquivos XLSX filtrados
pasta_destino = "caminho/da/pasta/Complementar"

# Parâmetros do filtro complementar
alfa = 0.98
dt = 0.01

# Verifica se a pasta de destino existe, caso contrário, cria-a
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Percorre todos os arquivos XLSX na pasta de origem
for arquivo in os.listdir(pasta_origem):
    if arquivo.endswith(".xlsx"):
        # Caminho completo para o arquivo de origem
        caminho_arquivo = os.path.join(pasta_origem, arquivo)

        # Leitura dos dados do arquivo XLSX
        dados = pd.read_excel(caminho_arquivo)

        # Extrair os dados dos eixos do acelerômetro e do giroscópio
        acelerometro = dados[['rfax', 'rfay', 'rfaz']].values
        giroscopio = dados[['rfgx', 'rfgy', 'rfgz']].values

        # Aplicar o filtro complementar aos dados
        angulos_filtrados = aplicar_filtro_complementar(acelerometro, giroscopio, alfa, dt)

        # Criar um DataFrame com os ângulos filtrados
        df_filtrado = pd.DataFrame(angulos_filtrados, columns=['AnguloX', 'AnguloY', 'AnguloZ'])

        # Criar o nome do arquivo de destino
        nome_arquivo_destino = os.path.splitext(arquivo)[0] + "_filtrado.xlsx"
        caminho_arquivo_destino = os.path.join(pasta_destino, nome_arquivo_destino)

        # Salvar o DataFrame filtrado em um novo arquivo XLSX
        df_filtrado.to_excel(caminho_arquivo_destino, index=False)

        print(f"Arquivo {arquivo} processado e salvo como {nome_arquivo_destino}.")

print("Processamento concluído.")
