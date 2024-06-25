import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Meu APP Streamlit",  # Título da aba
    page_icon="🦊",
)

st.title('Meu APP Streamlit') # Título
a = st.sidebar.radio('Choose:',[1,2]) # Menu lateral com opções

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz') #Carregando um dataframe de um bucket s3


@st.cache_data # Cache para otimizar funções muito grandes
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...') # Progresso
tamanho_amostra = st.slider("Selecione o tamanho da amostra para exibir o dataframe", 0, 10000) # Slider para a amostra
data = load_data(tamanho_amostra)
data_load_state.text('Loading data...done!')

st.divider() # Divisor

st.write("# Uber data")
data

code = """
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
"""

st.divider() # Divisor

st.write("<h2>Código para a função que gerou o dataframe</h2>",  unsafe_allow_html=True) # HTML
st.code(code, language="python", line_numbers=False) # Snippet de código

st.divider() # Divisor

st.write("<h2>Mapa com as coordenadas do dataframe</h2>",  unsafe_allow_html=True) # HTML

personalizado = st.text_input('Personalizar a legenda')

st.map(data[['lat', 'lon']]) # Mapa com as coordenadas
st.caption(personalizado) # Legenda para o mapa

st.markdown('_Markdown_') # MD
st.file_uploader('File uploader') # Botão de upload de arquivo
st.table(data.iloc[0:10]) # Selecionar um range de linhas do dataframe
st.button('Click') # Botão
st.warning('Warning message') # Alerta