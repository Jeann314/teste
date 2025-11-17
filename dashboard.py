import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('WHO_time_series.csv')

fig1 = px.line(df, x = 'Date_reported', y = 'Cumulative_cases', color = 'Country',
               title = 'Dados de COVID-19 no mundo - Ano 2020')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de casos acumulados', title_font_size = 30)
fig1.show()

st.title("DASHCOVID: Um Dashboard sobre os Dados de COVID-19 - 2020")

st.plotly_chart(fig1, use_container_width = True)
