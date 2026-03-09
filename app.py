import streamlit as st
from etl_visualizer import etl_tool

st.set_page_config(
    page_title="Data Analytics Dashboard",
    layout="wide"
)

st.title("📊 Data Analytics Dashboard")
st.caption("ETL • Data Cleaning • Visualization")

# ✅ File uploader ONLY here
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"],
    key="main_file"
)

if uploaded_file:
    etl_tool(uploaded_file)
else:
    st.info("Please upload a CSV file to start analysis")