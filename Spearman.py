import pandas as pd
from patsy import dmatrices
from matplotlib import pyplot as plt
import numpy as np
import os
#Change working directory
os.chdir("/Users/kymberlyvanlaar/Desktop")
#Read in Excel file
americanout = '2020americanout.xlsx'
americanout_df = pd.read_excel(americanout, header=0)
# Florida Correlation
americanout_df.plot.scatter(x='MIA_cases',y='MIA')
plt.xlabel('Florida Cases',fontsize=18)
Text(0.5, 0, 'Florida Cases')
plt.ylabel('MIA Traffic',fontsize=18)
Text(0, 0.5, 'MIA Traffic')
plt.show()
americanout_df.corr()['MIA_cases']
# Texas
americanout_df.plot.scatter(x='DFW_cases',y='DFW')
plt.xlabel('Texas Cases',fontsize=18)
Text(0.5, 0, 'Texas Cases')
plt.ylabel('DFW Traffic',fontsize=18)
Text(0, 0.5, 'DFW Traffic')
plt.show()
americanout_df.corr()['DFW_cases']
# California Cases
plt.xlabel('California Cases',fontsize=18)
Text(0.5, 0, 'California Cases')
plt.ylabel('LAX Traffic',fontsize=18)
Text(0, 0.5, 'LAX Traffic')
plt.show()
americanout_df.corr()['LAX_cases']
# Arizona cases
americanout_df.plot.scatter(x='PHX_cases',y='PHX')
plt.xlabel('Arizona Cases',fontsize=18)
Text(0.5, 0, 'Arizona Cases')
plt.ylabel('PHX Traffic',fontsize=18)
Text(0, 0.5, 'PHX Traffic')
plt.show()
#Spearman’s rank correlation
americanout_df.corr()['PHX_cases']



