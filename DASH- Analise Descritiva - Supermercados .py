#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pylab as matplt
import seaborn as sns


# In[2]:


abras_br = pd.read_excel("ranking abras.xlsx")


# In[3]:


abras_br=abras_br.dropna()


# In[4]:


abras_br_2=abras_br[['Razão Social','Faturamento Bruto em 2020 (R$)', 'Nº de lojas','Sede','Nº de funcionários']]


# In[5]:


abras_MG=abras_br_2.loc[abras_br_2.Sede=='MG']


# In[6]:


#abras_MG


# In[7]:


abras_MG_4=abras_MG.loc[7:18]


# In[15]:


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


from dash_bootstrap_templates import load_figure_template
load_figure_template("cyborg")


# In[24]:


app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])


# In[25]:


df_dash=abras_br_2


# In[26]:


df_dash


# In[27]:


fig = px.bar(df_dash, x="Sede", y="Nº de lojas",color="Razão Social",template="cyborg")


# In[28]:


fig2 = px.bar(df_dash, x="Sede", y="Faturamento Bruto em 2020 (R$)",color="Razão Social",template="cyborg")


# In[29]:


fig3 = px.bar(abras_MG_4, x="Sede", y="Nº de lojas",color="Razão Social",template="cyborg")


# In[30]:


fig4 = px.pie(abras_MG_4,values='Faturamento Bruto em 2020 (R$)', names='Razão Social',template="cyborg")


# In[31]:


fig5=px.sunburst(df_dash, path=['Sede','Razão Social'],values='Faturamento Bruto em 2020 (R$)',color='Faturamento Bruto em 2020 (R$)')


# In[32]:


df_BR_2=df_dash[['Razão Social','Faturamento Bruto em 2020 (R$)','Sede']]


# In[33]:


df_BR_2=df_BR_2.dropna()


# In[37]:


df_BR_2


# In[34]:


import plotly.graph_objects as go


# In[35]:


tab_BR_fat =go.Figure(data=[go.Table(
    header=dict(values=list(df_BR_2.columns)),
    cells=dict(values=[df_BR_2['Razão Social'],df_BR_2['Faturamento Bruto em 2020 (R$)'],df_BR_2["Sede"]])),
                       ])


# In[31]:


Op=list(df_dash['Sede'].unique())


# In[32]:


Op.append("TODAS AS SEDES")


# In[33]:


Op2=list(df_dash['Razão Social'])


# In[34]:


Op2.append("TODOS OS SUPERMERCADOS")


# In[35]:


Op3=list(abras_MG_4['Razão Social'])
Op3.append("TODOS OS SUPERMERCADOS (MG)")


# In[36]:


#mapasMG
import plotly.offline as pyo
import plotly.express as px
import json
import dash_table
from dash_table.Format import Format, Group, Scheme, Symbol


# In[37]:


#mapa top4 MG-Lojas
df_mg=pd.read_excel('Cidades Supermercados MG_2.xlsx')


# In[38]:


with open('geojs-31-mun.json',encoding='utf-8') as data:
    limites_MG = json.load(data)
for feature in limites_MG ['features']: 
    feature['id'] = feature['properties']['name']


# In[39]:


map_MG = px.choropleth_mapbox(df_mg,locations = 'cidade', 
                           geojson= limites_MG, 
                           color='total_lojas',
                           mapbox_style = "carto-darkmatter",
                           center = {'lon':-44.38, 'lat':-18.1},
                           zoom=5,
                           opacity=0.5, 
                            template="cyborg",
                              range_color = [1, df_mg['total_lojas'].max()])
map_MG.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# In[40]:


df_mg_2=df_mg[['cidade','total_lojas','sup_bh','grupo_dma','mart_minas','grupo_bahamas']]


# In[41]:


df_mg_2=df_mg_2.dropna()


# In[21]:


df_mg_2


# In[42]:


