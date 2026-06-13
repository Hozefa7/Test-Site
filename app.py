import streamlit as st
import requests
import pandas as pd

# Load API key from secrets.toml
try:
    API_KEY = st.secrets["NEWS_API_KEY"]
except KeyError:
    st.error(
        "NEWS_API_KEY not found in .streamlit/secrets.toml"
    )
    st.stop()

BASE_URL = "https://newsapi.org/v2/top-headlines"

st.set_page_config(
    page_title="News Dashboard",
    page_icon="📰",
    layout="wide"
)