import streamlit as st
from analysis import *
from visuals import *
from filters import apply_filters



df = load_data("airbnb_tp_clean.csv")
df_clean = apply_filters(df)

st.set_page_config(layout="wide")

st.title("Dashboard Airbnb")

tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Analyses", "🗂 A définir"])

with tab1:
    st.subheader("Csv Clean")
    st.dataframe(df_clean)
    median_price, mean_price = compute_price_stats(df_clean)

    st.subheader("Dataset overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Prix médian par personne", f"{median_price:.2f} €")

    col2.metric("Prix moyen par personne", f"{mean_price:.2f} €")
 
    col3.metric("Listings", len(df_clean))

    col4.metric("Columns", df_clean.shape[1])

    col5.metric("Missing values", df_clean.isna().sum().sum())
    
    st.markdown("### Numeric summary")
    st.dataframe(df_clean.describe())

    st.pyplot(heatmap(df_clean))

    st.markdown("### Missing values (%)")
    missing = (df_clean.isna().mean() * 100).sort_values(ascending=False)
    st.dataframe(missing.to_frame("Missing %"))
 

with tab2:
    st.subheader("Augmenter le taux d’occupation des logements accueillant 2 à 4 personnes de 70% à 80% au cours du prochain trimestre")
    st.pyplot(plot_capacity(df_clean))
    st.pyplot(plot_price_distribution(df_clean))

    st.subheader("Augmenter le prix médian par personne de 5% tout en maintenant une note moyenne de 4,7 ou plus dans les avis sur une période de six mois")
    st.pyplot(plot_dist_pricebyperson(df_clean))

    st.subheader("Réduire la proportion de logements offrant moins de 20 équipements à moins de 25% d’ici la fin de l’année")
    st.pyplot(plot_dist_equipements(df_clean))


with tab3:
    st.subheader("🗂 A définir")
    st.write("Ici tu mets tes analyses avancées…")
