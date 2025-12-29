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
    "This dashboard provides a clear and meaningful visualization of student performance "
    "based on the Math Education dataset."
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
# Dataset Overview
# =========================
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

st.markdown("---")

# =========================
# Distribution of Type of Answer (Percentages)
# =========================
st.subheader("📌 Distribution of Type of Answer")

type_percentage = df["Type of Answer"].value_counts(normalize=True) * 100

st.bar_chart(type_percentage)

st.write(
    "This chart shows the percentage of correct (1) and incorrect (0) answers. "
    "Percentages are used instead of raw counts to improve clarity for large datasets."
)

st.markdown("---")

# =========================
# Boxplot: Final Grade vs Type of Answer
# =========================
st.subheader("📦 Final Grade Distribution by Type of Answer")

fig, ax = plt.subplots(figsize=(6, 4))

df.boxplot(
    column="G3",
    by="Type of Answer",
    ax=ax
)

ax.set_xlabel("Type of Answer (0 = Incorrect, 1 = Correct)")
ax.set_ylabel("Final Grade (G3)")
ax.set_title("Final Grade vs Type of Answer")
plt.suptitle("")

st.pyplot(fig)

st.write(
    "The boxplot compares the distribution of final grades based on the type of answer. "
    "This visualization helps assess whether correct answers are associated with higher academic performance."
)

st.markdown("---")

# =========================
# Summary Statistics
# =========================
st.subheader("📊 Final Grade Summary Statistics")
st.write(df["G3"].describe())

# =========================
# Footer
# =========================
st.markdown(
    "📘 **Note:** Binary features such as *Type of Answer* are best visualized using "
    "aggregated or comparative plots rather than raw-value charts."
)
