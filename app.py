import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
feature = st.selectbox("Select a numeric feature", numeric_cols)

st.subheader("Histogram")

fig, ax = plt.subplots()
ax.hist(df[feature].dropna(), bins=10)
ax.set_xlabel(feature)
ax.set_ylabel("Count")
ax.set_title(f"Distribution of {feature}")

st.pyplot(fig)

st.subheader("Boxplot")
fig, ax = plt.subplots()
ax.boxplot(df[feature].dropna(), vert=False)
ax.set_title(f"Boxplot of {feature}")

st.pyplot(fig)


if "G3" in df.columns:
    st.subheader("Feature vs Final Grade (G3)")

    fig, ax = plt.subplots()
    ax.scatter(df[feature], df["G3"])
    ax.set_xlabel(feature)
    ax.set_ylabel("Final Grade (G3)")
    ax.set_title(f"{feature} vs G3")

    st.pyplot(fig)

st.markdown("---")
st.subheader("Model Performance Comparison")

results_df = pd.DataFrame({
    "Model": ["Logistic Regression", "SVM", "Random Forest"],
    "Accuracy": [0.78, 0.79, 0.80],
    "F1-score": [0.77, 0.78, 0.80]
})

st.dataframe(results_df)


st.bar_chart(results_df.set_index("Model"))




