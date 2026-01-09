import streamlit as st
from analysis import load_data, compute_price_stats, filter_small_units
from visuals import plot_price_distribution, plot_capacity

df_clean = load_data("airbnb_tp_clean.csv")

st.set_page_config(layout="wide")

st.title("Dashboard Airbnb")

tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Analyses", "🗂 A définir"])

with tab1:
    st.title("Csv Clean")
    st.dataframe(df_clean)
    median_price, mean_price = compute_price_stats(df_clean)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Prix médian par personne", f"{median_price:.2f} €")

    with col2:
        st.metric("Prix moyen par personne", f"{mean_price:.2f} €")


with tab2:
    st.title("Analyses")
    st.pyplot(plot_price_distribution(df_clean))
    st.pyplot(plot_capacity(df_clean))

with tab3:
    st.title("🗂 A définir")
    st.write("Ici tu mets tes analyses avancées…")
