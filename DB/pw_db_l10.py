import pandas as pd

df = pd.read_excel("random_matrix.xlsx")
print(df, "\n")

array = df.to_numpy()
print(array)