import streamlit as st
 
def apply_filters(df):
    st.sidebar.header("Filters")
 
    if "accommodates" in df.columns:
        mn, mx = int(df.accommodates.min()), int(df.accommodates.max())
        cap = st.sidebar.slider("Capacity", mn, mx, (mn, mx))
        df = df[df.accommodates.between(*cap)]
 
    if "price" in df.columns:
        pmin, pmax = int(df.price.min()), int(df.price.quantile(0.95))
        price = st.sidebar.slider("Price (€)", pmin, pmax, (pmin, pmax))
        df = df[df.price.between(*price)]
 
    if "amenities_count" in df.columns:
        acmin, acmax = int(df.amenities_count.min()), int(df.amenities_count.max())
        ac = st.sidebar.slider("Amenities count", acmin, acmax, (acmin, acmax))
        df = df[df.amenities_count.between(*ac)]
 
    if "bathrooms" in df.columns:
        bmin, bmax = int(df.bathrooms.min()), int(df.bathrooms.max())
        bath = st.sidebar.slider("Bathrooms", bmin, bmax, (bmin, bmax))
        df = df[df.bathrooms.between(*bath)]
 
    if "bedrooms" in df.columns:
        bmin, bmax = int(df.bedrooms.min()), int(df.bedrooms.max())
        bed = st.sidebar.slider("Bedrooms", bmin, bmax, (bmin, bmax))
        df = df[df.bedrooms.between(*bed)]
 
    if "Quarter_Or_City" in df.columns:
        options = sorted(df["Quarter_Or_City"].dropna().unique())

        selected = st.sidebar.multiselect(
            "Choisir un ou plusieurs quartiers",
            options,
            default=options  # tous sélectionnés par défaut
        )

        df = df[df["Quarter_Or_City"].isin(selected)]

    return df