import pandas as pd

# Is important to find the relationship between your data especially those listed in columns
# Pandas gives you a function to calculate such statistic and return the summary of such info 

# we use corr() method.

my_data_corr = pdisplay_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')

print(my_data_corr.corr())
# iA correlation of -1.0 indicates a perfect negative correlation and a correlation of 
    # 1.0 indicates a perfect positive correlation.

"""
The number varies from -1 to 1.

1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.

0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.
"""


"""
Perfect Correlation:
We can see that "Duration" and "Duration" got the number 1.000000, which makes sense, each column always has 
a perfect relationship with itself.

Good Correlation:
"Duration" and "Calories" got a 0.922721 correlation, which is a very good correlation, and we can predict that 
the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, 
you probably had a long work out.

Bad Correlation:
"Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not 
predict the max pulse by just looking at the duration of the work out, and vice versa.
"""