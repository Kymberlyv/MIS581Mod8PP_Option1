
import pandas as pd
import os
# Change working directory
os.chdir("/Users/kymberlyvanlaar/Desktop")
#Read in Excel file
american = '2020aadata2.xlsx'
xl = pd.ExcelFile(american)
from scipy import stats
american_df = xl.parse('Sheet1')
import numpy as np
from scipy.stats import iqr
#Calculate Q1 and Q3
Q1 = american_df.quantile(0.25)
Q3 = american_df.quantile(0.75)
#Subtract Q1 from Q3 to get middle fifty percent
IQR = Q3-Q1
print(IQR)
#Revise data to eliminate outliers
american_df_out = american_df[~((american_df<(Q1-1.5*IQR))|(american_df>(Q3+1.5 *IQR))).any(axis=1)]
american_df_out.shape
import openpyxl

#Export to ExcelFile AmericanOut
american_df_out.to_excel(r'/Users/kymberlyvanlaar/Desktop/2020americanout.xlsx',index = False, header = True)
# (Sharma, 2018)

