import os

def reduzir_nomes_xlsx(caminhos, n):
    for caminho in caminhos:
        caminho_completo = os.path.abspath(caminho)
        if os.path.isdir(caminho_completo):
            for arquivo in os.listdir(caminho_completo):
                if arquivo.endswith(".xlsx"):
                    nome_arquivo, extensao = os.path.splitext(arquivo)
                    novo_nome = nome_arquivo[:n] + extensao
                    antigo_caminho = os.path.join(caminho_completo, arquivo)
                    novo_caminho = os.path.join(caminho_completo, novo_nome)
                    os.rename(antigo_caminho, novo_caminho)

# Exemplo de uso:
caminhos = [
    "HuGaDB_RFOnly",
    "HuGaDB_RFOnly/Complementar",
    "HuGaDB_RF_CalibratedAccGyro",
    "HuGaDB_RF_CalibratedAccGyro/Complementar",
    "Single/Kalman",
    "Single/Kalman/Complementar",
    "Single/LowPass",
    "Single/LowPass/Complementar"
]
caracteres = 23
reduzir_nomes_xlsx(caminhos, caracteres)


