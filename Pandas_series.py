import pandas as pd

# A Pandas Series is like a column in a table. 
# or we can say, is a one-dimensional array holding data of any type.


#--------------------------------------------------------------------------------------------------------------------
# lets create a list and put some data
var_list = [22,44,55,66,77,88,77,99,90]
var_set = {22,44,55,66,77,88,77,99,90}
var_tuple = (1, 2, 3, 4, 6, 5, 7, 88, 5)
var_string = "This is series"
var_string_list = ["A one", "A two", "A three", "A four", "A five", "A six", "A seven", "A eight", "A nine", "A ten"]

var_series_list = pd.Series(var_list)
#var_series_set = pd.Series(var_set) # it will triger an error becouse sets are unordered
var_series_tuple = pd.Series(var_tuple)
var_series_string = pd.Series(var_string)
var_series_string_list = pd.Series(var_string_list)



print(var_series_list) # it gives column id and data is represented in a clunm manner
#print(var_series_set) # dont print this
print(var_series_tuple)
print(var_series_string) # the string become one row and take one id
print(var_series_string_list)


#--------------------------------------------------------------------------------------------------------------------
# Access some of the values in the series
# All what you need is to speciy their index which starts from 0 to n
print(var_series_list[0]) 
print(var_series_string_list[8])

#--------------------------------------------------------------------------------------------------------------------
# giving Labels to the data series or data frames. before it generates id for it which starts from 0 to n
var_data_with_label = ["A","B","C","D","E","F"]
var_data_with_label_2 = ("A","B","C","D","E","F")

# state index and assign the label as list
var_data_labels_1 = pd.Series(var_data_with_label, index = ["x", "y", "z","a", "b", "c"])# you can specify the labels as list or tuple is ok
var_data_labels_2 = pd.Series(var_data_with_label_2, index = ("2", "5", "9",2,3,4)) # any data type it can accept as a label


print(var_data_labels_1)
print(var_data_labels_2)


#--------------------------------------------------------------------------------------------------------------------
# this is also another option of creating series with key/values by using the dictionary 

Slary = {"Month 1": 2000, "Month 2": 4000, "Month 3": 5000}

show_my_salary = pd.Series(Slary)

print(show_my_salary)

# display some of the salaries using index parameter
show_some_salary = pd.Series(show_my_salary, index = ("Month 1", "Month 3"))
print(show_some_salary)

#--------------------------------------------------------------------------------------------------------------------
