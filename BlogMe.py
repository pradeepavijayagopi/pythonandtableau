# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 21:03:50 2023

@author: rvija
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Reading excel or xlsx files
data = pd.read_excel('articles.xlsx')
#Summary of data
data.describe()
#summary of columns
data.info()
#counting number of articles per source
#format of groupby:df.groupby(['columntogroup'])['columntocount'].count()
data.groupby(['source_id'])['article_id'].count()
data.groupby(['source_id'])['engagement_reaction_count'].sum()
#Dropping column
data=data.drop('engagement_comment_plugin_count', axis = 1)

#defining function
def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range (0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
keywordflag = keywordflag('murder')
#Creating new column in df
keywordflag = pd.Series(keywordflag)
data['keyword_flag'] = keywordflag

#sentiment intensity analyzer
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length = len(data)

for x in range (0,10437):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment = pd.Series(title_neg_sentiment) 
title_pos_sentiment = pd.Series(title_pos_sentiment) 
title_neu_sentiment = pd.Series(title_neu_sentiment)  

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

#Writing the data
data.to_excel('blogme_clean.xlsx',sheet_name = 'blogmedata', index= False)

        
        
        
        
        
        





