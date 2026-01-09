import matplotlib.pyplot as plt
import seaborn as sns

def plot_capacity(df):
    fig = plt.figure(figsize=(8,5))
    sns.countplot(x=df["accommodates"])
    plt.title("Distribution des capacités d'accueil")
    plt.xlabel("Nombre de personnes")
    plt.ylabel("Nombre de logements")
    plt.grid(axis="y")
    return fig

def plot_price_distribution(df):
    fig = plt.figure(figsize=(8,5))
    sns.histplot(df["review_score_average"], bins=20, kde=True)
    plt.title("Distribution des notes moyennes (logements 2–4 personnes)")
    plt.xlabel("Note moyenne")
    plt.ylabel("Nombre de logements")
    plt.grid(axis="y")
    return fig

def heatmap(df):
    cols = [
    "price", "accommodates", "bathrooms", "bedrooms", "num_beds",
    "rating_accuracy", "rating_cleanliness", "rating_communication",
    "rating_location", "rating_value", "review_score_average",
    "amenities_count"
]
    corr = df[cols].corr()
    fig = plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.show()
    return fig

def plot_dist_equipements(df):
    fig = plt.figure(figsize=(8,5))
    sns.histplot(df["amenities_count"], bins=30, kde=True)
    plt.axvline(20, color="red", linestyle="--", label="Seuil 20 équipements")
    plt.title("Distribution du nombre d'équipements")
    plt.xlabel("Nombre d'équipements")
    plt.ylabel("Nombre de logements")
    plt.legend()
    plt.grid(axis="y")
    return fig

def plot_dist_pricebyperson(df):
    fig = plt.figure(figsize=(8,5))
    sns.histplot(df["price_per_person"], bins=30, kde=True)
    plt.axvline(df["price_per_person"].median(), color="red", linestyle="--", label="Médiane actuelle")
    plt.title("Distribution du prix par personne")
    plt.xlabel("Prix par personne (€)")
    plt.ylabel("Nombre de logements")
    plt.legend()
    plt.grid(axis="y")
    return fig