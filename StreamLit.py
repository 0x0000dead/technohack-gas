import streamlit as st
import pandas as pd
import plotly.graph_objects as go
 
# set the app's title
st.title("Text Elements")
 
# header
st.header("Header in Streamlit")
 
# subheader
st.subheader("Subheader in Streamlit")
 
# markdown
# display text in bold formatting
st.markdown("Best Skolkovo project)")
# display text in italic formatting
st.markdown("info")
 
if st.button('Начать', help="Run simulation"):
    #   st.write('Загрузка...')
    fig = go.Figure(go.Scattergeo(
        #locations = ["Russia"],
        #locationmode = 'country names',
        name = "<b>Северный поток - 1</b>",
        lon = [28.0359 - 0.73*i*2 for i in range(10)]+[13.3923],
        lat = [60.3324 - 0.31*i*2 + 0.35*(i//5) for i in range(10)]+[54.0904],
        mode = 'lines+markers',
        line = dict(width = 1,color = 'black'),
        marker = dict(size = 10, color = 'green', symbol = 'circle'),
        text = [f'Датчик {i}' for i in range(1, 12)],
    ))

    fig.update_layout(
            title = 'Россия'
        )
    
    st.plotly_chart(fig, use_container_width=True)
