import os
import pandas as pd
from scipy.signal import butter, filtfilt

# Definindo as frequências de corte
fs = 58.82  # frequência de amostragem
fc_low = 10  # frequência de corte inferior

# Criando o filtro passa-baixa
order = 4
nyquist_freq = 0.5 * fs
cutoff_freq = fc_low / nyquist_freq
b, a = butter(order, cutoff_freq, btype='low', analog=False)

# Caminhos de entrada e saída
input_path = 'agoravai'
output_path = 'agoravai'

# Lendo todos os arquivos do caminho de entrada
for filename in os.listdir(input_path):
    if filename.endswith(".xlsx"):
        # Lendo o arquivo xlsx
        file_path = os.path.join(input_path, filename)
        df = pd.read_excel(file_path)

        # Aplicando o filtro passa-baixa nas colunas rfax, rfay e rfaz
        df_filtered = df.copy()
        df_filtered['rfax'] = filtfilt(b, a, df['rfax'])
        df_filtered['rfay'] = filtfilt(b, a, df['rfay'])
        df_filtered['rfaz'] = filtfilt(b, a, df['rfaz'])

        # Salvando os dados filtrados em um novo arquivo xlsx no caminho de saída
        output_filename = os.path.join(output_path, filename[:-5] + '_lowPass.xlsx')
        df.update(df_filtered)
        df.to_excel(output_filename, index=False)
