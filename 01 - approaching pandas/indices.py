import pandas as pd

s1 = pd.Series(
    [3,2.5,-1,18],
    index=["a","b","c","d"]
)
s2 = pd.Series(
    [3,2.5,-1],
    index=["b","c","d"]
)
print(s1+s2)

# Useful methods
# valor absoluto
print(s1.abs())
# varianza
print(s1.var())
# https://pandas.pydata.org/docs/reference/api/pandas.Series.html

