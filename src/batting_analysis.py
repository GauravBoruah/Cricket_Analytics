# This section calculates:

# - Top Batsmen
# - Batting Average
# - Strike Rate
# - Boundary Percentage
import pandas as pd

df  = pd.read_csv("../data/cleaned_data.csv")

# Top 10 run scorer
def top_batsmen(df):

    batsmen = df.groupby("Player")["Runs"].sum()

    batsmen = batsmen.sort_values(ascending=False).head(10)

    return batsmen.head(10)

# Top 10 players with best batting average
def batting_average(df):

    average = df.groupby("Player")["Runs"].mean()

    average = average.sort_values(ascending=False).head(10)

    return average.head(10)

# Top 10 players with best strike rate
def strike_rate(df):

    strike_rate = df.groupby("Player")["Strike_Rate"].mean()

    strike_rate = strike_rate.sort_values(ascending=False).head(10)

    return (strike_rate).head(10)


# Top 10 players with best boundary percentage
def boundary_percentage(df):

    df["Boundary_Runs"] = 4 * df["Fours"] + 6 * df["Sixes"]

    result = df.groupby("Player")[["Runs", "Boundary_Runs"]].sum()

    result["Boundary_Percentage"] = (result["Boundary_Runs"] / result["Runs"] ) * 100

    result = result[["Boundary_Percentage"]]

    result = result.sort_values(
        by="Boundary_Percentage",
        ascending=False
        ).head(10)

    return result.head(10)