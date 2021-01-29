# Imports
import pandas as pd
import zeyrek
from zemberek import TurkishTokenizer
import string
from turkish.deasciifier import Deasciifier
import pickle

# Functions from the toolkit
lemmatizer = zeyrek.MorphAnalyzer()
tokenizer = TurkishTokenizer.DEFAULT

# dataset getter
corpus = pd.read_csv('cs-filtered.csv')

# lowercase the text
def lowerText(corpus):
    return corpus['Text'].str.lower()

# Tokenize all Reddit comments
def tokenize_corpus(text):
    tokened2 = tokenizer.tokenize(text)
    tokens2 = []
    for tokens in tokened2:
        tokens2.append(tokens.content)
    return tokens2

# Deletes all the punctuation from the comments
def remove_punctuation(text):
    return text.str.replace('[{}]'.format(string.punctuation), '')

# Removes numbers from the comments
def remove_digits(text):
    return text.str.replace('\d+', '')

# Converts normal letters to Turkish letters, to make up for spelling errors
def deasciify(text):
    deasciifier = Deasciifier(text)
    text = deasciifier.convert_to_turkish()
    return text

text = lowerText(corpus)
text = remove_punctuation(text)
text = remove_digits(text)
text = [deasciify(comment) for comment in text]

tokens = []
for i in range(0, len(text)):
    tokens = tokens + tokenize_corpus(text[i])

filename = 'tokens.pk'
with open(filename, 'wb') as fi2:
    pickle.dump(tokens, fi2)

# gives all the possible lemmas for a word
lemmatized_options = [lemmatizer.lemmatize(comment) for comment in tokens]

filename2 = 'lemmatized_options.pk'
with open(filename2, 'wb') as fi:
    pickle.dump(lemmatized_options, fi)

# Chooses the first option as the lemma of choice
lemmatized_choice = []
list3 = [x for x in lemmatized_options if x != []] # removes empty tokens
for i in range(len(list3)):
    lemmatized_choice.append(list3[i][0][1][0].lower())

filename3 = 'final_corpus.pk'
with open(filename3, 'wb') as fi3:
    pickle.dump(rand_list, fi3)

