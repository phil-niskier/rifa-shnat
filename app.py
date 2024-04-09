import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

# Exibe uma imagem
def exibir_imagem(path_imagem):
    st.image(path_imagem)

# Exibe titulo de boas vindas
def exibir_titulo(titulo):
    st.title(titulo)

#Carrega os dados do csv pro dataframe
def carregar_dados(caminho_csv):
    dados_csv=pd.read_csv(caminho_csv)
    return dados_csv

# Exibe subtítulo
def exibir_subtitulo(subtitulo, dados):
    total = str(len(dados))
    participantes = total + ' participantes únicos'
    st.subheader(subtitulo + participantes)

# Exibir tabela com participantes e quantidade
def exibir_tabela_nomes_quantidades(dados):
    exibir_subtitulo('Dados do sorteio ', dados)
    st.write(dados[['Nome','Quantidade de Rifas']])
    #se não tiverem as colunas nome e quantidade

# Multiplicar a lista de participantes pela quantidade de rifas que cada um comprou

# Exibir a tabela com a lista multiplicada

# Recebe o arquivo csv através do upload
def receber_arquivo():
    arquivo = st.file_uploader('Insira um arquivo csv com os nomes e a quantidade de rifas de cada participante')
    if arquivo is not None:
        dados=carregar_dados(arquivo)
        exibir_tabela_nomes_quantidades(dados)
    else:
        st.info('Voce precisa carregar uma planilha')

    #se não tiverem as colunas nome e quantidade

# Exibir um botato para sortear um vencedor

# Ao botao clicado sortear de fato uma pessoa da lista dupçlicada 

# Exibir o vencedor abaixo do botao com fonte grande e verde 

# Exibir uma imagem abaixo do nome 

# Tocar um som de fundo de vitoria

#CHAMAR AS FUNÇÕES
exibir_imagem('chazi.png')
exibir_titulo('Bem vindos ao Super, Hiper, Ultra, Mega, TCHAPTCHURA!!! Sorteador de rifas do Shnat 25')
receber_arquivo()