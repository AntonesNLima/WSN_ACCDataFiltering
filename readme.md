# Etapas para Reprodução do Experimento

Esta versão do repositório conta com os scripts e arquivos de dados referentes ao testes finais apresentados no trabalho.
Algumas das etapas de pré-processamento e scripts de processamento em massa do dataset não estão inclusos.
Os testes apresentados foram realizados a partir de um único arquivo de dados original e todos ou filtros e plotagens foram aplicados em suas variações. O arquivo em questão é o "HuGaDB_v2_various_11_08.xlsx" presente na pasta "original_11_08".

**Observação**: Os inputs e outputs dos arquivos podem estar diferentes nos scripts. Caso o erro "No such file or directory:..." surja durante as execuções, por favor, conferir os caminhos pretendidos.

## 1. Pré-Processamento
1. Executar script walkingOnly.py no diretório "original_11_08": Essa etapa extrai apenas as informações referentes à atividade "walking" e elimina as demais. O output desta etapa é o arquivo "RF_walkingOnly.xlsx" na pasta "final_11_08".
2. Executar script "calibrate_Acc.py" no arquivo "RF_walkingOnly". Em seguida executar o script "calibrate_Gyro.py" no arquivo resultante. A saída será o equivalente ao arquivo "calibrated.xlsx" na pasta "Final_11_08".
   
## 2. Aplicação dos Filtros
1. **Filtro de Kalman**: Executar o script "filtro_kalman_acc.py" no arquivo "calibrated.xlsx"; Executar o script "filtro_kalman_gyro.py" no arquivo resultante. O output deve ser o equivalente ao "calibrated_kalman.xlsx".
2. **Filtro Passa-Baixa**: Executar o script "filtro_lowpass_acc.py" no arquivo "calibrated.xlsx"; Executar o script "filtro_lowpass_gyro.py" no arquivo resultante. O output deve ser o equivalente ao "calibrated_lowpass.xlsx".
3. **Filtro Complementar**: Executar o script "filtro_complementar.py" no arquivo "calibrated.xlsx" e nos arquivos de saída das duas etapas anteriores. Os outputs serão, respectivamente, equivalentes aos arquivos "calibrated_complementar.xlsx", "calibrated_kalman_complementar.xlsx" e "calibrated_lowpass_complementar.xlsx".
   
## 3. Calculo dos Índices de Erro
1. Executar o script "finalErrorsAIO.py", referenciando simultaneamente o arquivo "calibrated.xlsx" e os 5 arquivos de dados resultantes da seção anterior. Esta etapa gera um único arquivo contendo os três indices de erro das 5 filtragens. O output será equivalente ao arquivo "Resultados_AIO.xlsx" no caminho "final_11_08/Análises/".
2. **opcional**: Caso deseje-se gerar os erros separadamente, pode-se utilizar os scripts "finalErroMedio.py", "finalEQM.py" e "finalErroMaximo.py".
   
## Plotagem
1. Executar o script "comparisonPlot_singleplot.py" gera um único  gráfico de linha utilizando dados de arquivos diferentes. Os arquivos a serem inclusos em cada plotagem podem ser especificados alterando-se o conteúdo da variável  "nomes_arquivos =['arquivo_1', 'arquivo_2, ... arquivo_N]". O script está previamente configurado para plotar apenas a coluna "rfax" dos arquivos.
2. O script "comparisonPlot_multiplots.py" gera gráficos de linha da coluna "rfax" para todos os arquivos xlsx dentro do diretório especificado na variável "pasta_dados".
3. O script "barPlot_finalErrors_AIO.py" gera os gráficos de barras do arquivo "Resultados_AIO.xlsx" resultante da etapa 1 da seção 3.
