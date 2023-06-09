import os
import glob
import pandas as pd
import matplotlib.pyplot as plt


pasta_dados = 'testcalib'
pasta_graficos = 'testcalib'


def plot_xlsx_all(inpath, title, xAxis='rfax', yAxis='rfay', zAxis='rfaz'):

    outpath = inpath+'/plots'
    if not os.path.exists(outpath):
        os.makedirs(outpath)

    # Lista todos os arquivos .xlsx na pasta de dados
    arquivos_xlsx = glob.glob(os.path.join(inpath, '*.xlsx'))
    # Loop pelos arquivos
    for arquivo in arquivos_xlsx:
        # Leitura do arquivo .xlsx
        df = pd.read_excel(arquivo)
    
        # Extração das colunas de interesse
        x = df[xAxis]
        y = df[yAxis]
        z = df[zAxis]
    
        # Plotagem dos gráficos raw
        plt.figure()
        plt.plot(x, label='x-axis')
        plt.plot(y, label='y-axis')
        plt.plot(z, label='z-axis')
        plt.xlabel('Samples')
        plt.ylabel('Range')
        plt.title('Right Foot Accelerometer ({title})')
        plt.legend()
    
        #Obtém o nome do arquivo sem o caminho
        nome_arquivo = os.path.basename(arquivo)
        #Remove a extensão do arquivo
        nome_arquivo = os.path.splitext(nome_arquivo)[0]
        #Caminho completo para salvar o gráfico
        caminho_grafico = os.path.join(outpath, f'{nome_arquivo}.png')
        #Salva o gráfico como imagem
        plt.savefig(caminho_grafico)
        #Fecha a figura para liberar memória
        plt.close()
    
        print(f'Gráfico salvo: {caminho_grafico}')



##Rodando função para todas as pastas
plot_xlsx_all('HuGaDB_RFOnly', 'Dados Inalterados') ##dados Inalterados

plot_xlsx_all('HuGaDB_RF_CalibratedAccGyro', "Dados Normalizados") ##dados Calibrados

plot_xlsx_all('Single/Complementar', 'rfx', 'rfy', 'rfz')
plot_xlsx_all('Single/Kalman')
plot_xlsx_all('Single/Kalman/Complementar', 'rfx', 'rfy', 'rfz')
plot_xlsx_all('Single/LowPass')
plot_xlsx_all('Single/LowPass/Complementar', 'rfx', 'rfy', 'rfz')


