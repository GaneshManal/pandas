import numpy as np
import pandas as pd

data = np.array([
        ['', 'Col1', 'Col2'],
        ['Row1', 1, 2],
        ['Row2', 3, 4]
        ])

print "Data : {}".format(data)
print "Size  : {}".format(data.size)
# print "Dir    : {}".format(dir(data))

# Importing Numpy array data to the data-frames.
print "-" * 60
df_1 = pd.DataFrame(data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:])
print "Data-frame 1 :\n{}".format(df_1)

# Take a 2D array as input to your DataFrame
print "-" * 60
my_array = np.array([[1, 2, 3], [4, 5, 6]])
df_2 = pd.DataFrame(data=my_array[0:, 0:])
print "Data-frame 2 :\n{}".format(df_2)


# Take a dictionary as input to your DataFrame
print "-" * 60
my_dict = {'A': [1, 3], 'B': [1, 2], 'C': [2, 4]}
data = my_dict.values()
print ':', data, type(data)
df_3 = pd.DataFrame(data=data, index=my_dict.keys(), columns=my_dict.keys()[:2])
print "Data-frame 3 :\n{}".format(df_3)


# Take a DataFrame as input to your DataFrame
print "-" * 60
df_4 = pd.DataFrame(data=[4, 5, 6, 7], index=range(0, 4), columns=['A'])
print "Data-frame 4 :\n{}".format(df_4)

# Take a Series as input to your DataFrame
print "-" * 60
df_5 = pd.Series({"Belgium": "Brussels", "India": "New Delhi",
                  "United Kingdom": "London", "United States": "Washington"})
print "Data-frame 5 :\n{}".format(df_5)

print "-" * 60
print("Dir : {}".format(dir(df_5)))
