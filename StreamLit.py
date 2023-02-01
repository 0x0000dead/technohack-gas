import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(layout="wide")

lat = [60.5267, 60.5018, 60.4141, 60.2367, 60.1452, 60.13, 60.0699, 60.0041, 59.9917, 59.9367, 59.8916, 59.9, 59.6633,
       59.3981, 59.2167, 58.825, 56.5241, 56.3384, 56.25, 55.6667, 55.5933, 55.0866, 54.7861, 54.5597, 54.5086, 54.3809,
       54.3574, 54.3512, 54.2894, 54.2354, 54.2117, 54.1948, 54.1607, 54.1468, 54.1398]

lon = [28.0733, 28.0898, 28.0547, 27.8032, 27.4783, 26.9532, 26.673, 26.2917, 26.125, 25.97, 25.3666, 25.0333, 24.0333,
       22.1672, 21.2, 20.4217, 18.7936, 18.57, 18.1134, 16.4717, 16.4633, 15.9249, 15.2533, 14.1674, 14.016, 13.8041,
       13.8009, 13.7895, 13.7806, 13.7081, 13.707, 13.6325, 13.633, 13.6398]

lat_nsk = [54.859249, 54.858190, 54.849264,54.844629, 54.844280]
lon_nsk = [83.086347, 83.083929, 83.084680, 83.088186,83.092101 ]
# fill data
mean_temp, std = 8.0, 2
temperatures = np.random.normal(mean_temp, std, len(lat)).round(4)
temperatures1 = np.random.normal(20, std, len(lat_nsk)).round(4)

st.title("Система по контролю состояния трубопровода от команды Users")

st.markdown(
    "Разработанная система использует микроконтроллеры с передачей данных по Bluetooth, которые поступают на сервер, где происходит анализ и визуализация."
    "Разработанное решение позволит быстро и эффективно обнаруживать утечки, что сэкономит время и "
    "деньги на ремонт, а также предотвратит негативное влияние на окружающую среду.")

st.markdown("<b><h3>Получить актуальное состояние системы:</b></h3>", unsafe_allow_html=True)
import time
st.subheader("Интерактивная карта состояния Северного потока 2")
st_sever = st.empty()
st_nsk = st.empty()
first = True
while True:
    temperatures = np.random.normal(mean_temp, std, len(lat)).round(4)
    temperatures1 = np.random.normal(20, std, len(lat_nsk)).round(4)
    fig = go.Figure(
        go.Scattermapbox(
            name="<b>Северный поток - 2</b>",
            lat=lat,
            lon=lon,
            mode='lines+markers',
            line=dict(width=1, color='black'),
            marker=dict(
                color=["red" if abs(temp - temperatures.mean()) > std else "green" for temp in temperatures],
                size=10,
                symbol='circle'
            ),
            text=[f'Датчик {i} t = {temperatures[i]}' for i in range(len(temperatures))]
        )
    )
    fig.update_layout(
        mapbox_style="open-street-map",
        title='Россия',
        autosize=True,
        mapbox=dict(
            bearing=0,
            center=dict(
                lat=np.mean(lat),
                lon=np.mean(lon)
            ),
            pitch=0,
            zoom=4
        ),
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    st_sever.plotly_chart(fig, use_container_width=True)

    if first: st.subheader("Интерактивная карта состояния Новосибирского потока")
    fig = go.Figure(
        go.Scattermapbox(
            name="<b>Новосибирский поток</b>",
            lat=lat_nsk,
            lon=lon_nsk,
            mode='lines+markers',
            line=dict(width=1, color='black'),
            marker=dict(
                color=["red" if abs(temp - temperatures1.mean()) > std else "green" for temp in temperatures1],
                size=10,
                symbol='circle'
            ),
            text=[f'Датчик {i}\nТемпература {temperatures1[i]}' for i in range(len(temperatures1))]
        )
    )

    fig.update_layout(
        mapbox_style="open-street-map",
        title='Россия',
        autosize=True,
        mapbox=dict(
            bearing=0,
            center=dict(
                lat=np.mean(lat_nsk),
                lon=np.mean(lon_nsk)
            ),
            pitch=0,
            zoom=13
        ),
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    st_nsk.plotly_chart(fig, use_container_width=True)
    first = False
    time.sleep(2)
