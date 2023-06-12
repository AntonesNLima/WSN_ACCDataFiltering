import pandas as pd
import numpy as np
import os

def calcular_eqm(dados_filtrados, dados_originais):
    eqm = np.mean((dados_filtrados - dados_originais) ** 2)
    return eqm

# Pasta raiz
pasta_raiz = "final_11_08"

# Pasta com os dados originais
pasta_originais = os.path.join(pasta_raiz)

# Arquivo de dados originais
arquivo_originais = "calibrated.xlsx"

# Pasta para salvar o arquivo de resultados
pasta_analises = os.path.join(pasta_raiz, "Análises")

# Nome do arquivo de resultados
nome_arquivo_resultados = "EQM.xlsx"

# DataFrame para armazenar o EQM
df_eqm = pd.DataFrame()

# Caminho completo do arquivo de dados originais
caminho_originais = os.path.join(pasta_originais, arquivo_originais)

# Leitura dos dados originais
dados_originais = pd.read_excel(caminho_originais)["rfax"]

# Leitura dos arquivos XLSX na pasta
arquivos = os.listdir(pasta_originais)
for arquivo in arquivos:
    if arquivo.endswith(".xlsx") and arquivo != arquivo_originais:
        # Caminho completo do arquivo de dados filtrados
        caminho_filtrados = os.path.join(pasta_originais, arquivo)
        
        # Leitura dos dados filtrados
        dados_filtrados = pd.read_excel(caminho_filtrados)["rfax"]
        
        # Cálculo do EQM
        eqm = calcular_eqm(dados_filtrados, dados_originais)
        
        # Nome da coluna de resultado
        nome_coluna_resultado = arquivo[:-5]  # Remover a extensão .xlsx do nome do arquivo
        
        # Adicionar EQM ao DataFrame
        df_eqm[nome_coluna_resultado] = [eqm]

# Caminho completo para o arquivo de resultados
caminho_resultados = os.path.join(pasta_analises, nome_arquivo_resultados)

# Salvar o DataFrame com o EQM em um arquivo XLSX
df_eqm.to_excel(caminho_resultados, index=False)

print(f"Arquivo de resultados salvo em: {caminho_resultados}")
