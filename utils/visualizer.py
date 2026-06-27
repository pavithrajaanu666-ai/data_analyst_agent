import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def create_seaborn_distribution(df, column):
    """
    Generates a Seaborn distribution plot.
    """

    plt.close("all")  # Prevent duplicate figures

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.histplot(
        data=df,
        x=column,
        kde=True,
        ax=ax,
        color="steelblue"
    )

    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

    return fig


def create_plotly_scatter(df, x_col, y_col):
    """
    Generates an interactive Plotly scatter plot.
    """

    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        title=f"{y_col} vs {x_col}",
        template="plotly_white"
    )

    fig.update_layout(
        height=500
    )

    return fig