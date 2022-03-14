import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import iqr
from IPython.display import display





def configuracion():
    st.set_page_config(
     page_title="Data Analysis",
     page_icon=":pizza:")

def menu(data_people):
    #funcion principal de visualizacion del programa
    #es un select box, para cada elección el el selecbox hay una funcion panel asignada
    #cada panel es un conjunto de graficas distintas, como paginas de una presentación
    panel_pos=st.selectbox('Página',['0','1','2'])  
    #panel_pos1=st.button('individuales')
    #panel_pos2=st.button('groupby')

    if panel_pos=='0':
        panel0(data_people)
    elif panel_pos=='1':
        panel1(data_people)
    elif panel_pos=='2':
        panel2(data_people)    

def panel0(data_people):
    columna=st.selectbox('columna',data_people.columns)
    graph_one_var(columna,data_people=data_people)
    
    st.write('hola')

def panel1(data_people):
    col1,col2=st.columns(2)
    with col1:
        columna=st.selectbox('columna',data_people.columns)
    with col2:    
        grouped=st.selectbox('columna2',data_people.columns)

    graph_two_var(columna,grouped,data_people=data_people)    
    st.write('hola')

def panel2(data_people):
    col1,col2,col3=st.columns(3)
    with col1:
        columna=st.selectbox('columna',['sexo','ccaa','edad'])
    with col2:    
        grouped=st.selectbox('columna2',['sexo','ccaa','edad'])
    with col3:
        grouped_bool=st.selectbox('columna3',['sexo','dependiente'])
    graph_three_var(columna,grouped,grouped_bool,data_people=data_people)    
    st.write('hola')


def import_my_bbdd():
    '''
    Función que importa la BBDD de personas mayores de 55 años, generada por el grupo 2, 
    a la cual le han sumado  datos fictios para poder obtener un volumen suficiente y así 
    poder generar un recomendador de actividades para personas que vivan en co-livings.
    '''
    data_people = pd.read_csv('fake_data_model.csv')
    data_people.drop(columns=['Unnamed: 0'], inplace=True)
    return data_people


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
    fig,ax=plt.subplots()
    #fig= plt.figure(figsize=(num_cat*1.5,10))
    ax = sns.violinplot(x=categ_var, y=numeric_var, data=dataframe, palette= palette)
    ax = sns.boxplot(x=categ_var, y=numeric_var, data=dataframe,fliersize=0, color='white')
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
    st.dataframe(table)

