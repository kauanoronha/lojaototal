import pandas as pd 
import streamlit as st 

st.set_page_config(
    layout="wide",
)
uploaded = st.file_uploader("Escolha o arquivo", type='csv')

if uploaded is not None:
    try:
        df = pd.read_csv(uploaded)
        selecionadas = df[['Item.enteredValue', 'Item.Units']]
        selecionadas.to_csv('data.csv', index=False, header=False)
        #df1 = pd.read_csv('data.csv')
        test = df[['Item.description', 'Item.enteredValue', 'Item.Units', 'Item.value']]
        test = test.set_index('Item.description')
        with open('data.csv', "rb") as file:
            btn = st.download_button(
            label="Baixar arquivo CSV",
            data=file,
            file_name="extracao_colunas.csv",
            mime="text/csv",
            help="Clique para baixar o arquivo CSV"
            )
            test
            
    except Exception as e:
        print(f'arquivo com o erro: {e}')

