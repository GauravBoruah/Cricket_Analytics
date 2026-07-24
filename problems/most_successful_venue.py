# - This section shows the most successful venues
#
import pandas as pd

df = pd.read_csv("../data/cleaned_data.csv")

def most_successful_venue(df):

    wins = df[df["Match_Result"] == "Win"].groupby("Venue")["Match_ID"].nunique()

    wins = wins.sort_values(ascending=False)

    return wins

print("Most Successful Venues:")

print(most_successful_venue(df))
