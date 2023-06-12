import os
import pandas as pd
import matplotlib.pyplot as plt

# Pasta com os arquivos
pasta_dados = "maisuma"

# Pasta para salvar os gráficos
pasta_graficos = os.path.join(pasta_dados, "gráficos")
os.makedirs(pasta_graficos, exist_ok=True)

# Obter a lista de arquivos na pasta
arquivos = os.listdir(pasta_dados)

# Filtrar apenas arquivos com extensão .xlsx
arquivos_xlsx = [arquivo for arquivo in arquivos if arquivo.endswith(".xlsx")]

# Para cada arquivo .xlsx
for arquivo in arquivos_xlsx:
    # Caminho completo do arquivo
    caminho_arquivo = os.path.join(pasta_dados, arquivo)
    
    # Carregar os dados do arquivo
    dados = pd.read_excel(caminho_arquivo)
    
    # Verificar se a coluna 'rfax' existe no arquivo
    if 'rfax' not in dados.columns:
        print(f"A coluna 'rfax' não existe no arquivo {arquivo}.")
        continue
    
    # Plotar o gráfico
    plt.plot(dados['rfax'])
    plt.title(f"Gráfico de 'rfax' - {arquivo}")
    plt.xlabel("Índice")
    plt.ylabel("Valor 'rfax'")
    
    # Salvar o gráfico na pasta de gráficos
    nome_grafico = f"grafico_{arquivo[:-5]}.png"  # Nome do gráfico baseado no nome do arquivo
    caminho_grafico = os.path.join(pasta_graficos, nome_grafico)
    plt.savefig(caminho_grafico)
    
    # Limpar o gráfico para a próxima iteração
    plt.clf()

# Mensagem de conclusão
print("Gráficos salvos com sucesso!")
