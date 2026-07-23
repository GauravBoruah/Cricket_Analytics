#This section shows

# - Bar plot for top 10 batsmen and bowlers
# - A Scatter plot between strike rate and runs
# - A Pie chart of team performance
# - A Histogram of distribution of players score
# - A Line graph of match-wise performance of any player

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned_data.csv")


# 1. Top 10 Batsmen - Bar Chart
def plot_bar_chart1(df):

    top_batsmen = df.groupby("Player")["Runs"].sum()
    top_batsmen = top_batsmen.sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    plt.bar(top_batsmen.index, top_batsmen.values)

    plt.title("Top 10 Batsmen")
    plt.xlabel("Player")
    plt.xticks(rotation=90)
    plt.ylabel("Total Runs")
    plt.grid()
    plt.tight_layout()

    plt.savefig("../figures/batting_ranking.png")
    plt.show()


# 2. Top 10 Bowlers - Bar Chart
def plot_bar_chart2(df):

    top_bowlers = df.groupby("Player")["Wickets"].sum()
    top_bowlers = top_bowlers.sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    plt.bar(top_bowlers.index, top_bowlers.values)

    plt.title("Top 10 Bowlers")
    plt.xlabel("Player")
    plt.xticks(rotation=90)
    plt.ylabel("Total Wickets")
    plt.grid()
    plt.tight_layout()

    plt.savefig("../figures/bowling_ranking.png")
    plt.show()


# 3. Runs vs Strike Rate - Scatter Plot
def plot_scatter_plot(df):

    plt.figure(figsize=(10, 6))
    plt.scatter(df["Runs"], df["Strike_Rate"])

    plt.title("Runs vs Strike Rate")
    plt.xlabel("Runs")
    plt.ylabel("Strike Rate")
    plt.grid()
    plt.tight_layout()

    plt.savefig("../figures/strike_rate_vs_runs.png")
    plt.show()


# 4. Team Performance - pie Chart
def plot_pie_chart(df):

    df["Runs"] = pd.to_numeric(df["Runs"])

    team_runs = df.groupby("Team")["Runs"].sum()

    plt.figure(figsize=(10, 6))
    plt.pie(team_runs.values,labels= team_runs.index,
            autopct="%1.1f%%")

    plt.title("Team Comparison Based on Total Runs")

    plt.tight_layout()

    plt.savefig("../figures/team_comparison.png")
    plt.show()

# 5. Distribution of Player Scores - Histogram
def plot_histogram(df):

    plt.figure(figsize=(8, 6))

    plt.hist(
        df["Runs"]
    )

    plt.title("Distribution of Player Scores")
    plt.xlabel("Runs")
    plt.ylabel("Frequency")
    plt.grid()
    plt.tight_layout()

    plt.savefig("../figures/player_score_distribution.png")
    plt.show()


# 6. Match-wise Performance of a Player - Line Graph
def plot_line_graph(df, player_name):

    player_data = df[df["Player"] == player_name]

    plt.figure(figsize=(8, 6))

    plt.plot(
        player_data["Match_ID"],
        player_data["Runs"],
        marker="o"
    )

    plt.title("Match-wise Performance of " + player_name)
    plt.xlabel("Match ID")
    plt.ylabel("Runs")
    plt.grid()
    plt.xticks(player_data["Match_ID"])

    plt.tight_layout()

    plt.savefig("../figures/player_performance.png")
    plt.show()

