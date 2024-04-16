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
#Limpa os dados de 'None', 'teste' ou qtd=0'
def carregar_dados(caminho_csv):
    dados_csv=pd.read_csv(caminho_csv)
    if 'Nome' not in dados_csv.columns or 'Quantidade de Rifas' not in dados_csv.columns:
        st.warning("Erro: DataFrame deve conter as colunas 'Nome' e 'Quantidade de Rifas'.")
        return
        # Remover linhas nulas apenas nas colunas "Nome" e "Quantidade de Rifas"
    dados_csv = dados_csv.dropna(subset=['Nome', 'Quantidade de Rifas'])
    dados_csv = dados_csv[dados_csv['Quantidade de Rifas']>0]
    dados_csv = dados_csv[dados_csv['Nome'] != 'teste']
    dados_csv = dados_csv[dados_csv['Nome'] != 'Teste']
    dados_csv['Nome'] = dados_csv['Nome'].str.title()
    dados_csv = dados_csv.sort_values(by='Quantidade de Rifas', ascending=False)
    for index, row in dados_csv.iterrows():
        st.write(str(row['Quantidade de Rifas']))
        st.write(int(row['Quantidade de Rifas']))
    # Remover espaços em branco da coluna
    dados_csv['Quantidade de Rifas'] = dados_csv['Quantidade de Rifas'].astype(str)
    dados_csv['Quantidade de Rifas'] = dados_csv['Quantidade de Rifas'].str.strip()
    # Converter a coluna para inteiro
    dados_csv['Quantidade de Rifas'] = dados_csv['Quantidade de Rifas'].astype(int)
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
def multiplicar_linhas(dados_a_multiplicar):
        # Criar uma lista para armazenar os novos registros
    novos_registros = []
    # Iterar sobre cada linha do DataFrame
    for index, row in dados_a_multiplicar.iterrows():
        nome = row['Nome']
        quantidade = row['Quantidade de Rifas']
        # Repetir o nome o número de vezes indicado em 'Quantidade de Rifas'
        for _ in range(quantidade):
            novos_registros.append({'Nome': nome})
    
    # Criar um novo DataFrame com os novos registros
    novo_df = pd.DataFrame(novos_registros)
    
    return novo_df

# Exibir a tabela com a lista multiplicada

# Recebe o arquivo csv através do upload
def receber_arquivo():
    arquivo = st.file_uploader('Insira um arquivo csv com os nomes e a quantidade de rifas de cada participante')
    if arquivo is not None:
        dados=carregar_dados(arquivo)
        exibir_tabela_nomes_quantidades(dados)
        dados_mult = multiplicar_linhas(dados)
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