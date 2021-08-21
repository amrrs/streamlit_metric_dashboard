import streamlit as st #web app 
import pandas as pd # data manipulation
import numpy as np # random gen

st.title("Marketing KPI - Key Metric Dashboard")

st.subheader("using Python 🚀 📈")


st.markdown("### Key Metrics")

kpi1, kpi2, kpi3 = st.columns(3)

my_dynamic_value = 333.3335 

new_val = 222

final_val = my_dynamic_value / new_val

kpi1.metric(label = "Avg Time Spent",
            value = 3.5,
            delta = -1.4)

kpi2.metric(label = "Bounce Rate",
            value = 78,
            delta = -5,
            delta_color = 'inverse')
kpi3.metric(label = "Unique Visitors",
            value = "%.2f" %final_val )

st.markdown("### Important Charts 📈")

chart1, chart2 = st.columns(2)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

chart1.bar_chart(chart_data)
chart2.line_chart(chart_data)

st.dataframe(chart_data)
