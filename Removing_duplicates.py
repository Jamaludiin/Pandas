import pandas as pd

#--------------------------------------------------------------------------------------------------------------------
#lets first add wrong data into a specific row and fix later
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')

# change the setting of the pandas to maxmize the number of rows appear
pd.options.display.max_rows = 2000

print(var_csv_data.to_string())

# print the duplicates, this return true if that rows has duplicate similar
print(var_csv_data.duplicated()) 

# drop the duplicates
var_csv_data.drop_duplicates(inplace = True)

# print all the dataframe
print(var_csv_data.to_string())

# show again if the duplicates still exist
print(var_csv_data.duplicated()) 
