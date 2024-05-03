import pandas as pd 
import streamlit as st


df = pd.read_html('ListaPromocoes.xls', skiprows=9)

st.dataframe(df)