import pandas as pd

"""
Bad data could be:
    Empty cells
    Data in wrong format
    Wrong data
    Duplicates
"""

var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')
print(var_csv_data.to_string()) 

print("\n")
#--------------------------------------------------------------------------------------------------------------------
# Cleaning Empty Cells
    #Empty cells can potentially give you a wrong result when you analyze data.
    #Remove Rows
        #One way to deal with empty cells is to remove rows that contain empty cells.

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
after_dropna = var_csv_data.dropna()

print(after_dropna.to_string())