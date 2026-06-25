import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Care Transition Analytics",
    layout="wide"
)

# Load Data
df = pd.read_csv("cleaned_uac.csv")

df['Date'] = pd.to_datetime(df['Date'])

st.title("Care Transition Efficiency & Placement Outcome Analytics")

# Sidebar Filter
st.sidebar.header("Filters")

start_date = st.sidebar.date_input(
    "Start Date",
    df['Date'].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df['Date'].max()
)

filtered_df = df[
    (df['Date'] >= pd.to_datetime(start_date))
    &
    (df['Date'] <= pd.to_datetime(end_date))
]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Transfer Efficiency",
    round(filtered_df['Transfer Efficiency Ratio'].mean(), 2)
)

col2.metric(
    "Discharge Effectiveness",
    round(filtered_df['Discharge Effectiveness Index'].mean(), 2)
)

col3.metric(
    "Pipeline Throughput",
    round(filtered_df['Pipeline Throughput Rate'].mean(), 2)
)

col4.metric(
    "Outcome Stability",
    round(filtered_df['Outcome Stability Score'].mean(), 2)
)

# Chart 1
st.subheader("Daily Apprehensions")

fig1 = px.line(
    filtered_df,
    x='Date',
    y='Children apprehended and placed in CBP custody*'
)

st.plotly_chart(fig1, use_container_width=True)

# Chart 2
st.subheader("Transfer Efficiency Ratio")

fig2 = px.line(
    filtered_df,
    x='Date',
    y='Transfer Efficiency Ratio'
)

st.plotly_chart(fig2, use_container_width=True)

# Chart 3
st.subheader("Discharge Effectiveness Index")

fig3 = px.line(
    filtered_df,
    x='Date',
    y='Discharge Effectiveness Index'
)

st.plotly_chart(fig3, use_container_width=True)

# Chart 4
st.subheader("CBP Backlog")

fig4 = px.line(
    filtered_df,
    x='Date',
    y='CBP Backlog'
)

st.plotly_chart(fig4, use_container_width=True)

# Chart 5
st.subheader("HHS Backlog")

fig5 = px.line(
    filtered_df,
    x='Date',
    y='HHS Backlog'
)

st.plotly_chart(fig5, use_container_width=True)