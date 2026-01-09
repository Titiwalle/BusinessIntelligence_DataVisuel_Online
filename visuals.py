import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_distribution(df):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df["price_per_person"], kde=True, ax=ax)
    ax.set_title("Distribution du prix par personne")
    return fig

def plot_capacity(df):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.countplot(x=df["accommodates"], ax=ax)
    ax.set_title("Capacité d'accueil")
    return fig