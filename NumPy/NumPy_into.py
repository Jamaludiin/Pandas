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

#--------------------------------------------------------------------------------------------------------------------
# check the type of the array 
print("Checking the array type",type(np.array(var_array_list))) # all are <class 'numpy.ndarray'>
print("Checking the array type",type(np.array(var_array_set))) # all are <class 'numpy.ndarray'>
print("Checking the array type",type(var_array_tuple)) # or like this is ok

#--------------------------------------------------------------------------------------------------------------------
# Array Dimensions in NumPy
#---------------------------------
#1: 0-D Arrays
    #0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
    #you can only store single value
print("\n0-D Arrays")
print(np.array(33))
# print(np.array(33,44,44,5,6)) # is this also zero dimentional arrays, no this will be error
# error of the above line is : TypeError: array() takes from 1 to 2 positional arguments but 5 were given

#---------------------------------
#2: 1-D Arrays
    # An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
    # in 1-D array you can store multiple values seperated by comma e.g. 22,33,44,55,66 etc
print("\n1-D Arrays")
print(np.array([33,44,66,77,88,99,22,11]))

#---------------------------------
#2: 2-D Arrays
    # An array that has 1-D arrays as its elements is called a 2-D array.
    # These are often used to represent matrix or 2nd order tensors.
print("\n2-D Arrays")
print(np.array([[1,2,3,4],[5,6,7,8]]))
print("\n2-D Arrays scond example")
print(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])) # what about this, is also works

#---------------------------------
#3: 3-D Arrays
    # An array that has 2-D arrays (matrices) as its elements is called 3-D array.
    # These are often used to represent a 3rd order tensor.
print("\n3-D Arrays")
print(np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]))

#---------------------------------
# How to Check the Number of array Dimensions
    # use the ndim attribute 

print("\nChecking the number of dimentions in 0-D Arrays")
check_array_dim = np.array(33).ndim
print(check_array_dim)

print("\nChecking the number of dimentions in 1-D Arrays")
print(np.array([33,44,66,77,88,99,22,11]).ndim)

print("\nChecking the number of dimentions in 2-D Arrays")
print(np.array([[1,2,3,4],[5,6,7,8]]).ndim)
print("\nChecking the number of dimentions in 2-D Arrays scond example")
print(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]).ndim)

print("\nChecking the number of dimentions in 3-D Arrays")
print(np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]).ndim)


#--------------------------------------------------------------------------------------------------------------------
# Higher Dimensional Arrays
# the beuty of array is that it have any number of dimentions
# When the array is created, you can define the number of dimensions by using the ndmin argument and pass the number you want.
print("\nThis is a higher dimentional array")
print(np.array([[[[[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3]]]]], ndmin=5)) # you created array with 5 dimentions fully specified

print("\nChecking the higher dimentional arrays")
print(np.array([[[[[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3]]]]], ndmin=5).ndim)


#--------------------------------------------------------------------------------------------------------------------
# How to index NumPy arrays
var_array = np.array([10, 33, 44, 46])

print("\nA0-dimentiional Array is indexed")
print(var_array[0])
print(var_array[2] + var_array[3]) # combines both values after indexed 44+46

#--------------------------------------------------------------------------------------------------------------------
# looping array value through their index
for i in var_array:
    print(i)

#--------------------------------------------------------------------------------------------------------------------
# indexing 2-D Arrays
var_array_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('\n2nd element on 1st row: ', var_array_2d[0, 1])