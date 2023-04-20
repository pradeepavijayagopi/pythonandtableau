# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:07:08 2023

@author: rvija
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Method1 to read json file
json_file = open('loan_data_json.json')
data = json.load(json_file)

#Method2 to read json file
with open('loan_data_json.json') as json_file:
     data = json.load(json_file)
#transform to dataframe     
loandata = pd.DataFrame(data)

#Finding unique values for purpose column
loandata['purpose'].unique()
#Describe the data
loandata.describe()
#Describe data for specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()
#Working with arrays
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#Applying for loops to loandata
ficocat =[]
length = len(loandata)
for x in range(0,length):
    category = loandata['fico'][x]
    try:
        if category >= 300 and category < 400: 
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660: 
            cat = 'Fair'
        elif category >= 661 and category < 780: 
            cat = 'Good'
        elif category >= 781 and category < 850: 
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
    ficocat.append(cat)
ficocat = pd.Series(ficocat)
loandata['ficocategory'] = ficocat


#df.loc as conditional statements
#df.loc[df[columnname]]condition, newcolumnname]='value if condition is met'
#for interest rates, anew column name is wanted , rate > 0.12 then high, else low
loandata.loc[loandata['int.rate']>0.12,'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate']<=0.12,'int.rate.type'] = 'Low'

#number of loans/rows by ficocategory
catplot = loandata.groupby(['ficocategory']).size()
catplot.plot.bar(color = 'red', width = 0.2)
plt.show()
purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.2)
plt.show()

#Scatter Plots
xpoint = loandata['dti']
ypoint = loandata['annualincome']
plt.scatter(xpoint, ypoint, color = 'green')
plt.show()

#Writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)


      
        




