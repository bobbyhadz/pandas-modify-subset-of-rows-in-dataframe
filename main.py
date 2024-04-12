# How to modify a Subset of Rows in a Pandas DataFrame

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 3, 1, 7],
    'salary': [175.1, 180.2, 190.3, 205.4],
})

print(df)

df.loc[df.experience == 1, 'salary'] = 150

print('-' * 50)

print(df)