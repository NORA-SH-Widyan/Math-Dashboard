import streamlit as st
import pandas as pd

st.set_page_config(page_title="Math Dashboard", layout="wide")

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

st.title("📊 Math Students Performance Dashboard")

st.subheader("Dataset Preview")
st.dataframe(df.head())

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

if len(numeric_cols) > 0:
    feature = st.selectbox("Select a numeric feature", numeric_cols)
    st.subheader(f"Distribution of {feature}")
    st.bar_chart(df[feature])
else:
    st.warning("No numeric columns found.")


