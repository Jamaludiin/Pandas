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


#--------------------------------------------------------------------------------------------------------------------
# lets change some values and fix again using the same
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')
print(var_csv_data.head(10))

var_csv_data.loc[9, 'Duration'] = 400 # instead of 60
var_csv_data.loc[2, 'Duration'] = 500 # instead of 60
var_csv_data.loc[5, 'Duration'] = 590 # instead of 60
var_csv_data.loc[6, 'Duration'] = 456 # instead of 60

print("\nBefore correction")
print(var_csv_data.head(10))

# fix using lopp
for i in var_csv_data.index:
  if var_csv_data.loc[i, "Duration"] >= 400:
    var_csv_data.loc[i, "Duration"] = 60

print("\nAfter correction")
print(var_csv_data.head(10))

#--------------------------------------------------------------------------------------------------------------------
# looping single column value
print("\nBefore correction")

# fix using lopp
k = 0
for i in var_csv_data.index:
  print(var_csv_data.loc[i, "Duration"])
  k = k + 1

print("\nThe the number of rows",k)
var_csv_data.info() # check all infor and see if the k value match the duration colunm count or total rows number

#--------------------------------------------------------------------------------------------------------------------
# Droping or removing rows
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')

# lets do some  intentional data manipulation and then remove these rows
var_csv_data.loc[9, 'Duration'] = 400 # instead of 60
var_csv_data.loc[2, 'Duration'] = 500 # instead of 60
var_csv_data.loc[5, 'Duration'] = 590 # instead of 60
var_csv_data.loc[6, 'Duration'] = 456 # instead of 60

print("\nBefore removal rows but after manipulation the original")
print(var_csv_data.head(10))


# this is the removal process
for x in var_csv_data.index:
  if var_csv_data.loc[x, "Duration"] >= 400:
    var_csv_data.drop(x, inplace = True)

print("\nAfter removal rows")
print(var_csv_data.head(10))

#--------------------------------------------------------------------------------------------------------------------
# display the column names
print()

for i in var_csv_data:
    print(i)

print()
# display the column first letter of their names
colmn_index = 0
for i in var_csv_data:
  print("Column",i[colmn_index])
  colmn_index +=1