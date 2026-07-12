import streamlit as st
from src import Dataset
from src.dashboard_blocks import show_dataset_block
from src.dashboard_blocks import show_metrics_block
from src.dashboard_blocks import show_charts_block
from src.dashboard_blocks import show_results_block

d = Dataset('data/')

st.title("Мониторинг продаж")
st.set_page_config(page_title="Мониторинг продаж", layout="wide")

show_dataset_block(d)
st.divider()
show_metrics_block(d)
st.divider()
show_charts_block(d)
st.divider()
show_results_block(d)


