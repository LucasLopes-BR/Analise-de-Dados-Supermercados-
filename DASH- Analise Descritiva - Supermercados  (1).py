#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pylab as matplt
import seaborn as sns


# In[2]:


#data principal
abras_br = pd.read_excel("ranking abras.xlsx")


# In[3]:


#manipulação para tirar Null
abras_br=abras_br.dropna()


# In[4]:


#novo df filtrando o que interessa para a pesquisa
abras_br_2=abras_br[['xxxxx','xxxxxxx', 'xxxxxx','xxxxx','xxxxxx']]


# In[5]:


#localizar os supermercados com sede em MG
abras_MG=abras_br_2.loc[abras_br_2.Sede=='MG']


# In[7]:


abras_MG_4=abras_MG.loc[7:18]


# In[15]:


#componentes para o dashboard
get_ipython().system('pip install jupyter-dash')
get_ipython().system('pip install dash-bootstrap-components')
get_ipython().system('pip install dash-bootstrap-templates')


# In[22]:


import dash
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_bootstrap_templates 


# In[23]:


#chamando o templante que sera utuilizado como base em https://bootswatch.com/
from dash_bootstrap_templates import load_figure_template
load_figure_template("cyborg")


# In[24]:


#definindo o app do deshboard
app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])


# In[25]:


#df para o deshboard
df_dash=abras_br_2


# In[27]:


#gráfico barra com ploty express
fig = px.bar(df_dash, x="xxxxx", y="xxxxx",color="xxxxx",template="cyborg")


# In[28]:


#gráfico barra com ploty express
fig2 = px.bar(df_dash, x="xxxxx", y="xxxxx",color="xxxxx",template="cyborg")


# In[29]:


#gráfico barra com ploty express
fig3 = px.bar(abras_MG_4, x="xxxx", y="xxxx",color="xxxxx",template="cyborg")


# In[30]:


#gráfico pizza  com ploty express
fig4 = px.pie(abras_MG_4,values='xxxxx', names='xxxx',template="cyborg")


# In[31]:


#gráfico para mostrar dados hierárquicos em um formato circular com ploty express - sunburst
fig5=px.sunburst(df_dash, path=['xxxxx','xxxxx'],values='xxxxx',color='xxxxx')


# In[32]:


#redefinindo o df - questão de organização
df_BR_2=df_dash[['xxxx','xxxx','xxxxx']]


# In[33]:


#tirando nulls
df_BR_2=df_BR_2.dropna()


# In[34]:


#biblioteca para permitir, por exemplo, converssoes de classes Python e que contéma definições de classe para os objetos que compõem gráficos
import plotly.graph_objects as go


# In[35]:


tab_BR_fat =go.Figure(data=[go.Table(
    header=dict(values=list(df_BR_2.columns)),
    cells=dict(values=[df_BR_2['xxxxx'],df_BR_2['xxxxx'],df_BR_2["xxxxx"]])),
                       ])


# In[31]:


#tirando nomes repetidos que irão entrar na lista de opções ligadas ao callback 1
Op=list(df_dash['xxxx'].unique())


# In[32]:


#adicionando mais uma opção na lista ligada ao callback 1
Op.append("TODAS AS SEDES")


# In[33]:


#lista do que ira entrar na lista de opções ligadas ao callback 2
Op2=list(df_dash['xxxxxx'])


# In[34]:


#adicionando mais uma opção na lista ligada ao callback 2
Op2.append("TODOS OS SUPERMERCADOS")


# In[35]:


'''
lista do que ira entrar na lista de opções ligadas ao callback 3
adicionando mais uma opção na lista ligada ao callback 3
'''
Op3=list(abras_MG_4['xxxxx'])
Op3.append("TODOS OS SUPERMERCADOS (MG)")


# In[36]:


#montando os mapas com as fronteiras das cidades de MG
import plotly.offline as pyo
import plotly.express as px
import json
import dash_table
from dash_table.Format import Format, Group, Scheme, Symbol


# In[37]:


#mapa com as cidades de todas as lojas do top4 em MG
df_mg=pd.read_excel('Cidades Supermercados MG_2.xlsx')


# In[38]:


#não esqueça de converter caracteres para UTF-8 para evitar erros
with open('geojs-31-mun.json',encoding='utf-8') as data:
    limites_MG = json.load(data)
for feature in limites_MG ['features']: 
    feature['id'] = feature['properties']['name']


# In[39]:


map_MG = px.choropleth_mapbox(df_mg,locations = 'cidade', 
                           geojson= limites_MG, #limites das cidades de MG
                           color='total_lojas',
                           mapbox_style = "carto-darkmatter",
                           center = {'lon':-44.38, 'lat':-18.1}, #coordenadas centrais de MG
                           zoom=5,
                           opacity=0.5, 
                            template="cyborg",
                              range_color = [1, df_mg['total_lojas'].max()])
map_MG.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# In[40]:


