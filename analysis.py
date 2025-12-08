"""
analysis.py

This script loads quarterback statistics from CSV files, computes additional efficiency
metrics, displays rankings, and generates five visualizations relevant to evaluating
Drake Maye against peer quarterbacks and the league's top 5 quarterbacks.

Data sources:
data/qb_stats.csv        (Drake Maye + peer quarterback group)
data/qb_stats_top5.csv   (Drake Maye + top 5 quarterbacks through Week 13, 2025)

Output:
Printed rankings
Visualizations displayed using matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt


# ================================
# Data Loading
# ================================

# Load CSV files from the data directory
qb_peers = pd.read_csv("data/qb_stats.csv")
qb_top5 = pd.read_csv("data/qb_stats_top5.csv")


# ================================
# Metric Computation
# ================================

def compute_metrics(df):
    """
    Compute additional quarterback metrics:
    YPA (Yards per Attempt)
    TD_per_Att (Touchdowns per Attempt)

    Parameters:
    df (pd.DataFrame): DataFrame containing Attempts, Yards, Touchdowns.

    Returns:
    pd.DataFrame: Updated DataFrame with new metric columns.
    """
    df['YPA'] = df['Yards'] / df['Attempts']
    df['TD_per_Att'] = df['Touchdowns'] / df['Attempts']
    return df


# Apply computed metrics to datasets
qb_peers = compute_metrics(qb_peers)
qb_top5 = compute_metrics(qb_top5)


# ================================
# Display Rankings
# ================================

def display_ranking(df, column, title):
    """
    Display quarterback rankings sorted by a chosen metric.

    Parameters:
    df (pd.DataFrame): DataFrame containing Player names and metrics.
    column (str): Column name to sort on.
    title (str): User-friendly title to display.
    """
    print(f"\nRanking by {title}:\n")
    ranked = df.sort_values(by=column, ascending=False)
    print(ranked[['Player', column]])


print("Peer Group Comparison:")
display_ranking(qb_peers, 'CompletionPct', 'Completion Percentage')
display_ranking(qb_peers, 'YPA', 'Yards per Attempt')
display_ranking(qb_peers, 'TD_per_Att', 'Touchdowns per Attempt')

print("\nTop 5 Quarterbacks Comparison:")
display_ranking(qb_top5, 'CompletionPct', 'Completion Percentage')
display_ranking(qb_top5, 'YPA', 'Yards per Attempt')
display_ranking(qb_top5, 'TD_per_Att', 'Touchdowns per Attempt')


# ================================
# Visualization Functions
# ================================

def plot_bar(df, column, title, ylabel):
    """
    Create a bar chart comparing quarterbacks on a specific metric.

    Parameters:
    df (pd.DataFrame): Dataset containing metrics.
    column (str): Metric to visualize.
    title (str): Title of the chart.
    ylabel (str): Y-axis label.
    """
    plt.figure(figsize=(8, 5))
    plt.bar(df['Player'], df[column], color='skyblue')
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_scatter(df, x_col, y_col, title):
    """
    Create a scatter plot comparing two metrics, labeling each QB.

    Parameters:
    df (pd.DataFrame): Dataset containing metrics.
    x_col (str): Column for x-axis.
    y_col (str): Column for y-axis.
    title (str): Plot title.
    """
    plt.figure(figsize=(8, 5))
    plt.scatter(df[x_col], df[y_col], color='green', s=100)

    # Annotate each point with player name
    for i, player in enumerate(df['Player']):
        plt.text(df[x_col][i] + 0.1, df[y_col][i] + 0.001, player)

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.tight_layout()
    plt.show()

==============================
# Generate Visualizations
==============================

# 1. Completion % Bar Chart
plot_bar(
    qb_top5,
    'CompletionPct',
    'Top 5 QBs: Completion Percentage',
    'Completion %'
)

# 2. YPA Bar Chart
plot_bar(
    qb_top5,
    'YPA',
    'Top 5 QBs: Yards per Attempt',
    'Yards per Attempt'
)

# 3. Touchdowns Bar Chart
plot_bar(
    qb_top5,
    'Touchdowns',
    'Top 5 QBs: Total Passing Touchdowns',
    'Touchdowns'
)

# 4. Scatter Plot: Completion % vs YPA
plot_scatter(
    qb_top5,
    'CompletionPct',
    'YPA',
    'Top 5 QBs: YPA vs Completion %'
)

# 5. Scatter Plot: YPA vs Touchdowns per Attempt
plot_scatter(
    qb_top5,
    'YPA',
    'TD_per_Att',
    'Top 5 QBs: TD per Attempt vs YPA'
)
