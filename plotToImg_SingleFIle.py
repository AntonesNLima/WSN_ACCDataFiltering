import os
import glob
import pandas as pd
import matplotlib.pyplot as plt


pasta_dados = 'testcalib'
pasta_graficos = 'testcalib'



# Lista todos os arquivos .xlsx na pasta de dados
arquivos_xlsx = glob.glob(os.path.join(pasta_dados, '*.xlsx'))
# Loop pelos arquivos
for arquivo in arquivos_xlsx:
    # Leitura do arquivo .xlsx
    df = pd.read_excel(arquivo)
    
    # Extração das colunas de interesse
    x = df['rfax']
    y = df['rfay']
    z = df['rfaz']
    
    # Plotagem dos gráficos raw
    plt.figure()
    plt.plot(x, label='x-axis')
    plt.plot(y, label='y-axis')
    plt.plot(z, label='z-axis')
    plt.xlabel('Samples')
    plt.ylabel('Range')
    plt.title('Right Foot Accelerometer (kalman-Filter)')
    plt.legend()
    
    #Obtém o nome do arquivo sem o caminho
    nome_arquivo = os.path.basename(arquivo)
    #Remove a extensão do arquivo
    nome_arquivo = os.path.splitext(nome_arquivo)[0]
    #Caminho completo para salvar o gráfico
    caminho_grafico = os.path.join(pasta_graficos, f'{nome_arquivo}.png')
    #Salva o gráfico como imagem
    plt.savefig(caminho_grafico)
    #Fecha a figura para liberar memória
    plt.close()
    
    print(f'Gráfico salvo: {caminho_grafico}')
