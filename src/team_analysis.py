#This section calculates

# - Number of Wins of each Team
# - Teams With Best Run Rate
# - A Team Comparison

import pandas as pd

# To read the cleaned data
df = pd.read_csv("../data/cleaned_data.csv")

# Function to calculate team wins
def team_wins():

    # To count the number of wins of each team
    team_wins_count = df[df["Match_Result"] == "Win"].groupby("Team")["Match_ID"].nunique()

    team_wins_count = team_wins_count.sort_values(ascending=False)

    return team_wins_count


# Function to calculate team run rate
def team_run_rate():

    # To calculate total runs scored by each team
    total_runs = df.groupby("Team")["Runs"].sum()

    # To calculate total balls faced by each team
    total_balls = df.groupby("Team")["Balls_Faced"].sum()

    # To calculate run rate
    run_rate = (total_runs / total_balls) * 6

    run_rate = run_rate.sort_values(ascending=False)

    return run_rate


# Function to compare teams
def team_comparison():

    # To calculate total runs for each team
    total_runs = df.groupby("Team")["Runs"].sum()

    # To calculate total wickets for each team
    total_wickets = df.groupby("Team")["Wickets"].sum()

    # To calculate total matches played by each team
    total_matches = df.groupby("Team")["Match_ID"].nunique()

    # Create a team summary
    comparison = pd.DataFrame({
        "Total Runs": total_runs,
        "Total Wickets": total_wickets,
        "Total Matches": total_matches
    })

    # To sort teams by total runs
    comparison = comparison.sort_values(
        by="Total Runs",
        ascending=False
    )

    # To save team summary
    comparison.to_csv("team_summary.csv")

    return comparison

print("Team Summary file saved successfully.")

