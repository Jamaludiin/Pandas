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
after_dropna = var_csv_data.dropna() # this will not remove permenetly the empty rows

print(after_dropna.to_string())

#--------------------------------------------------------------------------------------------------------------------
# remove the empty rows permenetly from the original file
#If you want to change the original DataFrame, use the inplace = True argument:
print("\n Confused\n")

# this commented place failed while the others works, idont know why he refuse to store in another variable
"""after_dropna_inplace = var_csv_data.dropna(inplace = True)# if there is no empty places it will triger an error (attributeError)

print(after_dropna_inplace.to_string())"""

# explained the error
"""
The issue in your code is related to the use of the inplace=True argument with the dropna method in Pandas. 
When inplace=True is used, the dropna method modifies the original DataFrame and returns None. As a result, 
trying to print the result (after_dropna_inplace) will lead to an AttributeError 
because None does not have a to_string method.
"""
# solution, becouse this returns none, as it removes permenantly and you need to access directly
    # Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, 
    # but it will remove all rows containing NULL values from the original DataFrame.
var_csv_data.dropna(inplace=True)

print(var_csv_data.to_string())



# Replacing Empty Values in the dataframe
#--------------------------------------------------------------------------------------------------------------------
# if you dont need to remove the empty cells and its rows, 
# you can fill the empty palces using the fillna() method allows us to replace empty cells with a value

# In this example we are going to replace NULL values with the number 120:

var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv') # call this otherwise it will return data that was already modified

print("\Before Replacing the null values to a 120")
print(var_csv_data.to_string())

print("\nAfter Replacing the null values to a 120")
var_csv_data.fillna(120, inplace = True)
print(var_csv_data.to_string())

#--------------------------------------------------------------------------------------------------------------------
# fillna with specific colunmx
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv') 
print("\nAfter Replacing the null values to a 120")

# display only one colunm
print(var_csv_data["Calories"].to_string())

# fillna applied in a specific colunm
var_csv_data["Calories"].fillna(110, inplace = True)
print(var_csv_data.to_string())

#--------------------------------------------------------------------------------------------------------------------
# Replace Using Mean, Median, or Mode

# Mean
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv') 

# display only one colunm
print("\nBefore Means filled in the Calories colunm")
print(var_csv_data["Calories"].to_string())

mean_calories_filled = var_csv_data["Calories"].mean()
var_csv_data.fillna(mean_calories_filled,inplace=True)
print("\nAfter Means filled in the Calories colunm")
print(var_csv_data["Calories"].to_string())
print("The mean of colories is",mean_calories_filled)

#--------------------------------------------------------------------------------------------------------------------
# Replace Using Mean, Median, or Mode
# Median
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')
# display only one colunm
print("\nBefore Means filled in the Calories colunm")
print(var_csv_data["Calories"].to_string())

median_calories_filled = var_csv_data["Calories"].median()

print("\nAfter Median filled in the Calories colunm")
print(var_csv_data["Calories"].fillna(median_calories_filled, inplace=True))

print(var_csv_data["Calories"].to_string())
print("The median is",median_calories_filled)


#--------------------------------------------------------------------------------------------------------------------
# Replace Using Mean, Median, or Mode
# Mode
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')
# display only one colunm
print("\nBefore Mode filled in the Calories colunm")
print(var_csv_data["Calories"].to_string())

mode_calories_filled = var_csv_data["Calories"].mode()[0]

print("\nAfter Mode filled in the Calories colunm")
print(var_csv_data["Calories"].fillna(mode_calories_filled, inplace=True))

print(var_csv_data["Calories"].to_string())
print("The Mode is",mode_calories_filled)

