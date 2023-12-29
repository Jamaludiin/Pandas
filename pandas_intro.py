# Our goal is to analyze data, therefore Pandas is best module to use

"""
some of the things you can do in pandas include

Knowing your data more and answer some explotary questions such as
    Is there a correlation between two or more columns?
    What is average value?
    Max, Min value?
    Quartiles ranges

You can also:
    Clean your data
    access different data files such as json, csv files
    update, delete, insert etc can be done

    you can also analyze the data, plot graphs etc

"""


import pandas as pd

"""
#print(pd.__version__) # my previous bersion was 2.0.1
                      # after upgrade using this command pip install --upgrade pandas  the version become 2.1.4
"""


#--------------------------------------------------------------------------------------------------------------------
# let me declare dictionary and insert some data into it
my_data_dic = {
  'animal': ["Lion", "Tiger", "Cat", "Dog"],
  'age': [40, 38, 12, 22]
}

# display without using the dataframe 
print("\nWITHOUT USING DATAFRAME\n",my_data_dic)

# display using the dataframe 
var_show = pd.DataFrame(my_data_dic) # it gives id each row as it diplays like tablle data while the above does not
print("\nUSING DATAFRAME\n\n",var_show)


#--------------------------------------------------------------------------------------------------------------------
