import pandas as pd

# To read the csv file
data = pd.read_csv("../data/Ipl_Tournament_Data.csv")

print(data)

# To display information about the dataset
print("The information of the file: ")
print(data.info())

# To check for missing values
print("Column wise number of missing values are: ")
print(data.isnull().sum())

# To save the cleaned data
data.to_csv("cleaned_data.csv", index=False)

print("Cleaned data saved successfully.")

