import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import iqr
from IPython.display import display





def configuracion():
    st.set_page_config(
     page_title="VITA Data Analysis",
     page_icon=":pizza:")

def menu(data_people):
    #funcion principal de visualizacion del programa
    #es un select box, para cada elección el el selecbox hay una funcion panel asignada
    #cada panel es un conjunto de graficas distintas, como paginas de una presentación
    #panel_pos=st.selectbox('Página',['0','1','2'])  
    st.sidebar.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADFCAMAAAAmGE1yAAAApVBMVEX///8AAACL+/n8/PwEBAQICAj5+fkWFhYQEBDz8/MNDQ3v7+/o6Oj29vbs7OxFRUXh4eE4ODjPz88dHR22trYvLy8nJyeIiIiZmZnHx8daWlqfn5/X19c0NDR3d3eqqqpnZ2eRkZFTU1Nubm6np6dDQ0MhISFNTU2AgIB6enqJiYm0tLRqamrAwMBZWVnN/fyu/Pvm/v7i/v67/fu0/PvI/fye+/q7qHFyAAAOmUlEQVR4nO1da2OivBLWAqKCCl5R8YJ4raW7293t//9pBwgkM0nQLtYa3tPn23ZRMsncZzLWat/4xje+8Q31oFn+dOV5c+/cdzqPXswNmIbuvqnXYxjmeDOJWo9eUEk4bh3BnPUfvaRy8Ad1Dm41KREJqc8qyV0SQszpoxdVBhJC9PmjF1UGfVMgpO49elFlMBUJqeaJRE2BkObw0Ysqg2FbIGRhP3pRZbDSBUJC7dGLKgNPoMNYPXpNpTARCBk7j15TKRwFQtbVdIGXAmdVUvnWtDVPyN5/9JpKobHhCdlUk7M6PZ6Q4NFLKgd7xNFRTdc3DhDHHCG77qOXVA7+niOkmmY99uK5cKSiZj324jnnt6LKN3Z+DUzIoZLxeow5JyLHRy+oLAJORM6PXlBZcD7juKoiUgsxIb2qikht9h8REc7VMraPXlBZWDiFPaisiHA+o1tRR0twtV4q6mgJHkpFY5EYZ+ShVDUWibFF6bmKJoISYA9l03j0ekrjhAg5PXo5paEhw17ZoKpWayHDblazCpqgiwy7W8lyQgqcQ5lVV9axPZw8ejnlgSL2diUrbgRzaA8rm0CJ8Qw5a2c9ejmlgWsK68q6vrUOqilUsk2AwNr9R2QdhVUfcX0tfzUPvG1kK2Zx+tCMXJV1zQ96g0Rf681F+JFGu8aXCR3qerhWT3COY6CszfUVZd2KTrP1/IsUoQfNyGVZ1yKXa5FYDIsp15z5JmnWMdZfk82ApelmdOnJzpwvCMUGtCBPrNnncJS5DPrpK0qryIxclvW5pKurPpbR3h0uXcCxzcsxTjfyluHJm96WqUXRyEVZj8TzSD/DE29NjzuucjS6EOTYXva0uTnfQgpy4sMLD/o4H9nem0Re9CMUE2s66UkO7rXoqK3VjomdebpBmlD98EJKq4s8GX239adLwj2jfJFaARXJ8+7J87yzcODOGp2dEZanBGrfC7KuPUNnvxkmi2+9kEWmqk6zo+POFPu+GC16vc0FO9qQa5yuG5PSZge2al3w4c/w4MyAqKGsFXJna845dMV2QgFYBrUtX9+v1wcX9eYlHAvfA4EEZDDPnJMWcdPa4Xok9hLKgPLjViBjw9eSAt+AuaBCHz5jIo6OWvf12soNXC92wU51j9IjNEseCUqhPBc9tQXvNAkdqWRf4abmYYtrSK/Mz7TDgkMs2XUBtW+hDw8vMxiTeDENZ3jsiZKtoz8ZvZXFNVCxop4zK9ILo3K5Z9jxW5Sb6yzBS2d2d+rNZDJhuMcNeHD/bAvFMNqX1z/AP7dH4PtKhkQw81CQm9O2QCjbYehKTUXMRjZ4UO9FCYvgnBlV733IccZu69hz9mAhg18E7C+V5+a0s6gkBZizoVXzF2xxM8IguMU7r05COvRRkOyfNqdnUiptgJSWvCwdXaejvU5CrA5Tbfo6O1yUocl9Uh/QsT/5ZN1d+sdDGV8Z8rA8Dz/lu+skIO3nQ8ZY2XnUWkgU6qP0OZttXvs1ots/zzV1qYwU5OGmrObWX9SLoe+JQ5zWhrps0dQh5hrB0paK7pqK5RgGj06+Y4sy/hbkYZne83f1IjTdcOsT1kmd5i1l8gHVO5iz6rN4+21Gx/4MpaGRN5KUIgQqLVkLitDZTGDsN0HU1fI4OREuix6ITh0//jLdi1brAw19xFKdlzJL1fmhpyXRFg3M4wTt0XrrZwJJCEnc3yE92x3V4gnb68BJWSJ3ly8f51WBXQlvC2UZZYmHI29/jdHL2WEUB+nfYlZq0HCFxbV2oogWYOmnAMoMH1fnCbYyzdPQ05K2mzl8j7bro3NL66iJR8DSfBsqwMmBND0gZWNkVfidzxVPzhm/YnyUEHhJbCB1UHyOubCSJ2ZoH29tkB8dO5BUQsK+PNIXvortBYm+3v68x/jz9jHrCHseCu4i9bEdwVV4kjeOnXNmMA65qDYmMW0jv1/oIfMslN0hJJzx4/2J4OePjxzL5ML3UmKRLcBuDHl3/DdqMNh9jSTp0vZk17eke0JNQcoZP54Y3t+u0oEclKJGgXRnKbBqO6erXAI1To2RnZzRq1ULwIf10QF8F79zmfpNDPvbOyDk6efVM0FRVVG2FHvcOGGUau8k+UC7IpcZoZ1jzLX7KeqXNEIHng8vI0e6ob9+PiH8uEYIlPWiMCDCRm0J/6+Rhrqxc05rLO1c9SUxpfHcQIceO7/w5qaLtVYmZomr/wPT8fTzGiFQ1uUNgJ0V5/siQojCjO0BddnyPMww0UAbGx967DPCS8GcHcnUW3JRgjuQ61IC7fpIprRaz3wQhQghIhLzOl0f2Q5tmBCW5kmBS5zwkg18UG7rMgUeh1W/nnhc4S0k67J+eOdFUDmQEI14YkfQc5AqLctLNnew0rggIFYU8JU4HWgT7hz3Rc56evp9mRDUlClJ+057YoIAEuKk25sIV0QJdofO+TX5V5ps6e/4z0KFj9SLR9h82ZARckVI0J1pIVLurGQhFUzWbNN3LxzUBWKOU6LS5JeDFF6aWoVxA/wuf0QP5N8JgdlSITxsTSiZOkyiMCuWOe6JwhWuBI1W8XNd3OGdajQHCAnw11vE59QDrQQhGkwf8j61v6YazVgDzxEELas2/WAXx1/Gph8vyAoxZ6YRqAbsCrtp3ggIb/ZSjfPrnSfk70VCoAbh8teNiFUtzGNry9Q005kOWTwZcuFBrTBO8yKtI6cpiJaKAD/n92i1LdF6eQb7z79pLRRQo7Cs5TFW2XuxdmXGhJ5clrUzya62aCJXH4epG615yV+MMf8KmI/IPky0dfxwkAnNG3ck75d9FFTOhR6cA9Kyi6gBoyaqFBoeWfky+1xn+Dputs3RxsuCx1W68zvASZmC34KDcuNtafhHsqM6q/7+/ZcDwc00rI9ci5jW1Q8kSAG8RTIkrawkAAqIHac/ZXOHSDbMHIKgP9MTNswyjpfP67xyvwGW/gc4k/cr5hCJCPN9LZC8NNbZdwNdo7/4ljOckW2VlnQTTFPPRD+2wG7lJmgrd+x3SErfftOA5Jp/ggIFOnMDslXzmEetGrBj+ng3ygRivyqI3xyy6wdbAwovL1C2hLvaybceeF/v19vf379/fyCsQlMFsoAdslV9EDBV68uMYyEdWS5xH8FMJrNUPl85jG3MS+lGdtztS/weC2ir+ugM5F8LDP7d8QMFdFhEoRnPGvSC2owNpxwl+mJevsKOZ7qkpRF/Dbhthy1kN+Qo0Q/TAjq0zLptuiglC6sv/RnwVAx34perUqXA8yrit3TOcJ8OfE6le0JZhP2kqNE5L6eMk50AoRvKyFrD0B00m01z3AvP9i2dUDZ2Ksy+swRHZKzFZXZWu/zA2qNjv7DrLCtDtL1kecBH5DKhWtefTmN93bqxn4tLbpgBdNnbS2n61T6fXnu9w/oIc408ckmepRoPTI4pVfa4ig6nAnXIN81JYYVCazQut8TlqckR0abAwZ7dpZUuEgdqUQzm5feulXm8zcwuAUm8yzXN1qyAiBjjIq36AeTuOPVrgat1j0bcTlDccbGIytNB679uZqY11hqh3+GCjSZthcuWcMudt2lmNWgiu8V0o7SwdyOc4rqg4PH80/dmzoIe5kLWZW+6x+2BqIix9NktV/esvDrosiiSGXZp3uxGSCbOpTBebnlZI29NM1nFCBh29w7dv11hwk6KAjP4UayyRetL5gCCnOxdrjduZcWXC2bwI6AFIdh1Cu6cXur7LI3WUnTKTe+mLaO5OBNm9QP2/eVaZa7BfuEpGW9v8iA6p2zv9RPcDxCx32nymI2d8uIg6YOY51+H2plB21m7dNPlFXS2C9ipdYM5T0CT7oixYBR6xwun/ilX8mLg/4+wcwHRl0jQQKLmnpfLG/3n3t7Q9UH5wJ+glQsI9bEygNz2nQdxWv55tfJvneeyygWEv5UAXIj7hFWfC9YB+MKtdsV0YwUmYlg02BzxohYwdVKB6Te0q9IQQicQVqk/2qNPHdwN76qByqf69xtZ0CzeM/gaM/JJ8Kg8LwVxBtHIXvUZJYyxBEnH0Yji84hYhUCXSDMwI6+KXYflwQIbV8I78ztHI58H1g4rHS4GBseoPUmiwXpQexIZAEVKxafGTPcXDwRo33sktT4PIBEuvXkCtK/a0+BYD4NMZVVH+1osjpVPqAQlGKUnU69Y1C/30QOmtFSe7QGui7Tld9pBCkVl35fdTii4cAdSKCpPee2AUpGccUCJXWXtO2W1O11eiwKdsSXvSH4JQKdtwX6DBLbC42pha1FBygooLYWHj51BrUi+37Bj8j4J7M8AbLEs2G9QPrxHHfSTgJrW5LGGw5SWwgE7uoJbcDMW2Bl1Bw2i3/SRB00gPFRXaaHW5wJCgIOylD6gAjqHq4TAR9SdooZnbUplBERVlycrPRR4iPaL7BGQClJ4gDAmROozgjZvhX9ywkasJUu+aZLGZQWBW21l2hXcw1D59wjxtBNZlwm4CaGwXefu68uEGRTdlM6goDmusi0HlCpdPUTNthI7AW67qCwi3AAaSWIXFNiVFhFObYnJHnBxpqf23F30YziCoYBxl+Jj6FewTUoIEYEvpno514dCIihY0DQpq2SpBDSHRCgaBOz/lP/VODhMh9e/QPkq7MJnQC23nNoCE0QU11k1ruWWc+SZC1+QTVUK8GoTlvYWk5+F4qKeAPIWtt7M85WX5BSDBRMQiIOYsVRd9xIEwAN+BTVCFj6KDVxKAtpEeKeC+Vk9dTOMEA2QpQPaidUWrwyQVgcwAcxaONjd6Mr8DjdQs/V2vvsOzTqMFS4cckDVHiIPbPSTUQXVmwFad/2UJIW0FbUhQqumyjgDKUnu0YCRSRVirBp3L7O9eV5Ta99UOuUgouimrHGsisbKgMe6MYF5Ud5752HLxnvrs2qYdATJ1NZbxvE/EP6B4y5zom495CKcCfyRGKM3VLdf4wo0f+I2U1p08zCvoHgwaHbkhev1cn7jb6EoAU1TPYP1jW/8n+B/59LrxDBxqAEAAAAASUVORK5CYII=')
    panel_pos=st.sidebar.selectbox('Página',['1','2','3']) 
    #panel_pos1=st.button('individuales')
    #panel_pos2=st.button('groupby')

    if panel_pos=='1':
        panel0(data_people)
    elif panel_pos=='2':
        panel1(data_people)
    elif panel_pos=='3':
        panel2(data_people)    

def panel0(data_people):
    columna=st.selectbox('Columna',data_people.columns)
    graph_one_var(columna,data_people=data_people)
    
    

def panel1(data_people):
    col1,col2=st.columns(2)
    with col1:
        columna=st.selectbox('Columna',data_people.columns)
    with col2:    
        grouped=st.selectbox('Columna 2',data_people.columns)

    graph_two_var(columna,grouped,data_people=data_people)    
    

def panel2(data_people):
    col1,col2,col3=st.columns(3)
    types=data_people.dtypes
    types_cat = (types!='bool') & (types!='int64')
    types_int = (types=='int64')
    types_bool = (types!='bool')
    
    with col1:
        columna=st.selectbox('Columna categórica',data_people.columns[types_cat])
    with col2:    
        grouped=st.selectbox('Columna numérica',data_people.columns[types_int])
    with col3:
        grouped_bool=st.selectbox('Columna booleana',data_people.columns[~types_bool])
    graph_three_var(columna,grouped,grouped_bool,data_people=data_people)    
    


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
    #num_cat = len(list(dataframe[categ_var].unique()))
    fig,ax=plt.subplots()
    #fig= plt.figure(figsize=(num_cat*1.5,10))

    if dataframe[categ_var].nunique()>10 and dataframe[categ_var].dtype=='int64' :         
        ax = sns.violinplot(x=(pd.cut(dataframe[categ_var], bins=10)), y=numeric_var, data=dataframe, palette= palette)
        ax = sns.boxplot(x=(pd.cut(dataframe[categ_var], bins=10)), y=numeric_var, data=dataframe,fliersize=0, color='white')
    else:
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
    if (dataframe[categ_var].nunique()<=10): 
        st.table(table)

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
    ax = sns.violinplot(x=categ_var, y=numeric_var, data=dataframe, hue = categ_var2, split=True,palette=palette)
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
    st.table(table)


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
        elif(data_people[var2].dtype == 'O' and data_people[var1].dtype == 'O') :
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
            fig,ax=plt.subplots()  
            ax = sns.countplot(x=micat, data= data_people, hue=mibool, palette=colors)
            ax.tick_params(axis='x', rotation=40)
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
    if var1==var2:
        graph_two_var(var1=var1,var2=var3,data_people=data_people)
    else:
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