def better_visualizeME_and_describe_violinbox(dataframe, categ_var, numeric_var, categ_var2= None, palette='tab10'):
    '''
    Function that allows to obtain a more complete graph by merging boxplot and violinplot together with a table of descriptive metrics
    It is high recommendable! to use this type of graph for a categoric variable with 20 unique values maximum.
    ### Parameters (5):
        * dataframe: `dataframe`  origin table
        * categ_var: `str` categoric variable
        * numeric_var:  `str` numeric variable
        * categ_var2: `str` by default None, but if pass please a categoric variable
        * palette:  `str` by default 'tab10', but you can choose your palette
    '''
    # Generate ViolinBOX graph
    fig,ax=plt.subplots()
    ax = sns.violinplot(x=categ_var, y=numeric_var, data=dataframe, hue = categ_var2, split=True)
    ax = sns.boxplot(x=categ_var, y=numeric_var, data=dataframe, hue = categ_var2, fliersize=0, color='white')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha='right')
    handles, labels = ax.get_legend_handles_labels()
    l = plt.legend(handles[0:2], labels[0:2], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.);
    titulo= categ_var.upper() + ' VS ' + numeric_var.upper() + ' VS ' + categ_var2.upper()
    plt.title(titulo, fontsize=15);
    st.pyplot(fig)

    # Metrics table
    cabeceras= ['Metrics',]
    fila1 = ['Upper limit',]
    fila2 = ['Q3',]
    fila3 = ['Median',]
    fila4 = ['Q1',]
    fila5 = ['Lower limit',] 
    fila6 = ['Count',] 
    iqr_ = iqr(dataframe[numeric_var], nan_policy='omit')
    d = [ fila1, fila2, fila3, fila4, fila5, fila6]
    if categ_var2 != None:
        for i in sorted(list(dataframe[categ_var].unique())):
            for j in sorted(list(dataframe[categ_var2].unique())):
                nombre= str(i)+  '/' + str(j)
                cabeceras.append(nombre)
                mediana = round(float(dataframe[(dataframe[categ_var].isin([i]))& (dataframe[categ_var2].isin([j]))][[numeric_var]].median()), 2)
                fila3.append(mediana)
                q1 = round(np.nanpercentile(dataframe[(dataframe[categ_var].isin([i]))& (dataframe[categ_var2].isin([j]))][[numeric_var]], 25), 2)
                fila4.append(q1)
                q3 = round(np.nanpercentile(dataframe[(dataframe[categ_var].isin([i]))& (dataframe[categ_var2].isin([j]))][[numeric_var]], 75), 2)
                fila2.append(q3)
                th1 = round(q1 - iqr_*1.5, 2)
                fila5.append(th1)
                th2 = round(q3 + iqr_*1.5, 2)
                fila1.append(th2)
                cantidad = int(dataframe[(dataframe[categ_var].isin([i]))& (dataframe[categ_var2].isin([j]))][[numeric_var]].count())
                fila6.append(cantidad)
    else:
        for i in sorted(list(dataframe[categ_var].unique())):
                nombre= str(i)
                cabeceras.append(nombre)
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
                cantidad = int(dataframe[dataframe[categ_var].isin([i])][[numeric_var]].count())
                fila6.append(cantidad)
    table = pd.DataFrame(d, columns=cabeceras)
    table = table.set_index('Metrics')
    
    #plt.show()
    st.dataframe(table)


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

        if (data_people[variable].max() - data_people[variable].min())>10 :
            fig= sns.displot(data_people[variable], binwidth = 3, kde= True, color=colors[0])
        else:
            fig= sns.displot(data_people[variable], discrete=True, color=colors[0])

    else:
       fig= sns.catplot(x = variable , data= data_people , kind= 'count', palette= colors)
       fig.set_xticklabels(rotation=40, ha='right')
    st.pyplot(fig)
    st.write('hey')
    


def graph_two_var(var1, var2,data_people):
    '''
    ## Función que sirva para obtender graficas cruzando 2 y 3 variables.
    ### Parámetros(3):
        * var1: `str` variable de tipo 'int64', 'O' o 'bool'
        * var2: `str` variable de tipo 'int64', 'O' o 'bool'
    '''
    colors = data_tripus_palette()
    fig=plt.figure()
    if var1==var2:
        graph_one_var(var1,data_people)
    else:    
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
            st.pyplot(ax)    

        elif data_people[var2].dtype == 'bool' or data_people[var1].dtype == 'bool':
            if data_people[var2].dtype == 'bool':
                micat = var1
                mibool = var2
            else:
                micat = var2
                mibool = var1
            fig=plt.figure()    
            fig = sns.countplot(x=micat, data= data_people, hue=mibool, palette=colors)
            fig.tick_params(axis='x', rotation=40)
            titulo = micat.upper() + ' VS ' + mibool.upper()
            plt.title(titulo)
            plt.legend(bbox_to_anchor=(1, 1), loc=2) 
            st.pyplot(fig)    

def graph_three_var(var1, var2, var3,data_people):
    '''
    # Función que sirva para obtender grafica cruzando 3 variables.
    ## Parámetros(3):
        * var1: `str` variable de tipo 'int64' o 'O'
        * var2: `str` variable de tipo 'int64' o 'O'
        * var3: `str`  variable de tipo 'bool'
    '''
    
    colors = data_tripus_palette()
    if data_people[var3].dtype == 'bool' and ((data_people[var2].dtype == 'int64' and data_people[var1].dtype == 'O') or (data_people[var1].dtype == 'int64' and data_people[var2].dtype == 'O')): 
        if data_people[var2].dtype == 'int64':
            micat = var1
            minum = var2
        else:
            micat = var2
            minum = var1
        better_visualizeME_and_describe_violinbox(data_people, micat, minum, var3, palette= colors)
    else:
        st.write('Por favor, incluye una variable numérica, una categórica y una booleana')


data_people = import_my_bbdd()   
configuracion()
menu(data_people)  
'''
# Welcome to Streamlit!
'''