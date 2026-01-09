import streamlit as st
from analysis import load_data, compute_price_stats, filter_small_units
from visuals import plot_price_distribution, plot_capacity

df = load_data("airbnb_tp.csv")

st.title("Dashboard Airbnb")

median_price, mean_price = compute_price_stats(df)
st.metric("Prix médian par personne", f"{median_price:.2f} €")

st.pyplot(plot_price_distribution(df))
st.pyplot(plot_capacity(df))



# -----------------------------
# CONFIGURATION DE LA PAGE
# -----------------------------
st.set_page_config(
    page_title="Dashboard Airbnb",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("📁 Navigation")
page = st.sidebar.radio("Aller vers :", ["Accueil", "Graphiques", "Analyse avancée"])

st.sidebar.markdown("---")
st.sidebar.write("🔧 Options globales")
theme = st.sidebar.selectbox("Thème graphique", ["Seaborn", "Matplotlib"])

# -----------------------------
# PAGE : ACCUEIL
# -----------------------------
if page == "Accueil":
    st.title("📊 Dashboard Airbnb – Visualisations personnalisées")
    st.markdown("""
    Bienvenue dans ton espace de visualisation Streamlit.  
    Tu peux intégrer **tes propres graphiques**, explorer ton dataset,  
    et construire un vrai tableau de bord interactif.
    
    Utilise le menu à gauche pour naviguer.
    """)

# -----------------------------
# PAGE : GRAPHIQUES
# -----------------------------
elif page == "Graphiques":
    st.title("📈 Visualisations")

    uploaded_file = st.file_uploader("📥 Importer un fichier CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("Dataset chargé avec succès !")

        st.subheader("Aperçu du dataset")
        st.dataframe(df.head())

        st.markdown("---")

        # Choix des colonnes
        st.subheader("Créer un graphique")
        numeric_cols = df.select_dtypes(include=["int", "float"]).columns.tolist()

        col_x = st.selectbox("Axe X", numeric_cols)
        col_y = st.selectbox("Axe Y", numeric_cols)

        graph_type = st.radio("Type de graphique :", ["Histogramme", "Scatterplot", "Boxplot"])

        # Génération du graphique
        fig, ax = plt.subplots(figsize=(8, 4))

        if graph_type == "Histogramme":
            sns.histplot(df[col_x], kde=True, ax=ax)
            ax.set_title(f"Histogramme de {col_x}")

        elif graph_type == "Scatterplot":
            sns.scatterplot(x=df[col_x], y=df[col_y], ax=ax)
            ax.set_title(f"Scatterplot : {col_x} vs {col_y}")

        elif graph_type == "Boxplot":
            sns.boxplot(y=df[col_x], ax=ax)
            ax.set_title(f"Boxplot de {col_x}")

        st.pyplot(fig)

    else:
        st.info("💡 Importer un fichier CSV pour commencer.")

# -----------------------------
# PAGE : ANALYSE AVANCÉE
# -----------------------------
elif page == "Analyse avancée":
    st.title("🧠 Analyse avancée")
    st.markdown("""
    Ici, tu pourras intégrer :
    - des heatmaps  
    - des corrélations  
    - des modèles ML  
    - des cartes géographiques  
    - des analyses personnalisées  
    """)

    st.info("Ajoute ici tes propres fonctions d'analyse !")