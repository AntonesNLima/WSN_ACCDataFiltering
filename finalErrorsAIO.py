import pandas as pd
import numpy as np
import os

def calcular_erros(dados_filtrados, dados_originais):
    erro_medio = abs(dados_filtrados - dados_originais).mean()
    eqm = np.mean((dados_filtrados - dados_originais) ** 2)
    erro_maximo = np.max(np.abs(dados_filtrados - dados_originais))
    return erro_medio, eqm, erro_maximo

# Pasta raiz
pasta_raiz = "final_11_08"

# Pasta com os dados originais
pasta_originais = os.path.join(pasta_raiz)

# Arquivo de dados originais
arquivo_originais = "calibrated.xlsx"

# Pasta para salvar o arquivo de resultados
pasta_analises = os.path.join(pasta_raiz, "Análises")

# Nome do arquivo de resultados
nome_arquivo_resultados = "Resultados_AIO.xlsx"

# DataFrame para armazenar os resultados
df_resultados = pd.DataFrame(columns=["Arquivo", "Erro Médio", "EQM", "Erro Máximo"])

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
        
        # Cálculo dos erros
        erro_medio, eqm, erro_maximo = calcular_erros(dados_filtrados, dados_originais)
        
        # Adicionar resultados ao DataFrame
        df_resultados = df_resultados.append({
            "Arquivo": arquivo[:-5],  # Remover a extensão .xlsx do nome do arquivo
            "Erro Médio": erro_medio,
            "EQM": eqm,
            "Erro Máximo": erro_maximo
        }, ignore_index=True)

# Caminho completo para o arquivo de resultados
caminho_resultados = os.path.join(pasta_analises, nome_arquivo_resultados)

# Salvar o DataFrame com os resultados em um arquivo XLSX
df_resultados.to_excel(caminho_resultados, index=False)

print(f"Arquivo de resultados salvo em: {caminho_resultados}")
