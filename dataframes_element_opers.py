import numpy as np
import pandas as pd

print "-" * 60

data = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ])

# Importing Numpy array data to the data-frames.
df = pd.DataFrame(data=data, index=xrange(1, 4), columns=xrange(1, 4))
print "Data-frame 1 :\n{}".format(df)

# Using loc, iloc & ix
print "+"*60
print("df[1][1] = {} - using Location".format(df.loc[2]))
print("df[1][1] = {} - using position".format(df.iloc[2]))
print("df[1][1] = {} - using ix (index or position)".format(df.ix[2]))
print "+"*60


print "Adding index to data-frame"
df.set_index(2)
print "Data-frame 1 :\n{}".format(df)

df = pd.DataFrame(data=data, index=[2.5, 12.6, 4.8], columns=[48, 49, 50])

print "-" * 60
print "Updating rows to data-frame location using ix"
print "Data-frame Before :\n{}".format(df)
df.ix[2] = [60, 50, 40]

# ValueError: cannot set by positional indexing with enlargement
# df.ix[3] = [10, 10, 10]
print "Data-frame After 1:\n{}".format(df)

print "Adding rows to data-frame using label"
df.loc[2] = [11, 12, 13]
print "Data-frame After 2:\n{}".format(df)
print "-" * 60


df = pd.DataFrame(data=data, index=[2.5, 12.6, 4.8], columns=[48, 49, 50])
print "Adding column to data-frame using label"
print "Data-frame Before :\n{}".format(df)
# df[3] = df.index
df[3] = [15, 25, 35]
print "Data-frame After :\n{}".format(df)
print "-" * 60
