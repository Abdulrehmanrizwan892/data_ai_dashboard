import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def etl_tool(uploaded_file):
    df = pd.read_csv(uploaded_file)

    # 1️⃣ Extract
    st.subheader("1️⃣ Extract - Raw Data")
    st.dataframe(df, use_container_width=True)

    # 2️⃣ Transform
    clean_df = df.dropna()
    for col in clean_df.columns:
        clean_df[col] = pd.to_numeric(clean_df[col], errors="ignore")

    st.subheader("2️⃣ Transform - Cleaned Data")
    st.dataframe(clean_df, use_container_width=True)

    numeric_cols = clean_df.select_dtypes(include=["int64", "float64"]).columns
    if len(numeric_cols) == 0:
        st.warning("No numeric columns found.")
        return

    # 3️⃣ KPIs
    st.subheader("3️⃣ Key Metrics")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total", clean_df[numeric_cols[0]].sum())
    c2.metric("Max", clean_df[numeric_cols[0]].max())
    c3.metric("Min", clean_df[numeric_cols[0]].min())
    c4.metric("Rows", len(clean_df))

    # 4️⃣ Summary
    st.subheader("4️⃣ Load Summary")
    st.write(clean_df[numeric_cols].describe())

    # 5️⃣ Charts
    cat_cols = clean_df.select_dtypes(include=["object"]).columns
    if len(cat_cols) > 0:
        grp = clean_df.groupby(cat_cols[0])[numeric_cols[0]].sum()

        st.subheader("5️⃣ Bar Chart")
        st.bar_chart(grp)

        st.subheader("6️⃣ Pie Chart")
        fig, ax = plt.subplots()
        ax.pie(grp.values, labels=grp.index, autopct="%1.1f%%")
        st.pyplot(fig)