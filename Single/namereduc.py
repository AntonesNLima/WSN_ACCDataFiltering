import os

def reduzir_nomes_xlsx(caminho_pasta, n):
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith(".xlsx"):
            nome_arquivo, extensao = os.path.splitext(arquivo)
            novo_nome = nome_arquivo[:n] + extensao
            antigo_caminho = os.path.join(caminho_pasta, arquivo)
            novo_caminho = os.path.join(caminho_pasta, novo_nome)
            os.rename(antigo_caminho, novo_caminho)

# Exemplo de uso:
caminho = "testnamereduc"
caracteres = 23
reduzir_nomes_xlsx(caminho, caracteres)

