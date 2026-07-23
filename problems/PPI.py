# PPI Formula
#
# PPI =
# 0.4 × Runs
# +25 × Wickets
# +5 × Catches
# +0.1 × Strike Rate
# −2 × Economy
#
# Players are ranked using this score.

import pandas as pd

df = pd.read_csv("../data/Ipl_Tournament_Data.csv")

# defining ppi using the formula

df["PPI"] = (

0.4*df["Runs"] + 25*df["Wickets"] + 5*df["Catches"] + 0.1*df["Strike_Rate"] - 2*df["Economy"]

)

ppi = df.groupby("Player")["PPI"].mean()

ppi = ppi.sort_values(ascending=False)

print(ppi)