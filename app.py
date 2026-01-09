import streamlit as st
from analysis import load_data, compute_price_stats, filter_small_units
from visuals import plot_price_distribution, plot_capacity

df = load_data("airbnb_tp.csv")

st.title("Dashboard Airbnb")

median_price, mean_price = compute_price_stats(df)
st.metric("Prix médian par personne", f"{median_price:.2f} €")

st.pyplot(plot_price_distribution(df))
st.pyplot(plot_capacity(df))
