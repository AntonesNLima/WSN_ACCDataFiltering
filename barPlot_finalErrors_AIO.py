import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo de resultados
caminho_resultados = "final_11_08/Análises/Resultados_AIO.xlsx"
df_resultados = pd.read_excel(caminho_resultados)

# Configurações do gráfico
plt.figure(figsize=(12, 6))
width = 0.2
index = df_resultados.index

# Plotar as barras
plt.bar(index - width, df_resultados["Erro Médio"], width=width, label="Erro Médio", color="#2a9df4")
plt.bar(index, df_resultados["EQM"], width=width, label="EQM", color="#1167b1")
plt.bar(index + width, df_resultados["Erro Máximo"], width=width, label="Erro Máximo", color="#03254c")

# Configurar o eixo x
plt.xticks(index, df_resultados["Arquivo"], rotation=0)

# Adicionar rótulos e título
plt.xlabel("Filtro")
plt.ylabel("Valor")
plt.title("Métricas de Erro")

# Adicionar legenda
plt.legend()

# Salvar o gráfico como imagem
caminho_imagem = "final_11_08/Análises/Gráfico_Barras.png"
plt.savefig(caminho_imagem)

plt.show()
