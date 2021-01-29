import pandas as pd
import zeyrek

lemmatizer = zeyrek.MorphAnalyzer()


loanwords = pd.read_csv('csvfiles/200French.csv')
print(loanwords)

old_lemmatized = [lemmatizer.lemmatize(word) for word in loanwords['Old Turkish']]
new_lemmatized = [lemmatizer.lemmatize(word) for word in loanwords['Modern Turkish']]
old_lem = [lis[0][1][0].lower() for lis in old_lemmatized]
new_lem = [lis[0][1][0].lower() for lis in new_lemmatized]
loanwords['Old Lemmatized'] = old_lem
loanwords['Modern Lemmatized'] = new_lem

loanwords.to_csv('200FrenchLemmatized2.csv', index=False)