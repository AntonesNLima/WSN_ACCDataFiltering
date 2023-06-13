import os
import pandas as pd
import matplotlib.pyplot as plt

# Pasta com os arquivos
pasta_dados = "final_11_08"

# Pasta para salvar os gráficos
pasta_graficos = os.path.join(pasta_dados, "gráficos")
os.makedirs(pasta_graficos, exist_ok=True)

# Lista de nomes de arquivos a serem lidos
nomes_arquivos = [
    "calibrated.xlsx",
    #"calibrated_kalman.xlsx",
    #"calibrated_lowPass.xlsx",
    "calibrated_complementar.xlsx",
    "calibrated_kalman_complementar.xlsx",
    "calibrated_lowPass_complementar.xlsx"
    ]

# Criar um DataFrame vazio para armazenar todos os dados
dados_completos = pd.DataFrame()

# Para cada nome de arquivo
for nome_arquivo in nomes_arquivos:
    # Caminho completo do arquivo
    caminho_arquivo = os.path.join(pasta_dados, nome_arquivo)
    
    # Verificar se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        print(f"O arquivo {nome_arquivo} não existe.")
        continue
    
    # Carregar os dados do arquivo
    dados = pd.read_excel(caminho_arquivo)
    
    # Verificar se a coluna 'rfax' existe no arquivo
    if 'rfax' not in dados.columns:
        print(f"A coluna 'rfax' não existe no arquivo {nome_arquivo}.")
        continue
    
    # Adicionar os dados à DataFrame completo
    dados_completos[nome_arquivo] = dados['rfax']

# Plotar o gráfico com todas as colunas
plt.figure(figsize=(10, 6))  # Tamanho do gráfico (opcional)
plt.title("Comparação: Filtros Complementares(Eixo-X)")
plt.xlabel("Índice")
plt.ylabel("Valor")

# Plotar cada coluna no mesmo gráfico
for coluna in dados_completos.columns:
    plt.plot(dados_completos[coluna], label=coluna[:-5])

plt.legend()  # Mostrar legenda com os nomes dos arquivos
plt.tight_layout()  # Ajustar layout para evitar cortes nos rótulos

# Salvar o gráfico na pasta de gráficos
caminho_grafico = os.path.join(pasta_graficos, "Comparação calibrado vs Complementares eixo X.png")
plt.savefig(caminho_grafico)

# Mensagem de conclusão
print("Gráfico salvo com sucesso!")
