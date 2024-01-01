import pandas as pd

"""
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
"""

#--------------------------------------------------------------------------------------------------------------------
#convert the data type of int
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')

print(var_csv_data.to_string())


median_calories_filled = var_csv_data["Calories"].median()# replaces the nan value to avoid string value to be converted to int

print("\nAfter Median filled in the Calories colunm")
print(var_csv_data["Calories"].fillna(median_calories_filled, inplace=True))

#convert the colories column data into int
var_csv_data['Calories'] = var_csv_data['Calories'].astype(int)
print(var_csv_data.to_string())

# other manipulations you can is to_datetime formatting
# df['Date'] = pd.to_datetime(df['Date'])


#--------------------------------------------------------------------------------------------------------------------
# Removing Rows  
# dop the nan values in a specific column
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')

print(var_csv_data.to_string())

var_csv_data.dropna(subset=['Calories'], inplace=True)

print(var_csv_data.to_string())


#--------------------------------------------------------------------------------------------------------------------
