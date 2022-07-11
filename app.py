import streamlit as st 
import pandas as pd 
import numpy as np
import seaborn as sns 

st.title("Sales KPI Dashboard with nice charts")

st.markdown('## Key Metrics')

col1, col2, col3 = st.columns(3)
col1.metric(label = "SPDR S&P 500", value = '%.2f' %200.12 , delta = "-$1.25")
col2.metric("FTEC", "$121.10", "0.46%")
col3.metric("BTC", "$46,583.91", "+4.87%")

st.markdown('## Detailed Charts')

chart1, chart2 = st.columns(2)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])



chart1.bar_chart(chart_data)
chart2.line_chart(chart_data)
