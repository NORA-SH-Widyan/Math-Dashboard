import streamlit as st
import pandas as pd

st.set_page_config(page_title="Math Dashboard", layout="wide")

st.title("📊 Math Students Performance Dashboard")

st.write("App started successfully ✅")

try:
    df = pd.read_csv(
        "MathEdataset.csv",
        sep=";",
        encoding="latin1",
        engine="python",
        on_bad_lines="skip"
    )

    st.success("Dataset loaded successfully")
    st.write("Shape:", df.shape)
    st.dataframe(df.head())

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) > 0:
        feature = st.selectbox("Select numeric feature", numeric_cols)
        st.bar_chart(df[feature])
    else:
        st.warning("No numeric columns found")

except Exception as e:
    st.error("Application error ❌")
    st.write(e)
