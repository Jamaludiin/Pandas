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
import numpy

var_list = [22,44,55,66,77,88,77,99,90]

# See the diffrence, the array you use the array() method from numpy library while the list is python pure
var_array = numpy.array([1, 2, 3, 4, 5])

print(var_array) # output [1 2 3 4 5]
print(var_list) # output [22, 44, 55, 66, 77, 88, 77, 99, 90]

#--------------------------------------------------------------------------------------------------------------------
