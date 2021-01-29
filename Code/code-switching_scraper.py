# Takes the dataset from Rabinovich et al. and takes the Turkish-English combinations

# -*- coding: utf-8 -*-
# imports
import pandas as pd
import csv



# read file
df = pd.read_csv('cs_additional_reddit_corpus.csv')

# filter dataset for English-Turkish
languages = ['Turkish', 'English']
df = df.loc[(df['Lang1'].isin(languages)) & (df['Lang2'].isin(languages))]


df.to_csv('cs-filtered.csv')


