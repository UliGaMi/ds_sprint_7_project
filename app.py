import pandas as pd
import plotly.graph_objects as go 
import streamlit as st

car_data = pd.read_csv('./datasets/vehicles_data.csv')

st.title("Análisis de Datos de Vehículos 🚗")

hist_button = st.checkbox('Construir un histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    fig.update_layout(title_text='Distribución del Odómetro')

    st.plotly_chart(fig, use_container_width=True)



scatter_button = st.checkbox('Construir un Scatter Plot')

if scatter_button:
    st.write('Creación de un Scatter Plot para ver la relación entre el precio y el odómetro')

    fig_2 = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig_2.update_layout(title_text='Relación entre Odómetro y Precio')

    fig_2.update_layout(title_text='Distribución del Odómetro')

    st.plotly_chart(fig_2, use_container_width=True)