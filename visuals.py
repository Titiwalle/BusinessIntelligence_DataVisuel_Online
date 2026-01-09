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
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df["price_per_person"], kde=True, ax=ax)
    ax.set_title("Distribution du prix par personne")
    return fig
