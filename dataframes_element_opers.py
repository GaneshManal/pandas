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
print "Data-frame After 1:\n{}".format(df)
print "-" * 60

# Append a column to df using series
print "Adding column to data-frame using Series"
df.loc[:, 4] = pd.Series([100, 200, 300], index=df.index)
print "Data-frame After 1:\n{}".format(df)
print "-" * 60

df = pd.DataFrame(data=data, index=xrange(1, 4), columns=xrange(1, 4))
print "Data-frame Before :\n{}".format(df)
print "Resetting index of the Data-frame"
df.reset_index(level=0, drop=True)
print "Data-frame After :\n{}".format(df)
print "-" * 60

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6],
                                 [7, 8, 9], [40, 50, 60], [23, 35, 37]]),
                  index=[2.5, 12.6, 4.8, 4.8, 2.5],  columns=[48, 49, 50])
print "Data-frame Before :\n{}".format(df)
print "Deleting the row from data-frame"
# df.reset_index(level=0, drop=True)
# df.drop_duplicates(subset='index', keep='last').set_index('index')
# df.drop(2.5)
ret = df.drop(df.index[0], axis=0)
print "Data-frame After :\n{}".format(df)
print "-" * 60


df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6],
                                 [7, 8, 9], [40, 50, 60], [23, 35, 37]]),
                  index=[2.5, 12.6, 4.8, 4.8, 2.5],  columns=[48, 49, 50])
print "Data-frame Before :\n{}".format(df)
print "1. Deleting the column from data-frame ( using label : 50 )"
df.drop(50, axis=1, inplace=True)
print "Data-frame After 1:\n{}".format(df)

print "2. Deleting the column from data-frame ( using pos : 1 )"
# Not working ??
# The axis argument is either 0 when it indicates rows and 1 when it is used to drop columns.
# You can set inplace to True to delete the column without having to reassign the DataFrame.
df.drop(df.columns[[1]], axis=1)
print "Data-frame After 2:\n{}".format(df)
print "-" * 60

# There are some more operations available with data frames.
print "Deleting Rows"
print "Deleting Columns"
print "Resetting indexes"
print "Replacing All Occurrences of a String in a DataFrame"
print "Removing Parts From Strings in the Cells of Your DataFrame0"
print "Splitting Text in a Column into Multiple Rows in a DataFrame"
print "Applying A Function to Your Pandas DataFrame's Columns or Rows"
print "Applying maps DataFrame's Columns or Rows"
print "-" * 60

print "Creating Empty Frames"
df = pd.DataFrame(np.nan, index=[0, 1, 2, 3], columns=['A'])
print "Data-frame 1 :\n{}".format(df)

df = pd.DataFrame(index=range(0, 4), columns=['A'], dtype='float')
print "Data-frame 2 :\n{}".format(df)