import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Math Dashboard", layout="wide")

st.title("📊 Math Students Performance Dashboard")
st.markdown("Interactive exploratory analysis of students performance data.")

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

st.subheader("Dataset Preview")
st.dataframe(df.head())

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
feature = st.selectbox("Select a numeric feature", numeric_cols)

# Histogram
st.subheader("Histogram")
fig, ax = plt.subplots()
ax.hist(df[feature].dropna(), bins=10)
ax.set_xlabel(feature)
ax.set_ylabel("Count")
ax.set_title(f"Distribution of {feature}")
st.pyplot(fig)

# Boxplot
st.subheader("Boxplot")
fig, ax = plt.subplots()
ax.boxplot(df[feature].dropna(), vert=False)
ax.set_title(f"Boxplot of {feature}")
st.pyplot(fig)

# Feature vs Target
if "G3" in df.columns:
    st.subheader("Feature vs Final Grade (G3)")
    fig, ax = plt.subplots()
    ax.scatter(df[feature], df["G3"])
    ax.set_xlabel(feature)
    ax.set_ylabel("Final Grade (G3)")
    ax.set_title(f"{feature} vs G3")
    st.pyplot(fig)

st.subheader("Distribution of Type of Answer")
type_counts = df["Type of Answer"].value_counts(normalize=True) * 100
st.bar_chart(type_counts)


# Model results
st.markdown("---")
st.subheader("Model Performance Comparison")

results_df = pd.DataFrame({
    "Model": ["Logistic Regression", "SVM", "Random Forest"],
    "Accuracy": [0.78, 0.79, 0.80],
    "F1-score": [0.77, 0.78, 0.80]
})

st.dataframe(results_df)
st.bar_chart(results_df.set_index("Model"))
