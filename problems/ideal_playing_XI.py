# Ideal Playing XI Based on Statistics

import pandas as pd

#importing ppi data from PPP.py
df = pd.read_csv("../data/Ipl_Tournament_Data.csv")


wicketkeeper = df[df["Role"] == "Wicketkeeper"]

wicketkeeper = wicketkeeper.groupby("Player").agg({
    "Runs": "sum",
    "Catches": "sum"
})

wicketkeeper = wicketkeeper.sort_values(
    by=["Runs", "Catches"],
    ascending=False
)

best_wicketkeeper = wicketkeeper.head(1)

print(best_wicketkeeper)

batsmen = df[df["Role"] == "Batter"]

batsmen = batsmen.groupby("Player")["Runs"].sum()

batsmen = batsmen.sort_values(ascending=False)

best_batsmen = batsmen.head(4)

print(best_batsmen)

all_rounders = df[df["Role"] == "All-Rounder"]

all_rounders = all_rounders.groupby("Player").agg({
    "Runs": "sum",
    "Wickets": "sum",
    "Catches": "sum"
})

all_rounders = all_rounders.sort_values(
    by=["Runs", "Wickets", "Catches"],
    ascending=False
)

best_all_rounders = all_rounders.head(2)

print(best_all_rounders)

bowlers = df[df["Role"] == "Bowler"]

bowlers = bowlers.groupby("Player")["Wickets"].sum()

bowlers = bowlers.sort_values(ascending=False)

best_bowlers = bowlers.head(4)

print(best_bowlers)

ideal_xi = pd.concat([
    best_wicketkeeper.reset_index(),
    best_batsmen.reset_index(),
    best_all_rounders.reset_index(),
    best_bowlers.reset_index()
])

ideal_xi = ideal_xi.fillna(0)

ideal_xi = ideal_xi.sort_values(by=["Runs", "Wickets", "Catches"], ascending=False)

print("========== IDEAL PLAYING XI ==========")
print(ideal_xi)