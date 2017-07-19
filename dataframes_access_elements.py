import numpy as np
import pandas as pd

print "-" * 60

data = np.array([
        ['', 'C1', 'C2', 'C3'],
        ['R1', 1, 2, 3],
        ['R2', 4, 5, 6],
        ['R3', 7, 8, 9]
        ])

# Importing Numpy array data to the data-frames.
df = pd.DataFrame(data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:])
print "Data-frame 1 :\n{}".format(df)

print "-" * 60

# Accessing the data-frame elements.
print "Accessing data-frame Elements"

# Using index location
print("df[1][1] = {} - using index".format(df.iloc[1][1]))

# Using loc[]
print("df[1][1] = {} - using Location".format(df.loc['R2']['C2']))

# Using `at[]`
print("df[1][1] = {} - using at".format(df.at['R2', 'C2']))

# Using `iat[]`
print("df[1][1] = {} - using index at".format(df.iat[1, 1]))

# Using `get_value(index, column)`
print("df[1][1] = {} - using get value".format(df.get_value('R2', 'C2')))

print "-" * 60

print "Accessing data-frame Row"
print("Row[1] = \n{}".format(df.iloc[1]))

print "-" * 60

print "Accessing data-frame Column"
print("Column[1] = \n{}".format(df.loc[:, 'C2']))