tab_MG =go.Figure(data=[go.Table(
    header=dict(values=list(df_mg_2.columns)),
    cells=dict(values=[df_mg_2.cidade,df_mg_2.total_lojas,df_mg_2.sup_bh, df_mg_2.grupo_dma, df_mg_2.mart_minas,df_mg_2.grupo_bahamas])),
                       ])


# In[43]:


#pyo.offline.plot(map_MG, filename = "mapaMGsup-1.html")


# In[44]:


#mapa sup BH
df_BH=pd.read_excel('Supermercados BH em MG.xlsx')


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


df_BH_2=df_BH[['cidade','Supermercados BH']]


# In[47]:


tab_BH =go.Figure(data=[go.Table(
    header=dict(values=list(df_BH_2.columns)),
    cells=dict(values=[df_mg_2.cidade,df_mg_2.sup_bh])),
                       ])


# In[48]:


#pyo.offline.plot(map_BH, filename = "mapaBHsup-1.html")


# In[49]:


#mapa DMA
df_DMA=pd.read_excel('Grupo DMA em MG.xlsx')


# In[50]:


map_DMA = px.choropleth_mapbox(df_DMA,locations = 'cidade', 
                           geojson= limites_MG, 
                           color='Grupo DMA',
                           mapbox_style = "carto-darkmatter",
                           center = {'lon':-44.38, 'lat':-18.1},
                           zoom=5,
                           opacity=0.5, range_color = [1, df_DMA['Grupo DMA'].max()])
map_DMA.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) 


# In[51]:


#pyo.offline.plot(map_DMA, filename = "mapaDMAsup-1.html")


# In[52]:


df_DMA_2=df_DMA[['cidade','Grupo DMA']]


# In[53]:


tab_DMA =go.Figure(data=[go.Table(
    header=dict(values=list(df_DMA_2.columns)),
    cells=dict(values=[df_mg_2.cidade,df_mg_2.grupo_dma])),
                       ])


# In[54]:


#mapa Mart Minas
df_MM=pd.read_excel('Mart Minas em MG.xlsx')


# In[55]:


map_MM = px.choropleth_mapbox(df_MM,locations = 'cidade', 
                           geojson= limites_MG, 
                           color='Mart Minas',
                           mapbox_style = "carto-darkmatter",
                           center = {'lon':-44.38, 'lat':-18.1},
                           zoom=5,
                           opacity=0.5, range_color = [1, df_MM['Mart Minas'].max()])
map_MM.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) 


# In[56]:


#pyo.offline.plot(map_MM, filename = "mapaMartMinassup-1.html")


# In[57]:


df_MM_2=df_MM[['cidade','Mart Minas']]


# In[58]:


tab_MM =go.Figure(data=[go.Table(
    header=dict(values=list(df_MM_2.columns)),
    cells=dict(values=[df_mg_2.cidade,df_mg_2.mart_minas])),
                       ])


# In[59]:


#mapa Bahamas
df_Bahamas=pd.read_excel('Grupo Bahamas em MG.xlsx')


# In[60]:


map_Bahamas = px.choropleth_mapbox(df_Bahamas,locations = 'cidade', 
                           geojson= limites_MG, 
                           color='Grupo Bahamas',
                           mapbox_style = "carto-darkmatter",
                           center = {'lon':-44.38, 'lat':-18.1},
                           zoom=5,
                           opacity=0.5, range_color = [1, df_Bahamas['Grupo Bahamas'].max()])
map_Bahamas.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) 


# In[61]:


#pyo.offline.plot(map_Bahamas, filename = "mapaBahamas-1.html") 


# In[62]:


df_Bahamas_2=df_Bahamas[['cidade','Grupo Bahamas']]


# In[63]:


tab_Bahamas =go.Figure(data=[go.Table(
    header=dict(values=list(df_Bahamas_2.columns)),
    cells=dict(values=[df_mg_2.cidade,df_mg_2.grupo_bahamas])),
                       ])


# In[ ]:





# In[64]:


#AREA NACIONAL
grid = html.Div(children=[
    html.Div(style = {'paddingTop': '25px','paddingBottom': '25px'}, children= [#div do titulo
        dbc.Row(
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
        dbc.Col(
            dcc.Dropdown(Op, value='TODAS AS SEDES', id='lista_lojas'),
            )),
        dbc.Row([
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
    
    
     #AREA MG
    
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
      html.Div(children=[
      html.Div(style = {'textAlign': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row(
            dbc.Col(
                html.H6(children='Grupo DMA'))),
         ]), 
    html.Div(style = {'align': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row([
            dbc.Col(
            dcc.Graph(id = 'mapa_DMA', figure=map_DMA),width = 7),
            dbc.Col(
                    dcc.Graph(id = 'table-DMA',figure=tab_DMA),width = 5),
    
]),
    ]),
]),
     
         html.Div(children=[
         html.Div(style = {'textAlign': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row(
            dbc.Col(
                html.H6(children='Mart Minas'))),
         ]), 
    html.Div(style = {'align': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row([
            dbc.Col(
            dcc.Graph(id = 'mapa_MM', figure=map_MM),width = 7),
            dbc.Col(
                    dcc.Graph(id = 'table-MM',figure=tab_MM),width = 5),
    
]),
    ]),
]),
     
        html.Div(children=[
        html.Div(style = {'textAlign': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row(
            dbc.Col(
                html.H6(children='Grupo Bahamas'))),
         ]), 
    html.Div(style = {'align': 'center', 'paddingTop': '40px', 'paddingBottom': '40px'},children=[
        dbc.Row([
            dbc.Col(
            dcc.Graph(id = 'mapa_Bahamas', figure=map_Bahamas),width = 7),
            dbc.Col(
                    dcc.Graph(id = 'table-Bahamas',figure=tab_Bahamas),width = 5),
    
]),
    ]),
]),       
        
])

   #FINAL PRIMEIRA DIV GERAL


# In[65]:


app.layout = html.Div(
    [
        dbc.Container(
            [       
                grid
            ]
        )
    ]
)

             
@app.callback(
    Output('Supermercados Nacionais no ranking ABRAS - Nº de lojas', 'figure'),
    Input('lista_lojas', 'value'))

def update_grafico1(value):
    if value == "TODAS AS SEDES":
        fig = px.bar(df_dash, x="Sede", y="Nº de lojas",color="Razão Social",template="cyborg")
    else:
        tab_filt=df_dash.loc[df_dash["Sede"]==value,:]
        fig = px.bar(tab_filt, x="Sede", y="Nº de lojas",color="Razão Social",template="cyborg")
    return fig

@app.callback(
    Output('Supermercados Nacionais no ranking ABRAS - Faturamento Bruto em 2020 (R$)', 'figure'),
    Input('lista_fat', 'value'))

def update_grafico2(value):
    if value == "TODOS OS SUPERMERCADOS":
        fig2 = px.bar(df_dash, x="Sede", y="Faturamento Bruto em 2020 (R$)",color="Razão Social",template="cyborg")
    else:
        tab_filt2=df_dash.loc[df_dash["Razão Social"]==value,:]
        fig2 = px.bar(tab_filt2, x="Sede", y="Faturamento Bruto em 2020 (R$)",color="Razão Social",template="cyborg")
    return fig2

@app.callback(
    Output('Top 4 Supermercados de Minas Gerais no ranking ABRAS - Nº de Lojas', 'figure'),
    Input('lista_MG_4', 'value'))

def update_grafico3(value):
    if value == "TODOS OS SUPERMERCADOS (MG)":
        fig3 = px.bar(abras_MG_4, x="Sede", y="Nº de lojas",color="Razão Social",template="cyborg")
    else:
        tab_filt3=abras_MG_4.loc[abras_MG_4["Razão Social"]==value,:]
        fig3 = px.bar(tab_filt3, x="Sede", y="Nº de lojas",color="Razão Social",template="cyborg")
    return fig3


# In[ ]:


if __name__ == '__main__':
    app.run_server(debug=False, use_reloader = False)


# In[ ]:





# In[ ]:




