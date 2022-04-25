<h2 align="center"> Analise de dados dos principais supermercados de Minas Gerais </h2> 

Aqui eu utilizei dados da ABRAS, dos supermercados BH, DMA, Mart Minas e Bahamas para analisar através de técnicas estatísticas, gráficos e mapa, a concentração das suas lojas em Minas Gerais e a realção entre o número de lojas e a receita bruta no ano de 2020.

![Lucas Lopes - Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Lucas Lopes - Jupyter](https://img.shields.io/badge/Jupyter-black?style=for-the-badge&logo=Jupyter)

![Lucas Lopes - Pandas](https://img.shields.io/badge/-Pandas-9cf?style=for-the-badge&logo=Pandas)
![Lucas Lopes - Numpy](https://img.shields.io/badge/-Numpy-blue?style=for-the-badge&logo=Numpy)
![Lucas Lopes - folium](https://img.shields.io/badge/-folium-black?style=for-the-badge&logo=folium)
![Lucas Lopes - matplotlib](https://img.shields.io/badge/-matplotlib-blue?style=for-the-badge&logo=matplotlib)
![Lucas Lopes - sklearn](https://img.shields.io/badge/-sklearn-green?style=for-the-badge&logo=sklearn)
![Lucas Lopes - seaborn](https://img.shields.io/badge/-seaborn-black?style=for-the-badge&logo=seaborn)
![Lucas Lopes - scipy stats](https://img.shields.io/badge/-scipystats-9cf?style=for-the-badge&logo=scipystats)
![Lucas Lopes - excel](https://img.shields.io/badge/-Excel-green?style=for-the-badge&logo=Excel)


<h2>📊 Alguns insights: </h2> 

<b> Vou listrar alguns isnights mais simples...</b>

1. Usando todas as informações referentes ao número de lojas e ao faturamento bruto de todos os rows do ranking da ABRAS, o coeficiente de determinação fica consideravelmente baixo (R²=0.241), isso acontece pois há a necessidade de manipular e filtrar os dados com foco na "raiz" do que queremos analizar. Desta forma decidi filtrar por estado (uf).
2. Manipulando o ranking para que somente os supermercados de MG sejam levados em conta, há uma grande melhora no coeficiente de deteminação (R²=0.912) usando a mesma comparação y= Numero de lojas e x= Faturamento Bruto em 2020.
3. É interessante notar que a linha de tendência é crescente, mostrando que a quantidade há relação positiva entre os as variáveis.
4. Outro ponto é que, quando x= 0, y aumenta em 0.714.
5. A grande maioria dos pontos ficou concentrado proximo ao ponto inicial da linha de tendência (e na "base" do boxplot) indicando uma concentração, onde a maioria dos mercados ten menos que 50 e um faturamento bruto menor ate que 1.000.000.000.
6. Existem outliers perceptiveis na linha de tendência e no boxplot, e esses são o foco dessa analise - BH, DMA, Bahamas,Mart Minas e Super Nosso (esse ultimo não entrou pois não a dados facilmente disponiveis).
7. Na matriz de correlação vemos que há associação muito forte entre as variaveis x e y quando levamos em conta todos os dados.
8. Nos gráficos de barra, vemos que as duas maiores redes se mantem firmes na relação numero de lojas e faturamento, quanto as duas ultimas invertem suas posições, ou seja, o Mart Minas fatura mais que o Bahamas mesmo tendo menos lojas - um fator para isso é, por exemplo, a concetração de lojas nos grandes centros urbanos de MG (como veremos no mapa)-
9. Na descrição das estatisticas vemos que 75% dos dados são menores que ou iguais aos valores determinados para cada variavel, o valor minimo de lojas é 40 e de faturamento bruto é de mais de 2.000.000.000, mostrando a força e o tamanho dessas redes.
10. Podemos então perceber que, levando em conta todos de MG, há muitos mercados com apenas uma loja (e que estão ranqueados).
11. Logo, vemos no grafico que há uma enorme concentração das top 4 redes nas regiões  Central,Centro-oeste, Zona da Mata, Sul de Minas e na região do Rio doce, e isso pode ser explicado pela exitencia de grandes centros urbanos e industriais e pela circulação de renda.

<b> QUER MAIS INSIGHTS OU TROCAR AQUELA IDÉIA SOBRE? PODE ME CHAMAR </b>

<a href="https://www.linkedin.com/in/lucas-lopes-br/" alt="linkedin" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=flat-square&logo=linkedin&logoColor=white"></a> 
<a href="https://wa.me/5532998342365" alt="WhatsApp" target="_blank"><img src="https://img.shields.io/badge/-WhatsApp-25d366?style=flat-square&labelColor=25d366&logo=whatsapp&logoColor=white&link=https://wa.me/5584981430120"/></a>
<a href="mailto:lucas.aguiarlopes26@gmail.com" alt="gmail" target="_blank"><img src="https://img.shields.io/badge/-Gmail-FF0000?style=flat-square&labelColor=FF0000&logo=gmail&logoColor=white&link=mailto:tassiofernandescosta@gmail.com" /></a>




Made with 💖 by Lucas Lopes