#preparando tabelas para o mapa com todas as lojas do top4 supermercados de MG
df_mg_2=df_mg[['xxxx','xxx','xxxx','xxxx','xxxx','xxxxx']]


# In[41]:


df_mg_2=df_mg_2.dropna()


# In[21]:


df_mg_2


# In[42]:


#tabela do mapa de MG
tab_MG =go.Figure(data=[go.Table(
    header=dict(values=list(df_mg_2.columns)),
    cells=dict(values=[df_mg_2.xxxxx,df_mg_2.xxxx,df_mg_2.xxxxx, df_mg_2.xxxxx, df_mg_2.xxxxxx,df_mg_2.xxxxxx])),
                       ])


# In[44]:


#mapa individual da rede de MG numero 1 no ranking ABRAS
df_BH=pd.read_excel('xxxxxxxxxxx')


# In[45]:


map_BH = px.choropleth_mapbox(df_BH,locations = 'cidade', 
                           geojson= limites_MG, 
                           color='Supermercados BH',
                           mapbox_style = "carto-darkmatter",
                           center = {'lon':-44.38, 'lat':-18.1},
                           zoom=5,
                           opacity=0.5, range_color = [1, df_BH['Supermercados BH'].max()])
map_BH.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# In[46]:


df_BH_2=df_BH[['xxxxx','xxxxx']]


# In[47]:


#tabela para acompanhar o mapa acima
tab_BH =go.Figure(data=[go.Table(
    header=dict(values=list(df_BH_2.columns)),
    cells=dict(values=[df_mg_2.xxxx,df_mg_2.xxxx])),
                       ])


# In[48]:


'''
PARA FAZER OS OUTROS MAPAS BASTA IR ADAPTANDO OS COMANDOS ANTERIORES.

QUALQUER DUVIDA ENTRE EM CONTATO COMIGO!
❤️
'''


# In[ ]:





# In[64]:


#MONTANDO O SISTEMA GRID DO DASBOARD
#É NECESSÁRIO CERTO CONHECIMENTO EM HTML/FRONTEND

