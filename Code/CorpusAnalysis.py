import pandas as pd

df = pd.read_csv('final_corpus2.csv')
loanwords = pd.read_csv('200FrenchLemmatized2.csv')

old_words = loanwords['Old Lemmatized']
new_words = loanwords['Modern Lemmatized']


loanwords['Old Count'] = [df['Token'].isin([word]).sum(axis=0) for word in old_words]
loanwords['New Count'] = [df['Token'].isin([word]).sum(axis=0) for word in new_words]

#loanwords.to_csv('csvfiles/FinalFrenchCount2.csv')