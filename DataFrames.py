import pandas as pd

# DataFrames is like a table

#--------------------------------------------------------------------------------------------------------------------
# this is series and is diffrent from the dataframe becouse, this data will triger error if applied to dataframe
var_dic_data = {
    "Score 1": 90,
    "Score 2": 100,
    "Score 4": 93,
    "Score 4": 84,
    "Score 5": 55

}

var_series_data = pd.Series(var_dic_data)

print(var_series_data)

# indexing specific data in series/column
print(var_series_data["Score 5"])
#--------------------------------------------------------------------------------------------------------------------
# THIS IS DATAFRAME
var_dic_data = {
    "Score 1": [90,33,55,66,88,99], # NOTE THE DATA MUST BE THE SAME LENGHT IN EACH ROW N COLUMN, OTHERWISE IT WILL TRIGER AN ERROR
    "Score 2": [100,99,88,55,77,56],
    "Score 4": [93,44,89,56,87,43],# if they have two ids the last one will be stored
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}

#loading the above data into the DataFrame object as follows:
var_data_frame = pd.DataFrame(var_dic_data)

print(var_data_frame)


#--------------------------------------------------------------------------------------------------------------------
# CAN WE GIVE CUSTOM ID TO THE DATAFRAME DATA
var_data_frame = pd.DataFrame(var_dic_data, index= (1,2,3,4,5,6)) # you can do like this, or auto generate custome ids
print(var_data_frame)

#--------------------------------------------------------------------------------------------------------------------
# indexing specific row in dataframe. so you cannot use the [index number] instead use the loc
print("\nlocating data or row data")
print(var_data_frame.loc[1]) # Note: This example returns a Pandas Series. means the row will be converted to colunm

# return row 1 and 2
print(var_data_frame.loc[[1, 2]]) # Note: When using [], the result is a Pandas DataFrame.


#--------------------------------------------------------------------------------------------------------------------
# Load data from csv file using the read_csv()
print("\n")
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')

print(var_csv_data)

#--------------------------------------------------------------------------------------------------------------------
print("\nPrinting the entire data in the dataframe using to_string")
print(var_csv_data.to_string()) 

#--------------------------------------------------------------------------------------------------------------------
# max_rows
"""
The number of rows returned is defined in Pandas option settings.

You can check your system's maximum rows with the pd.options.display.max_rows statement.

In my system the number is 60, which means that if the DataFrame contains more than 60 rows, 
the print(df) statement will return only the headers and the first and last 5 rows.
"""
print("\nMy Pandas return the maximum rows option in the stting is")
print(pd.options.display.max_rows) 

#--------------------------------------------------------------------------------------------------------------------
# Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 2000

display_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')
print("\Display the data")
print(display_data)

print("\nIncreasing the max_rows")
print(pd.options.display.max_rows) 


#--------------------------------------------------------------------------------------------------------------------
# The head() method returns the headers and a specified number of rows, starting from the top.
print("\nThe first ten rows")
print(display_data.head(10))

# if you dont specify any parameter it will return the first five rows
print("\nThe first five rows")
print(display_data.head())

#--------------------------------------------------------------------------------------------------------------------
# There is also a tail() method for viewing the last rows of the DataFrame.
print("\nThe last five rows")
print(display_data.tail())

print("\nThe last ten rows")
print(display_data.tail(10))

#--------------------------------------------------------------------------------------------------------------------
# Info About the Data
print("\nInfo about the data")
print(display_data.info())

