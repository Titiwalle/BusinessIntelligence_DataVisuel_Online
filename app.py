import streamlit as st
from analysis import load_data, compute_price_stats, filter_small_units
from visuals import plot_price_distribution, plot_capacity

df_clean = load_data("airbnb_tp_clean.csv")

st.set_page_config(layout="wide")

st.title("Dashboard Airbnb")

tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Analyses", "🗂 A définir"])

with tab1:
    st.subheader("Csv Clean")
    st.dataframe(df_clean)
    median_price, mean_price = compute_price_stats(df_clean)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Prix médian par personne", f"{median_price:.2f} €")

    with col2:
        st.metric("Prix moyen par personne", f"{mean_price:.2f} €")
    st.subheader("Dataset overview")
 
    col3.metric("Listings", len(df))

    col4.metric("Columns", df.shape[1])

    col5.metric("Missing values", df.isna().sum().sum())
 
    st.markdown("### Missing values (%)")
    missing = (df.isna().mean() * 100).sort_values(ascending=False)
    st.dataframe(missing.to_frame("Missing %"))
 
    st.markdown("### Numeric summary")
    st.dataframe(df.describe())


with tab2:
    st.subheader("Analyses")
    st.pyplot(plot_price_distribution(df_clean))
    st.pyplot(plot_capacity(df_clean))

with tab3:
    st.subheader("🗂 A définir")
    st.write("Ici tu mets tes analyses avancées…")
