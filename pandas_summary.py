import pandas as pd

# for series data
#--------------------------------------------------------------------------------------------------------------------
# pandas series()
var_series_list = pd.Series([1,2,3,4,5,6,7,8,9])

# access specific value of a series 
print(var_series_list[0]) 

# give labels to the data USE INDEX=[THE LABELS SEPERATED BY COMMA]
var_series_list = pd.Series([1,2,3,4,5,6,7,8,9], index=["A","B","C","D","E","F","G","H","I"])

# ALTERNATIVE TO THE ABOVE, YOU CAN USE DICTIONARY, THE LABELS WILL BE THE KEYS "Month 1" ETC
show_my_salary = pd.Series({"Month 1": 2000, "Month 2": 4000, "Month 3": 5000})

# display some of the salaries using index parameter
show_some_salary = pd.Series(show_my_salary, index = ("Month 1", "Month 3")) # THIS RETURN THE REUIRED DATA IF FOUND
print(show_some_salary)

# options.display.max_rows for changing the maxmimum rows to be diplayed, by default it can be 60
print(pd.options.display.max_rows) 

# Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 2000

#--------------------------------------------------------------------------------------------------------------------
# access data from csv file using the read_csv(path and the file) method
display_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')

#--------------------------------------------------------------------------------------------------------------------
# diplay top ten dataframes in the csv file using the head(), by default is 5, but you can specify the number
print(display_data.head(10))

#--------------------------------------------------------------------------------------------------------------------
# dislpaying the last 10 rows of the data using the tail, is option to specify the 10 or more
print(display_data.tail(10))

#--------------------------------------------------------------------------------------------------------------------
# you can display information about the data using info()
display_data.info()

#--------------------------------------------------------------------------------------------------------------------
# printing specific row
row_index = 2
specific_row = display_data.iloc[row_index]

# return row 1 and 2
print(display_data.loc[[1, 2]]) # Note: When using [], the result is a Pandas DataFrame.

#--------------------------------------------------------------------------------------------------------------------
# printing a specific column values using lopp
for i in display_data.index:
  print(display_data.loc[i, "Duration"])

#--------------------------------------------------------------------------------------------------------------------
# print the duplicates, this return true if that rows has duplicate similar
print(display_data.duplicated()) 

# drop duplicates
display_data.drop_duplicates(inplace = True)

#--------------------------------------------------------------------------------------------------------------------
# replacing the empty cells using median, mean or mode etc
# replaces the nan value to avoid string value to be converted to int
# median
median_calories_filled = display_data["Calories"].median()
display_data["Calories"].fillna(median_calories_filled, inplace=True)

# mean
mean_calories_filled = display_data["Calories"].mean()
display_data.fillna(mean_calories_filled,inplace=True)

# mode
mode_calories_filled = display_data["Calories"].mode()[0]
print(display_data["Calories"].fillna(mode_calories_filled, inplace=True))

#--------------------------------------------------------------------------------------------------------------------
#convert the colories column data into int
display_data['Calories'] = display_data['Calories'].astype(int)

#--------------------------------------------------------------------------------------------------------------------
# lets do some  intentional data manipulation and then remove these rows
display_data.loc[9, 'Duration'] = 400 # instead of 60

#--------------------------------------------------------------------------------------------------------------------
# this is the removal process, using loop
for x in display_data.index:
  if display_data.loc[x, "Duration"] >= 400:
    display_data.drop(x, inplace = True)

#--------------------------------------------------------------------------------------------------------------------
# assign new values when such condition match, e.g minimizing the extreme values
for i in display_data.index:
  if display_data.loc[i, "Duration"] >= 400:
    display_data.loc[i, "Duration"] = 60