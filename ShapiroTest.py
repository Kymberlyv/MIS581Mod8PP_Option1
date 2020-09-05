# Import programs
from scipy.stats import shapiro
import os
import pandas as pd
os.chdir("/Users/kymberlyvanlaar/Desktop")
 #Read in Excel file
american = '2020americanout.xlsx'
xl = pd.ExcelFile(american)
df = xl.parse('Sheet1')
PHX_cases = df['PHX_cases']
# Test PHX cases for normal distribution
stat, p = shapiro(PHX_cases)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
     print('Probably normal')
else:
    print('Probably not normal')
# Test PHX airline traffic for normal distribution
PHX = df['PHX']
stat, p = shapiro(PHX)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
     print('Probably normal')
else:
     print('Probably not normal')

# Test DFW cases for normal distribution
DFW_cases = df['DFW_cases']
stat, p = shapiro(DFW_cases)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Probably normal')
else:
    print('Probably not normal')

# Test DFW airline traffic for normal distribution
DFW = df['DFW']
stat, p = shapiro(DFW)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Probably normal')
else:
    print('Probably not normal')

# Test LAX cases for normal distribution
LAX_cases = df['LAX_cases']
stat, p = shapiro(LAX_cases)
print('stat=%.3f, p=%.3f' % (stat, p))

if p > 0.05:
    print('Probably normal')
else:
   print('Probably not normal')

#Test LAX airline traffic
LAX = df['LAX']
stat, p = shapiro(LAX)
print('stat=%.3f, p=%.3f' % (stat, p))

if p > 0.05:
     print('Probably normal')
else:
    print('Probably not normal')

#Test MIA cases for normal distribution
MIA_cases = df['MIA_cases']
stat, p = shapiro(MIA_cases)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Probably normal')
else:
    print('Probably not normal')

#Test MIA airline traffic
MIA = df['MIA']
stat, p = shapiro(MIA)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
     print('Probably normal')
else:
    print('Probably not normal')

# (Brownlee, 2019)


