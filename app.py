import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Page configuration
# =========================
st.set_page_config(
    page_title="Math Students Performance Dashboard",
    layout="wide"
)

st.title("📊 Math Students Performance Dashboard")
st.write("This dashboard presents clear and meaningful visualizations of the Math Education dataset.")

# =========================
# Load data
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
# Dataset preview
# =========================
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# =========================
# Distribution of Type of Answer
# =========================
st.subheader("📌 Distribution of Type of Answer")

type_counts = df["Type of Answer"].value_counts(normalize=True) * 100

st.bar_chart(type_counts)

st.write(
    "This bar chart shows the percentage distribution of correct (1) and incorrect (0) answers. "
    "Using proportions instead of raw counts improves clarity for large datasets."
)

# =========================
# Boxplot: Final Grade vs Type of Answer
# =========================
st.subheader("📈 Final Grade vs Type of Answer")

fig, ax = plt.subplots(figsize=(6, 4))

df.boxplot(
    column="G3",
    by="Type of Answer",
    ax=ax
)

ax.set_title("Final Grade Distribution by Type of Answer")
ax.set_xlabel("Type of Answer (0 = Incorrect, 1 = Correct)")
ax.set_ylabel("Final Grade")
plt.suptitle("")

st.pyplot(fig)

st.write(
    "The boxplot highlights the relationship between students' final grades and their type of answer. "
    "This visualization helps assess whether correct answers are associated with higher academic performance."
)

# =========================
# Summary statistics
# =========================
st.subheader("📊 Final Grade Statistics")

st.write(df["G3"].describe())

# =========================
# Footer
# =========================
st.markdown("---")
st.markdown(
    "📘 **Note:** Visualizations were selected to avoid overplotting and ensure interpretability for binary and large-scale data."
)
