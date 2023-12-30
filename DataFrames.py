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
    "Score 4": [93,44,89,56,87,43],
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
print(var_data_frame.loc[1]) # Note: This example returns a Pandas Series.

# return row 1 and 2
print(var_data_frame.loc[[1, 2]]) # Note: When using [], the result is a Pandas DataFrame.

