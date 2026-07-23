import pandas as pd

from batting_analysis import *

from bowling_analysis import *

from team_analysis import *

from statistics_module import *

from visualization import *

df = pd.read_csv("../data/Ipl_Tournament_Data.csv")

while True:

    print("====================================")
    print("       IPL CRICKET ANALYTICS")
    print("====================================")

    print("1. Batting Analysis")
    print("2. Bowling Analysis")
    print("3. Team Analysis")
    print("4. Statistical Analysis")
    print("5. Visualization")
    print("6. Exit")


    try:
        choice = int(input("Enter your choice: "))


        # Batting Analysis
        if choice == 1 :

            print("===== BATTING ANALYSIS =====")

            print("Top 10 batsmen with most runs:")
            print(top_batsmen(df))

            print("Top 10 batsmen with best batting average:")
            print(batting_average(df))

            print("Top 10 batsmen with highest strike rate:")
            print(strike_rate(df))

            print("Top 10 batsmen with highest boundary percentage:")
            print(boundary_percentage(df))


        # Bowling Analysis
        elif choice == 2 :

            print("===== BOWLING ANALYSIS =====")

            print("Top 10 Bowlers with Highest Wickets: ")
            print(top_bowlers(df))

            print("Top 10 Bowlers with Best Economy: ")
            print(economy(df))

            print("Top 10 Bowlers with Best Bowling Average:")
            print(bowling_average(df))


        # Team Analysis
        elif choice == 3 :

            print("===== TEAM ANALYSIS =====")

            print("Team Wins: ")
            print(team_wins())

            print("Team Run Rate: ")
            print(team_run_rate())

            print("Team Comparison: ")
            print(team_comparison())


        # Statistical Analysis
        elif choice == 4 :

            print("===== STATISTICAL ANALYSIS =====")

            print("Mean of Runs: ")
            print(mean())

            print("Median of Runs: ")
            print(median())

            print("Mode of Runs:")
            print(mode())

            print("Variance of Economy: ")
            print(variance())

            print("Standard Deviation of Economy: ")
            print(standard_deviation())

            print("Minimum Runs: ")
            print(minimum())

            print("Maximum Runs: ")
            print(maximum())

            print("Correlation between Runs and Strike Rate: ")
            print(correlation_runs_strike_rate())


        # Visualization
        elif choice == 5 :

            print("===== VISUALIZATION =====")

            print("Generating graphs...")

            plot_bar_chart1(df)
            plot_bar_chart2(df)
            plot_scatter_plot(df)
            plot_pie_chart(df)
            plot_histogram(df)

            player_name = input(
                "Enter player name for match-wise performance graph: "
            )

            plot_line_graph(df, player_name)

            print("All graphs generated successfully.")


        # Exit
        elif choice == 6 :

            print("Thank you for using IPL Cricket Analytics!")

            break


        # For Invalid choice
        else:

            print("Invalid choice!")
            print("Please enter a number between 1 and 6.")

    except ValueError:
        print("Invalid input! Please enter a number.")