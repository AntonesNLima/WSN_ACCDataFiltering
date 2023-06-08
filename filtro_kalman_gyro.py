import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import Workbook

# Função para aplicar o filtro de Kalman e salvar os dados filtrados
def aplicar_filtro_kalman(arquivo):
    # Carregar os dados do arquivo .xlsx
    dados = pd.read_excel(arquivo, sheet_name='Sheet1')

    # Extrair as colunas de interesse
    coluna1 = dados['rfgx']
    coluna2 = dados['rfgy']
    coluna3 = dados['rfgz']

    # Definir as matrizes do filtro de Kalman
    F = np.array([[1, 1, 0],
                  [0, 1, 1],
                  [0, 0, 1]])
    H = np.array([[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]])
    Q = np.eye(3) * 0.01  # Covariância do processo
    R = np.eye(3) * 0.1   # Covariância da medição
    x0 = np.array([0, 0, 0])  # Estado inicial
    P0 = np.eye(3) * 1     # Covariância inicial

    # Inicializar os vetores de estado e covariância
    x_est = [x0]
    P_est = [P0]

    # Executar o filtro de Kalman
    for i in range(len(coluna1)):
        # Prever o próximo estado
        x_pred = F.dot(x_est[-1])
        P_pred = F.dot(P_est[-1]).dot(F.T) + Q

        # Calcular a inovação
        y = np.array([coluna1[i], coluna2[i], coluna3[i]])
        innovation = y - H.dot(x_pred)
        S = H.dot(P_pred).dot(H.T) + R

        # Calcular a ganho de Kalman
        K = P_pred.dot(H.T).dot(np.linalg.inv(S))

        # Atualizar o estado estimado e a covariância
        x_est.append(x_pred + K.dot(innovation))
        P_est.append((np.eye(3) - K.dot(H)).dot(P_pred))

    # Extrair as colunas filtradas
    coluna1_filtrada = [x[0] for x in x_est[1:]]
    coluna2_filtrada = [x[1] for x in x_est[1:]]
    coluna3_filtrada = [x[2] for x in x_est[1:]]

    # salvar dados em .xlsx
    df_filtrado = pd.DataFrame({'Coluna 1': coluna1_filtrada, 'Coluna 2': coluna2_filtrada, 'Coluna 3': coluna3_filtrada})
    nome_arquivo = os.path.splitext(os.path.basename(arquivo))[0]
    df_filtrado.to_excel(f'filtrados_kalman/{nome_arquivo}_filtrado_kalman.xlsx', index=False)

# Pasta com os arquivos .xlsx
pasta_dados = 'HugaDB_RFOnly'

# Obter a lista de arquivos .xlsx na pasta
arquivos_xlsx = glob.glob(os.path.join(pasta_dados, '*.xlsx'))

# Iterar sobre os arquivos e aplicar o filtro de Kalman
for arquivo in arquivos_xlsx:
    aplicar_filtro_kalman(arquivo)
