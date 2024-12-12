import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import time
import base64


st.set_page_config(
    page_title="Mega Rifa Shnat",
    page_icon="✡️",
    layout="wide",  # Modo "wide"
    initial_sidebar_state="expanded"
)

# Configuração do tema escuro via atributos de configuração
st.markdown(
    """
    <style>
    /* Força o modo escuro no Streamlit */
    html {
        color-scheme: dark;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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
    dados_csv['Quantidade de Rifas'] = dados_csv['Quantidade de Rifas'].astype(str)
    dados_csv['Quantidade de Rifas'] = dados_csv['Quantidade de Rifas'].str.split('.').str[0]
    dados_csv['Quantidade de Rifas'] = dados_csv['Quantidade de Rifas'].astype(int)
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

# Sortear um vencedor
def sortear_multiplos_vencedores(dados_duplicados, itens):
    if st.button('Sortear Vencedores'):
        lista_nomes = dados_duplicados['Nome'].tolist()
        with st.spinner('Preparando sorteio...'):
            time.sleep(2)

        for item in itens:
            with st.spinner(f'Sorteando para o item: {item}...'):
                time.sleep(2)
                st.text('Embaralhando os nomes...')
                time.sleep(2)
                st.text(f'Sorteando o vencedor para o item {item}...')
                time.sleep(2)
                vencedor = random.choice(lista_nomes)
                lista_nomes = [nome for nome in lista_nomes if nome != vencedor]
                st.markdown(f'<p style="font-size:35px; color:lightgreen;">Item: {item} - Vencedor: {vencedor}</p>', unsafe_allow_html=True)

        exibir_imagem('macaco.gif')
        tocar_som('trompete.mp3')
        exibir_mensagem('chazak ve ale')

# Tocar um som de fundo de vitoria
def tocar_som(caminho_som):
    audio_file = open(caminho_som, 'rb')
    audio_bytes = audio_file.read()    
    # Exibir o arquivo de áudio sem controles e com autoplay
    encoded_audio = base64.b64encode(audio_bytes).decode('utf-8')
    # Exibir o arquivo de áudio sem controles e com autoplay usando HTML
    st.markdown(f'<audio src="data:audio/mp3;base64,{encoded_audio}" autoplay >', unsafe_allow_html=True)

# Exibe mensagem
def exibir_mensagem(string):
    st.text(string)

# Exibe um vencedor
def exibir_vencedor(vencedor):
    if vencedor is not None:
        st.markdown(f'<p style="font-size:30px; color:green;">O vencedor é:</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size:30px; color:green;">{vencedor}</p>', unsafe_allow_html=True)
        exibir_imagem('macaco.gif')
        tocar_som('trompete.mp3')
        exibir_mensagem('chazak ve ale')

# Recebe o arquivo csv através do upload
def receber_arquivo():
    arquivo = st.file_uploader('Insira um arquivo csv com os nomes e a quantidade de rifas de cada participante')
    if arquivo is not None:
        dados=carregar_dados(arquivo)
        exibir_tabela_nomes_quantidades(dados)
        dados_duplicados = multiplicar_linhas(dados)
        exibir_tabela_nomes_duplicados(dados_duplicados)
        itens = ['Vale de 300 reais Gurume', 'Kit Dermage', 'Vinho Viña Eden', 'Consulta KamiNutri', 'Cesta myBrownies']
        sortear_multiplos_vencedores(dados_duplicados, itens)
        
        

    else:
        st.info('Voce precisa carregar uma planilha')

#Ainda falta sortear os premios para cada em ordem

#CHAMAR AS FUNÇÕES
exibir_imagem('chazi.png')
exibir_titulo('Bem vindos ao Super, Hiper, Ultra, Mega, TCHAPTCHURA!!! Sorteador de rifas do Shnat 25')
receber_arquivo()