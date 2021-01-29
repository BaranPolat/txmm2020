# Take 200 random loanwords from the complete dataset
# imports
import pandas as pd
import numpy as np
from sympy import symbols, Eq, solve


# setup
np.random.seed(2020)
df = pd.read_csv('ArabicLoanwords.csv')
x = symbols('x')

#parameters
remove_n = solve(Eq(len(df.index)-x, 200), x)[0]
drop_indices = np.random.choice(df.index, remove_n, replace=False)
df = df.drop(drop_indices)
df.to_csv('RandomArabicLoanwords.csv', index=False)