grid =
#SUPERMERCADOS BRASILEIROS
html.Div(children=[
    html.Div(style = {'paddingTop': '25px','paddingBottom': '25px'}, children= [#div do titulo
        dbc.Row(#row é a linha e col a coluna, o conteúdo dentro das cols e cols dentro de rows
            dbc.Col(
                html.H6(children='DASHBOARD 01 - TESTE'),
            )),
        dbc.Row(
            dbc.Col(
                html.H6(children='Análise descritiva'),
            ),style={'textAlign': 'center'}),
        dbc.Row(
            dbc.Col(
                html.H3(children='Supermercados Brasileiros'),
            ),style={'textAlign': 'center'}),
         dbc.Row(
            dbc.Col(
                html.H6(children='Ranking ABRAS 2020'),
            ),style={'textAlign': 'center'})
    ]),
            
    html.Div(children=[
    html.Div(style = {'textAlign': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[#div gráfico 1
        dbc.Row(
            dbc.Col(
                html.H4(children='BRASIL'))),
        dbc.Row(
            dbc.Col(
                html.H6(children='Estado-sede x Número de lojas'))),
    ])
]),
        
    dbc.Row(
        dbc.Col(
            html.Div(children=['''Selecione a sede ''']))),
    dbc.Row(
        dbc.Col(#dropdown do grafico 1- permite que o usuário escolha um valor de uma lista de opções
            dcc.Dropdown(Op, value='TODAS AS SEDES', id='lista_lojas'),
            )),
        dbc.Row([#grafico 1 vai abaixo do dropdown 
            dbc.Col(
        dcc.Graph(
        id='Supermercados Nacionais no ranking ABRAS - Nº de lojas',
        figure=fig)
            ),
            
        
        ]),
    
    html.Div(children=[
    html.Div(style = {'textAlign': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row(
            dbc.Col(
                html.H6(children='Estado-sede x Faturamento bruto')))
    ]),
]),
    html.Div(children=[
        html.Div(children=['''Selecione o supermercado ''']),
            dcc.Dropdown(Op2, value='TODOS OS SUPERMERCADOS', id='lista_fat'),
            dcc.Graph(id='Supermercados Nacionais no ranking ABRAS - Faturamento Bruto em 2020 (R$)',
        figure=fig2),
    html.Div(style = {'textAlign': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Col(
            dcc.Graph(
        id='Supermercados Nacionais no ranking ABRAS - Faturamento Bruto em 2020',
        figure=fig5)),
        ]),
    ]),
    
    
#SUPERMERCADOS MINEIROS
    
    html.Div(children=[
        dbc.Row(
            dbc.Col(
                html.H6(children='Análise descritiva')
            ),style={'textAlign': 'center','color': 'blue'}),
        dbc.Row(
            dbc.Col(
                html.H4(children='Os quatro supermercados de Minas Gerais melhores classificados'),
            ),style={'textAlign': 'center','color': 'black'}),
        dbc.Row(
            dbc.Col(
                html.H6(children='Ranking ABRAS 2020'),
            ),style={'textAlign': 'center','color': 'black'}),
    ]),
    html.Div(style = {'textAlign': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row(
            dbc.Col(
                html.H6(children='Melhores classificados de Minas Gerais x Número de lojas'))),
    ]), 
    html.Div(children=['''Selecione o supermercado ''']),  
    dcc.Dropdown(Op3, value='TODOS OS SUPERMERCADOS (MG)', id='lista_MG_4'),
    dcc.Graph(
        id='Top 4 Supermercados de Minas Gerais no ranking ABRAS - Nº de Lojas',
        figure=fig3), 
    
    html.Div(children=[
    html.Div(style = {'textAlign': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row(
            dbc.Col(
                html.H6(children='Melhores classificados de Minas Gerais x Faturamento bruto em 2020 (R$)')))
   ]),
       ]),
             dcc.Graph(
        id='Top 4 Supermercados de Minas Gerais no ranking ABRAS - Faturamento Bruto em 2020 (R$)',
        figure=fig4),
  html.Div(children=[
    html.Div(style = {'textAlign': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row(
            dbc.Col(
                html.H6(children='Distribuição das lojas dos melhores classificados de Minas Gerais no Estado'))),
    ]),
    ]),
    #MAPA DE TODAS AS LOJAS DOS TOP 4 DISTRIBUIDOS NAS CIDADES DE MG
    #PARA BOTAR MAPA E TABRLA LADO A LADO USE dbc.Row([dbc.col(),dbc.col()])
        html.Div(children=[
    html.Div(style = {'align': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row([
            dbc.Col(
            dcc.Graph(id = 'mapa_MG', figure=map_MG),width = 7),
            dbc.Col(
                    dcc.Graph(id = 'table-MG',figure=tab_MG),width = 5),
    
]),
    ]),
]),
    # DIV PARA O MAPA DE CADA UMA DAS LOJAS DE CADA UM DOS TOP 4 DISTRIBUIDOS NAS CIDADES DE MG
    #PARA BOTAR MAPA E TABRLA LADO A LADO USE dbc.Row([dbc.col(),dbc.col()])
    html.Div(children=[
    html.Div(style = {'textAlign': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row(
            dbc.Col(
                html.H6(children='Distribuição das lojas dos melhores classificados de Minas Gerais no Estado por supermercado'))),
         ]),
    ]),
        
        html.Div(children=[
        html.Div(style = {'textAlign': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row(
            dbc.Col(
                html.H6(children='Supermercados BH'))),
         ]),    
    html.Div(style = {'align': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row([
            dbc.Col(
            dcc.Graph(id = 'mapa_BH', figure=map_BH),width = 7),
            dbc.Col(
                    dcc.Graph(id = 'table-BH',figure=tab_BH),width = 5),
    
]),
    ]),
]),
    #PARA FAZER DOS OUTROS SUPERERCADOS BASTA ADAPTAR OS CODIGOS ANTERIORES
     
        
]) #FINAL DIV GERAL


# In[65]:


# FAZENDO O DESIGN DO APLICATIVO, É A CARA DO PROJETO E COMO O UTILIZADOR VAI ENXERGAR O DASHBOARD

app.layout = html.Div(
    [
        dbc.Container(
            [       
                grid
            ]
        )
    ]
)

'''
COMANDO PARA OS CALLBACKS + AS FUNÕES LIGADAS A CADA UM DOS CALLBACKS
AQUI VOCE EXPLICA PARA O APP O QUE ELE VAI FAZER QUANDO O CALLBACK FOR CHAMADO
NO CASO, ELE VAI MODIFICAR CADA GRAFICO RELACIONADO
'''

@app.callback(
    Output('Supermercados Nacionais no ranking ABRAS - Nº de lojas', 'figure'),
    Input('lista_lojas', 'value'))

def update_grafico1(value):
    if value == "TODAS AS SEDES":
        fig = px.bar(df_dash, x="XXXXX", y="XXXXXX",color="XXXXX",template="cyborg")
    else:
        tab_filt=df_dash.loc[df_dash["XXXX"]==value,:]
        fig = px.bar(tab_filt, x="XXXXX", y="XXXXX",color="XXXXX",template="cyborg")
    return fig

'''
A PARTIR DO EXEMPLO ACIMA VOCÊ PODE FAZER OUTROS CALLBACKS, BASTA DAPTAR PARA CADA CASO
'''


# In[ ]:


#RODANDO O APP
#CASO TAMBÉM USE O JUPYTER, SE DER ERRO "1", BASTA MUDAR DEBUG PARA FALSE
# O USE_RELOADER VAI PERMITIR QUE O SERVIDOR DÊ UM RESTARTE AUTOMATICO EM CADA MUDANÇA NO CODIGO (BOTE FALSE QUANDO FIZER O DEPLOY)

if __name__ == '__main__':
    app.run_server(debug=False, use_reloader = False)


# In[ ]:





# In[ ]:




