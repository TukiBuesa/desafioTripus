import pandas as pd
import streamlit as st


def configuracion():
    st.set_page_config(
     page_title="Data Analysis",
     page_icon=":pizza:")

def menu():
    #funcion principal de visualizacion del programa
    #es un select box, para cada elección el el selecbox hay una funcion panel asignada
    #cada panel es un conjunto de graficas distintas, como paginas de una presentación
    # panel_pos=st.selectbox('Página',['0','1','2','3','4','5','6','7','8','9'])  
    panel_pos1=st.button('individuales')
    panel_pos2=st.button('groupby')

    if panel_pos1==True:
        panel0()
    elif panel_pos2==True:
        panel1()

def panel0():
    columna=st.selectbox('columna',['col1','col2'])
    st.write('hola')

def panel1():
    columna=st.selectbox('columna',['col1','col2'])
    grouped=st.selectbox('columna2',['col1','col2'])
    st.write('hola')
    
configuracion()
menu()  
'''
# Welcome to Streamlit!
'''