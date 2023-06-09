import pandas as pd
import os

def calcular_erro_medio(dados_filtrados, dados_originais):
    erro_medio = abs(dados_filtrados - dados_originais).mean()
    return erro_medio

# Pasta com os dados originais
pasta_originais = "HuGaDB_RFOnly"

# Pasta com os dados filtrados
pasta_filtrados = "HuGaDB_RFOnly/Complementar"

# Pasta para salvar o arquivo de resultados
pasta_analises = "Análises"

# Nome do arquivo de resultados
nome_arquivo_resultados = "Erro_Medio.xlsx"

# DataFrame para armazenar os erros médios
df_erros_medios = pd.DataFrame()

# Leitura dos arquivos XLSX
arquivos = os.listdir(pasta_originais)
for arquivo in arquivos:
    if arquivo.endswith(".xlsx"):
        # Caminho completo dos arquivos
        caminho_originais = os.path.join(pasta_originais, arquivo)
        caminho_filtrados = os.path.join(pasta_filtrados, arquivo)
        
        # Leitura dos dados originais
        dados_originais = pd.read_excel(caminho_originais)
        
        # Leitura dos dados filtrados
        dados_filtrados = pd.read_excel(caminho_filtrados[:-5]+"_complementar.xlsx")
        
        # Seleção das colunas dos eixos do acelerômetro
        colunas = ["rfax", "rfay", "rfaz"]
        
        # Cálculo do erro médio para cada coluna
        for coluna in colunas:
            erro_medio = calcular_erro_medio(dados_filtrados[coluna[:-2]+coluna[-1:]], dados_originais[coluna])
            nome_coluna_resultado = coluna + "_complementar"
            df_erros_medios.loc[arquivo, nome_coluna_resultado] = erro_medio

# Caminho completo para o arquivo de resultados
caminho_resultados = os.path.join(pasta_analises, nome_arquivo_resultados)

# Salvar o DataFrame com os erros médios em um arquivo XLSX
df_erros_medios.to_excel(caminho_resultados)

print(f"Arquivo de resultados salvo em: {caminho_resultados}")
