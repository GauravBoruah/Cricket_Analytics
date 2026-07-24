# IPL Cricket Analytics

## About the Project

This project analyzes IPL cricket data using Python. It provides batting,
bowling, team, statistical, and visualization-based analysis.

## Features

- Batting Analysis
- Bowling Analysis
- Team Analysis
- Statistical Analysis
- Data Visualization
- Player Performance Index
- Ideal Playing XI

## Technologies Used

- Python
- Pandas
- Matplotlib

## How to Run

1. Open the project in PyCharm.
2. Open `src/main.py`.
3. Make sure the data file is inside the data folder.
4. Run the program
5. Select the required option from the menu by typing the number associate with the option.


## Project Structure

Cricket_Analytics

- 

data/
- -----Ipl_Tournament_Data.csv
- -----cleaned_data.csv
- ------team_summary

src/

- ------main.py
- ------data_loader.py
- ------batting_analysis.py
- ------bowling_analysis
- ------statistics_module.py
- ------team_analysis.py
- ------visualization.py

figures/

- -----batting_ranking.png
- -----bowling_ranking.png
- -----player_performance.png
- -----player_score_distribution.png
- -----strike_rate_vs_runs.png
- -----team_comparison.png

problems/

- -----PPI.py
- -----ideal_playing_XI.py

reports/

- -----README.md
- -----presentation.pptx

## Conclusion

The Cricket Analytics project provides a simple and effective way to analyze cricket data using Python. 
The project defines a player performance index (ppi) which ranks players based on their overall performance. 
In addition, an Ideal Playing XI is created by selecting the best players according to their performance,
consisting of 4 batsmen, 4 bowlers, 2 all-rounders, and 1 wicketkeeper.
