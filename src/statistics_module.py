# This section calculates :
#
# - Mean
# - Median
# - Mode
# - Variance
# - Standard Deviation
# - Minimum
# - Maximum and
# - Correlation Coefficient between runs and strike rate

import pandas as pd

df = pd.read_csv("../data/cleaned_data.csv")


# Function to calculate mean runs
def mean():

    mean_runs = df["Runs"].mean()

    return mean_runs


# Function to calculate median runs
def median():

    median_runs = df["Runs"].median()

    return median_runs


# Function to calculate mode runs
def mode():

    mode_runs = df["Runs"].mode()

    return mode_runs


# Function to calculate variance of Economy
def variance():

    variance_economy = df["Economy"].var()

    return variance_economy


# Function to calculate standard deviation of Economy
def standard_deviation():

    standard_deviation_economy = df["Economy"].std()

    return standard_deviation_economy


# Function to calculate minimum runs
def minimum():

    minimum_runs = df["Runs"].min()

    return minimum_runs


# Function to calculate maximum runs
def maximum():

    maximum_runs = df["Runs"].max()

    return maximum_runs


# Function to calculate the correlation coefficient between runs and strike rate
def correlation_runs_strike_rate():

    correlation1 = df["Runs"].corr(df["Strike_Rate"])

    return correlation1


# Function to calculate the correlation coefficient between runs and strike rate
def correlation_Overs_Wickets():

    correlation2 = df["Overs_Bowled"].corr(df["Wickets"])

    return correlation2
