# This section calculates:
#
# - Top Bowlers
# - Economy Rate
# - Bowling Average
import pandas as pd


# To read the csv file
df  = pd.read_csv("../data/cleaned_data.csv")


# Top 10 wicket takers
def top_bowlers(df):

    bowlers = df.groupby("Player")["Wickets"].sum()

    bowlers = bowlers.sort_values(ascending=False).head(10)

    return bowlers


# Top 10 player with best economy
def economy(df):

    eco = df.groupby("Player")["Economy"].mean()

    eco = eco[eco > 0]
  
    eco = eco.sort_values(ascending=True).head(10)

    return eco


# Top 10 players with best bowling economy
def bowling_average(df):

    df["Bowling_Average"] = df["Runs_Conceded"] / df["Wickets"]

    bowling_average = df[["Player", "Bowling_Average"]]

    bowling_average = bowling_average.sort_values(
        by="Bowling_Average",
        ascending=True
    ).head(10)

    return bowling_average
