import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Page Configuration
# =========================
st.set_page_config(
    page_title="Math Students Performance Dashboard",
    layout="centered"
)

st.title("📊 Math Students Performance Dashboard")
st.write(
    "This dashboard visualizes student performance data and compares "
    "machine learning model results in a clear and academic manner."
)

# =========================
# Load Dataset
# =========================
@st.cache_data
def load_data():
    return pd.read_csv(
        "MathEdataset.csv",
        sep=";",
        encoding="latin1",
        engine="python",
        on_bad_lines="skip"
    )

df = load_data()
st.success("Dataset loaded successfully ✅")

# =========================
# Dataset Preview
# =========================
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

st.markdown("---")

# =========================
# Identify Binary Features Automatically
# =========================
binary_features = [
    col for col in df.columns
    if
