# import pandas as pd

# data = {
#     "name": ["Alex", "Oleg", "Max"],
#     "age": [25, 32, 28],
#     "salary": [2000, 3000, 2500]
# }
#
# df = pd.DataFrame(data)
#
# print(df, "\n")
#
# my_series = pd.Series([5,6,7,8,9,10,11,12,13,14,15])
# print(my_series)

# df = pd.DataFrame({
#     'country': ['Russia', 'Kazakhstan', 'Belarus', 'Ukraine'],
#     'population': [17.04, 143.05, 9.5, 45.5],
#     'square': [2724902, 17125191, 207600, 603628]
# })
#
#
# df.index = ['RU', 'KZ', 'BY', 'UA']
# df.index.name = 'country code'
# print(df.head())
# print(df.loc[['KZ', 'RU'], 'population'])


import numpy as np

# left = np.array([[1,3],[2,-4]])
# right = np.array([9,8])
# print(np.linalg.solve(left,right))

matrix = np.array([
    [1,2],
    [3,4]
])

print(matrix[0][1])
