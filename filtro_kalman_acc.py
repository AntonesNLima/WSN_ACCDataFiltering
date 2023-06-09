# esse worka
import os
import glob
import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl import load_workbook

# Função para aplicar o filtro de Kalman e substituir as colunas filtradas nos dados de saída
def aplicar_filtro_kalman(arquivo):
    # Carregar os dados do arquivo .xlsx
    dados = pd.read_excel(arquivo, sheet_name='Sheet1')

    # Extrair as colunas de interesse
    coluna1 = dados['rfax']
    coluna2 = dados['rfay']
    coluna3 = dados['rfaz']

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

    # Substituir as colunas filtradas nos dados de saída
    dados_filtrados = dados.copy()
    dados_filtrados['rfax'] = [x[0] for x in x_est[1:]]
    dados_filtrados['rfay'] = [x[1] for x in x_est[1:]]
    dados_filtrados['rfaz'] = [x[2] for x in x_est[1:]]

    # Obter o caminho para o arquivo de saída
    nome_arquivo = os.path.splitext(os.path.basename(arquivo))[0]
    arquivo_saida = f'Single/Kalman/{nome_arquivo}_kalman.xlsx'

    # Salvar os dados filtrados no arquivo de saída
    with pd.ExcelWriter(arquivo_saida) as writer:
        dados_filtrados.to_excel(writer, sheet_name='Sheet1', index=False)

# Pasta com os arquivos .xlsx
pasta_dados = 'HuGaDB_RF_CalibratedAccGyro'

# Obter a lista de arquivos .xlsx na pasta
arquivos_xlsx = glob.glob(os.path.join(pasta_dados, '*.xlsx'))

# Iterar sobre os arquivos e aplicar o filtro de Kalman
for arquivo in arquivos_xlsx:
    aplicar_filtro_kalman(arquivo)

    print('aplicou')
