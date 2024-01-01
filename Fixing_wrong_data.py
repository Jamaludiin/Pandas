import pandas as pd


#--------------------------------------------------------------------------------------------------------------------
#lets first add wrong data into a specific row and fix later
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')

var_csv_data.loc[10, 'Maxpulse'] = 14 # instead of 147

print(var_csv_data.to_string())

#--------------------------------------------------------------------------------------------------------------------
# lets fix again using the same
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')

var_csv_data.loc[10, 'Maxpulse'] = 147 # instead of 147

print(var_csv_data.to_string())

#--------------------------------------------------------------------------------------------------------------------
# printing the first 10 rows
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')

print(var_csv_data.head(10))

#--------------------------------------------------------------------------------------------------------------------
# printing specific row
row_index = 2
specific_row = var_csv_data.iloc[row_index] # returns a Pandas Series. means the row will be converted to colunm, thus column names at the left and values at the right

print("\nprinting specific row using iloc[2]")
print(specific_row)

# there is diffrence between iloc[] and loc[]
print("\nlocating data or row data using loc[1]")
print(var_csv_data.loc[1]) # Note: This example returns a Pandas Series. means the row will be converted to colunm

print("\nlreturn row 1 and 2 using loc[[1,2]]")
# return row 1 and 2
print(var_csv_data.loc[[1, 2]]) # Note: When using [], the result is a Pandas DataFrame.

