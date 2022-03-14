import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import iqr
from IPython.display import display


data_people = pd.read_csv('fake_data_model.csv')
data_people.drop(columns=['Unnamed: 0'], inplace=True)


def configuracion():
    st.set_page_config(
     page_title="Data Analysis",
     page_icon=":pizza:")

def menu():
    #funcion principal de visualizacion del programa
    #es un select box, para cada elección el el selecbox hay una funcion panel asignada
    #cada panel es un conjunto de graficas distintas, como paginas de una presentación
    panel_pos=st.selectbox('Página',['0','1','2','3','4','5','6','7','8','9'])  
    panel_pos1=st.button('individuales')
    panel_pos2=st.button('groupby')

    if panel_pos=='0':
        panel0()
    elif panel_pos=='1':
        panel1()

def panel0():
    columna=st.selectbox('columna',['sexo','ccaa','edad'])
    graph_one_var(columna,data_people=data_people)
    
    st.write('hola')

def panel1():
    col1,col2=st.columns(2)
    with col1:
        columna=st.selectbox('columna',['sexo','ccaa','edad'])
    with col2:    
        grouped=st.selectbox('columna2',['sexo','ccaa','edad'])

    graph_two_var(columna,grouped)    
    st.write('hola')


def data_tripus_palette():
    '''
    Función que trae la paleta de colores específica elegida para utilizar el equipo de DATA en el Desafío de Tripulaciones GRUPO 2.
    '''
    colors = ['#0294AB', '#51BF83', '#002D52','#007D60', '#D76174', '#95B0B7', '#003EAD',  '#FC9039', '#56423E', '#FFA0B6', '#AE5000', '#F3EED9', '#E36F60', '#FFE086', '#323232', '#CBCCFF', '#786AB0']
    return colors

def visualizeME_and_describe_violinbox(dataframe, categ_var, numeric_var, palette= 'tab10', save= False):
    '''
    Function that allows to obtain a more complete graph by merging boxplot and violinplot together with a table of descriptive metrics
    It is high recommendable! to use this type of graph for a categoric variable with 20 unique values maximum.
    ### Parameters (5):
        * dataframe: `dataframe`  origin table
        * categ_var: `str` categoric variable
        * numeric_var:  `str` numeric variable
        * palette:  `str` by default 'tab10', but you can choose your palette
        * save:  `bool` by default True, the function save the plot and table generated
    '''
    # Generate ViolinBOX graph
    num_cat = len(list(dataframe[categ_var].unique()))
    fig,ax = plt.figure(figsize=(num_cat*1.5,10))
    ax = sns.violinplot(x=categ_var, y=numeric_var, data=dataframe, palette= palette)
    #ax = sns.boxplot(x=categ_var, y=numeric_var, data=dataframe,fliersize=0, color='white')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha='right')
    titulo= numeric_var.upper() + '_vs_' + categ_var.upper()
    plt.title(titulo, fontsize=15)

    st.pyplot(fig)

    # Save graph
    if save == True:
        graph = 'visualizeME_Graphic_violinbox_' + titulo.lower() + '.png'
        plt.savefig(graph)

    # Metrics table
    cabeceras= ['Metrics',]
    fila1 = ['Upper limit',]
    fila2 = ['Q3',]
    fila3 = ['Median',]
    fila4 = ['Q1',]
    fila5 = ['Lower limit',]  
    iqr_ = iqr(dataframe[numeric_var], nan_policy='omit')
    d = [ fila1, fila2, fila3, fila4, fila5]
    for i in sorted(list(dataframe[categ_var].unique())):
        cabeceras.append(i)
        mediana = round(float(dataframe[dataframe[categ_var].isin([i])][[numeric_var]].median()), 2)
        fila3.append(mediana)
        q1 = round(np.nanpercentile(dataframe[dataframe[categ_var].isin([i])][[numeric_var]], 25), 2)
        fila4.append(q1)
        q3 = round(np.nanpercentile(dataframe[dataframe[categ_var].isin([i])][[numeric_var]], 75), 2)
        fila2.append(q3)
        th1 = round(q1 - iqr_*1.5, 2)
        fila5.append(th1)
        th2 = round(q3 + iqr_*1.5, 2)
        fila1.append(th2)
    table = pd.DataFrame(d, columns=cabeceras)
    table = table.set_index('Metrics')
    
    # Save table
    if save == True:
        name = 'visualizeME_table_violinbox_' + titulo.lower() + '.csv'
        table.to_csv(name, header=True)

    

    #plt.show()
    display(table)




def graph_one_var(variable,data_people):
    '''
    ## Función para mostrar gráfico de una sola variable del dataframe
    ### Input(1):
        * variable `str`: nombre de la columna del dataframe que quieres ver gráficamente
    ### Return(1):
        * plot: displot si es numérica y countplot en caso de que sea categórica
    '''
    fig=plt.figure()
    colors = data_tripus_palette()
    if data_people[variable].dtypes == 'int64':
       fig= sns.displot(data_people[variable], binwidth = 3, kde= True, color=colors[0])

    else:
       fig= sns.catplot(x = variable , data= data_people , kind= 'count', palette= colors)
       fig.set_xticklabels(rotation=40, ha='right')
    st.pyplot(fig)
    st.write('hey')
    


def graph_two_var(var1, var2):
    '''
    ## Función que sirva para obtender graficas cruzando 2 y 3 variables.
    ### Parámetros(3):
        * var1: `str` variable de tipo 'int64', 'O' o 'bool'
        * var2: `str` variable de tipo 'int64', 'O' o 'bool'
    '''
    colors = data_tripus_palette()
    fig=plt.figure()
    if (data_people[var2].dtype == 'int64' or data_people[var1].dtype == 'int64'):
        if data_people[var2].dtype == 'int64':
            micat = var1
            minum = var2
        else:
            micat = var2
            minum = var1
        visualizeME_and_describe_violinbox(data_people, micat, minum, palette= colors)
    elif(data_people[var2].dtype == 'O' and data_people[var1].dtype == 'O') or (data_people[var1].dtype == 'O' and data_people[var2].dtype == 'O'):
        if data_people[var1].nunique() <= data_people[var1].nunique():
            micat1 = var1
            micat2 = var2
        else:
            micat1 = var2
            micat2 = var1
        ax = sns.catplot(x= micat1, col= micat2, col_order=list(data_people[micat2].value_counts().index), col_wrap=3, data = data_people, kind="count", height=3, aspect=2, palette= colors)
        titulo = micat1.upper() + ' VS. ' + micat2.upper()
        plt.suptitle(titulo)
        ax.fig.subplots_adjust(top=0.8)
        ax.fig.suptitle(titulo)
        ax.set_xticklabels(rotation=40, ha='right')

    elif data_people[var2].dtype == 'bool' or data_people[var1].dtype == 'bool':
        if data_people[var2].dtype == 'bool':
            micat = var1
            mibool = var2
        else:
            micat = var2
            mibool = var1
        ax = sns.countplot(x=micat, data= data_people, hue=mibool, palette=colors)
        ax.tick_params(axis='x', rotation=40)
        titulo = micat.upper() + ' VS ' + mibool.upper()
        plt.title(titulo)
        plt.legend(bbox_to_anchor=(1, 1), loc=2) 
    st.pyplot(ax)    




    
configuracion()
menu()  
'''
# Welcome to Streamlit!
'''