import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

lat = [60.5267, 60.5018, 60.4141, 60.2367, 60.1452, 60.13, 60.0699, 60.0041, 59.9917, 59.9367, 59.8916, 59.9, 59.6633,
       59.3981, 59.2167, 58.825, 56.5241, 56.3384, 56.25, 55.6667, 55.5933, 55.0866, 54.7861, 54.5597, 54.5086, 54.3809,
       54.3574, 54.3512, 54.2894, 54.2354, 54.2117, 54.1948, 54.1607, 54.1468, 54.1398]

lon = [28.0733, 28.0898, 28.0547, 27.8032, 27.4783, 26.9532, 26.673, 26.2917, 26.125, 25.97, 25.3666, 25.0333, 24.0333,
       22.1672, 21.2, 20.4217, 18.7936, 18.57, 18.1134, 16.4717, 16.4633, 15.9249, 15.2533, 14.1674, 14.016, 13.8041,
       13.8009, 13.7895, 13.7806, 13.7081, 13.707, 13.6325, 13.633, 13.6398]

# fill data
mean_temp, std = 7.0, 4
temperatures = np.random.normal(mean_temp, std, len(lat))

st.title("Технология обнаружения утечек в трубопроводах")

# Заголовок
st.header("Новая технология для обнаружения утечек в трубопроводах")

# Подзаголовок
st.subheader("Мы используем датчики температуры вдоль трубы для передачи данных на сервер для обработки")

# Текст в формате markdown
st.markdown(
    "Наша система использует микроконтроллеры с Bluetooth и доступом к радио, а также батарейную систему с "
    "возможностью заряда. Эта технология позволит нам быстро и эффективно обнаруживать утечки, что сэкономит время и "
    "деньги на ремонт и предотвратит негативный влияние на окружающую среду.")

if st.button('Запустить моделирование', help="Запустить моделирование"):
    fig = go.Figure(
        go.Scattermapbox(
            name="<b>Северный поток - 1</b>",
            lat=lat,
            lon=lon,
            mode='lines+markers',
            line=dict(width=1, color='black'),
            marker=dict(
                color=["red" if abs(temp - temperatures.mean()) > std else "green" for temp in temperatures],
                size=10,
                symbol='circle'
            ),
            text=[f'Датчик {i}\nТемпература {temperatures[i]}' for i in range(len(temperatures))]
        )
    )

    fig.update_layout(
        mapbox_style="open-street-map",
        title='Россия',
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    st.plotly_chart(fig, use_container_width=True)
