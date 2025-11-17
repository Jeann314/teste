import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('WHO_time_series.csv')

fig1 = px.line(df, x = 'Date_reported', y = 'Cumulative_cases', color = 'Country',
               title = 'Dados de COVID-19 no mundo - Ano 2020')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de casos acumulados', title_font_size = 30)
fig1.show()

df_brasil_usa = df.query('Country == "Brazil" or Country == "United States of America"')
fig2 = px.line(df_brasil_usa, x = 'Date_reported', y = 'Cumulative_cases', color = 'Country', title='Comparativo entre os casos acumulados de Brasil e USA')
fig2.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de casos acumulados')
fig2.show()

df_brasil_usa_india = df.query('Country == "Brazil" or Country == "United States of America" or Country == "India"')
fig3 = px.pie(df_brasil_usa_india, values = 'Cumulative_cases', names = 'Country', title = 'Comparativo entre os casos acumulados de Brasil, USA e Índia')
fig3.show()

st.title("DASHCOVID: Um Dashboard sobre os Dados de COVID-19 - 2020")

st.plotly_chart(fig1, use_container_width = True)
st.plotly_chart(fig2, use_container_width = True)
st.plotly_chart(fig3, use_container_width = True)
