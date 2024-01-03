#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

my_data = pdisplay_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/Pandas/data.csv')


my_data.plot()

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()