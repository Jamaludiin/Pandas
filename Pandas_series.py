import pandas as pd

# A Pandas Series is like a column in a table. 
# or we can say, is a one-dimensional array holding data of any type.


#--------------------------------------------------------------------------------------------------------------------
# lets create a list and put some data
var_list = [22,44,55,66,77,88,77,99,90]
var_set = {22,44,55,66,77,88,77,99,90}
var_tuple = (1, 2, 3, 4, 6, 5, 7, 88, 5)


var_series_list = pd.Series(var_list)
#var_series_set = pd.Series(var_set) # it will triger an error becouse sets are unordered
var_series_tuple = pd.Series(var_tuple)


print(var_series_list) # it gives column id and data is represented in a clunm manner
#print(var_series_set)
print(var_series_tuple)


#--------------------------------------------------------------------------------------------------------------------
