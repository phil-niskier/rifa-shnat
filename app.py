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
    # Convertendo a coluna 'Quantidade de Rifas' para int
    dados_csv['Quantidade de Rifas'] = dados_csv['Quantidade de Rifas'].str.split(',').str[0].astype(int)
    dados_csv = dados_csv[dados_csv['Quantidade de Rifas']>0]
    dados_csv = dados_csv[dados_csv['Nome'] != 'teste']
    dados_csv = dados_csv[dados_csv['Nome'] != 'Teste']
    dados_csv['Nome'] = dados_csv['Nome'].str.title()
    dados_csv = dados_csv.sort_values(by=['Quantidade de Rifas', 'Nome'], ascending=[False, True])
    return dados_csv

# Exibe subtítulo
def exibir_subtitulo_unicos(subtitulo, dados):
    total = str(len(dados))
    participantes = total + ' participantes únicos'
    st.subheader(subtitulo + participantes)

# Exibe subtítulo
def exibir_subtitulo_duplicados(subtitulo, dados_duplicados):
    total = str(len(dados_duplicados))
    duplicados = total + ' rifas vendidas'
    st.subheader(subtitulo + duplicados)

# Exibir tabela com participantes e quantidade
def exibir_tabela_nomes_quantidades(dados):
    exibir_subtitulo_unicos('Dados do sorteio ', dados)
    st.write(dados[['Nome','Quantidade de Rifas']])
    #se não tiverem as colunas nome e quantidade

# Multiplicar a lista de participantes pela quantidade de rifas que cada um comprou
def multiplicar_linhas(dados):
        # Criar uma lista para armazenar os novos registros
    novos_registros = []
    # Iterar sobre cada linha do DataFrame
    for index, row in dados.iterrows():
        nome = row['Nome']
        quantidade = row['Quantidade de Rifas']
        # Repetir o nome o número de vezes indicado em 'Quantidade de Rifas'
        for _ in range(quantidade):
            novos_registros.append({'Nome': nome})
    
    # Criar um novo DataFrame com os novos registros
    dados_duplicados = pd.DataFrame(novos_registros)
    dados_duplicados = dados_duplicados.sort_values(by='Nome', ascending=True)
    dados_duplicados = dados_duplicados.iloc[dados_duplicados['Nome'].str.normalize('NFKD').argsort()]
    return dados_duplicados

# Exibir a tabela com a lista multiplicada
def exibir_tabela_nomes_duplicados(dados_duplicados):
    exibir_subtitulo_duplicados('', dados_duplicados)
    st.write(dados_duplicados['Nome'])
    #se não tiverem as colunas nome e quantidade

# Sortear um vencedor
def sortear_vencedor(dados_duplicados):
    if st.button('Sortear Vencedor'):
        lista_nomes = dados_duplicados['Nome'].tolist()
        vencedor = random.choice(lista_nomes)
        return vencedor

# Exibe um vencedor
def exibir_vencedor(vencedor):
    if vencedor is not None:
        st.success(vencedor)

# Recebe o arquivo csv através do upload
def receber_arquivo():
    arquivo = st.file_uploader('Insira um arquivo csv com os nomes e a quantidade de rifas de cada participante')
    if arquivo is not None:
        dados=carregar_dados(arquivo)
        exibir_tabela_nomes_quantidades(dados)
        dados_duplicados = multiplicar_linhas(dados)
        exibir_tabela_nomes_duplicados(dados_duplicados)
        vencedor = sortear_vencedor(dados_duplicados)
        exibir_vencedor(vencedor)
        

    else:
        st.info('Voce precisa carregar uma planilha')

    #se não tiverem as colunas nome e quantidade

# Ao botao clicado sortear de fato uma pessoa da lista dupçlicada 

# Exibir o vencedor abaixo do botao com fonte grande e verde 

# Exibir uma imagem abaixo do nome 

# Tocar um som de fundo de vitoria

#CHAMAR AS FUNÇÕES
exibir_imagem('chazi.png')
exibir_titulo('Bem vindos ao Super, Hiper, Ultra, Mega, TCHAPTCHURA!!! Sorteador de rifas do Shnat 25')
receber_arquivo()