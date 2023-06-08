##Gera aplica filtro passa baixa nos arquivos selecionados;
##Gera imagem do grafico resultante (pasta "gráficos") e novo arquivo xml contendo dados de entrada e dados de saída(pasta "dados_filtrados_passa_baixa")
import os
import pandas as pd
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt


# Criando a pasta para salvar os dados filtrados
if not os.path.exists('dados_filtrados_Passa_Baixa'):
    os.makedirs('dados_filtrados_Passa_Baixa')

# Definindo as frequências de corte
fs = 58.82  # frequência de amostragem 
fc_low = 10 # frequência de corte inferior
fc_high = 29  # frequência de corte superior

# Criando o filtro passa-baixa
order = 4
nyquist_freq = 0.5 * fs
cutoff_freq = fc_low / nyquist_freq
b, a = butter(order, cutoff_freq, btype='low', analog=False)

#Caminhos
sourceDir = 'HugaDB_RFOnly'


# Lendo todos os arquivos da pasta './xlsx'
for filename in os.listdir(sourceDir):
    # Lendo o arquivo xlsx
    df = pd.read_excel(os.path.join(sourceDir, filename),
                       usecols=['rfax', 'rfay', 'rfaz'])

    # Aplicando o filtro passa-baixa nas colunas accelerometer_right_foot_x, accelerometer_right_foot_y e accelerometer_right_foot_z
    df['rfax'] = filtfilt(b, a, df['rfax'])
    df['rfay'] = filtfilt(b, a, df['rfay'])
    df['rfaz'] = filtfilt(b, a, df['rfaz'])

    # Salvando os dados filtrados em um novo arquivo xlsx na pasta 'dados_filtrados'
    output_filename = os.path.join('dados_filtrados_Passa_Baixa', filename[:-5] + '_Passa_Baixa.xlsx')
    df.to_excel(output_filename, index=False)

    

   
 
