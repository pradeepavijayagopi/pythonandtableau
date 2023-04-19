# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:40:42 2023

@author: rvija
"""
import pandas as pd

# file_name = pd.read_csv('file.csv') ---> format to read csv file
data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv',sep =';')
#summary of data
data.info()
#variable = dataframe['COLUMNNAME']
CostPerTransaction = data['CostPerItem'] * data['NumberOfItemsPurchased']
#adding columns to dataframe
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

data['SellingPricePerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitPerTransaction'] = data['SellingPricePerTransaction'] - data['CostPerTransaction']

data['MarkUp'] = (data['SellingPricePerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

#Round Function
data['MarkUp'] = round(data['MarkUp'],2)
#Combining data fields
#Checking and Changing Datatypes
print (data['Day'].dtype)
day = data['Day'].astype(str)
print (day.dtype)
Year = data['Year'].astype(str)
print (Year.dtype)

data['Date'] = day+'-'+data['Month']+'-'+Year 

#Using iloc function to view specific Columns/rows
data.iloc[0]
data.iloc[0,3]
data.iloc[0:3]
data.iloc[-5]

#Using Split funtion
Split_Col = data['ClientKeywords'].str.split(',', expand = True)
data['ClientAge'] = Split_Col[0]
data['ClientType'] = Split_Col[1]
data['LengthofContract'] = Split_Col[2]

#Relace Function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

#Lower Function
data['ItemDescription'] = data['ItemDescription'].str.lower()

#How to Merge files
#Bringing new data set

Seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')

data = pd.merge(data,Seasons, on= 'Month')
#Dropping Columns
#df = df.drop('ColumnName', axis = 1)
data = data.drop(['ClientKeywords','Day','Month','Year'], axis = 1)

#Export to CSV
data.to_csv('ValueIncCleaned.csv', index = False)

























