import os
import pandas as pd
import matplotlib.pyplot as plt

# Função para aplicar o filtro de média móvel
def aplicar_filtro_media_movel(data, window_size):
    return data.rolling(window=window_size).mean()

# Pasta de entrada dos arquivos .xlsx
pasta_entrada = 'HugaDB_RFOnly'

# Pasta de saída para os arquivos .xlsx filtrados
pasta_saida_xlsx = 'filtrados_media_movel'

# Cria as pastas de saída se elas não existirem
os.makedirs(pasta_saida_xlsx, exist_ok=True)

# Lista todos os arquivos .xlsx na pasta de entrada
arquivos_xlsx = [arquivo for arquivo in os.listdir(pasta_entrada) if arquivo.endswith('.xlsx')]

# Loop para processar cada arquivo
for arquivo in arquivos_xlsx:
    # Carrega o arquivo .xlsx em um DataFrame, selecionando apenas as colunas 'a', 'b' e 'c'
    arquivo_entrada = os.path.join(pasta_entrada, arquivo)
    df = pd.read_excel(arquivo_entrada, usecols=['rfax', 'rfay', 'rfaz'])
    
    # Aplica o filtro de média móvel com janela de tamanho 3
    df_filtrado = aplicar_filtro_media_movel(df, window_size=3)
    
    # Salva o DataFrame filtrado em um novo arquivo .xlsx na pasta de saída
    arquivo_saida_xlsx = os.path.join(pasta_saida_xlsx, f'{os.path.splitext(arquivo)[0]}_filtrado_media_movel.xlsx')
    df_filtrado.to_excel(arquivo_saida_xlsx, index=False)
    
