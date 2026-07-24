# - This section shows the most successful venues
#
import pandas as pd

df = pd.read_csv("../data/cleaned_data.csv")

def most_successful_venue(df):

    venue_wins = df[df["Match_Result"] == "Win"].groupby("Venue")["Match_ID"].nunique()

    venue_wins = venue_wins.sort_values(ascending=False)

    return venue_wins

print("Most Successful Venues:")

print(most_successful_venue(df))