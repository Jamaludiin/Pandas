"""
We use NumPy library when working with arrays.
NumPy is short for "Numerical Python".

It is opensource            created in 2005

The Main Reason of using NumPy is 
    To overcome the slow process of the list in python
    So NumPy was aimed to solve such issue and it is faster than the list

When you are anayzing huge data array is important 

Although Numpy is python library and writen most of the code in Python, therefore, some parts are written in C and C++ especially those parts who need faster process

You can Install NumPy using this command   pip install numpy
"""

#--------------------------------------------------------------------------------------------------------------------
# To get started NumPy you need to import its library after installation
import numpy as np

var_list = [22,44,55,66,77,88,77,99,90]

# See the diffrence, the array you use the array() method from numpy library while the list is python pure
var_array = np.array([1, 2, 3, 4, 5])

print(var_array) # output [1 2 3 4 5]
print(var_list) # output [22, 44, 55, 66, 77, 88, 77, 99, 90]

#--------------------------------------------------------------------------------------------------------------------
# check the kind of NumPy version that you are using by calling np.__version__
print(np.__version__) # this numpy version is 1.24.3

#--------------------------------------------------------------------------------------------------------------------
# the array object in numpy is called ndarray. and we create it using array() method
# in array() method you can pass any data type
var_list = [22,44,55,66,77,88,77,99,90]
var_set = {22,44,55,66,77,88,77,99,90}
var_tuple = (1, 2, 3, 4, 6, 5, 7, 88, 5)


var_array_list = np.array(var_list)
var_array_set = np.array(var_set)
var_array_tuple = np.array(var_tuple)

print("\nArray declaration using np.array() method")
print(var_array_list)
print(var_array_set)
print(var_array_tuple)


