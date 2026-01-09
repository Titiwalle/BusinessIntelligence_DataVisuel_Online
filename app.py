import streamlit as st
from analysis import load_data, compute_price_stats, filter_small_units
from visuals import plot_price_distribution, plot_capacity

df = load_data("airbnb_tp.csv")

st.title("Dashboard Airbnb")

tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Analyses", "🗂 A définir"])

with tab1:
    st.header("📊 Overview")
    median_price, mean_price = compute_price_stats(df)
    st.metric("Prix médian par personne", f"{median_price:.2f} €")

with tab2:
    st.header("Analyses")
    st.pyplot(plot_price_distribution(df))

with tab3:
    st.header("🗂 A définir")
    st.write("Ici tu mets tes analyses avancées…")
