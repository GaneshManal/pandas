import os
import numpy as np
import pandas as pd

data = np.array([
        ['', 'Col1', 'Col2'],
        ['Row1', 1, 2],
        ['Row2', 3, 4]
        ])

print "-" * 60

# Importing Numpy array data to the data-frames.
df_1 = pd.DataFrame(data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:])
print "Data-frame 1 :\n{}".format(df_1)
print "-" * 60

print "Writing data-frame to file"
df_1.to_csv('output.csv', sep='\t',  encoding='utf-8')
print "Done"
print "-" * 60

print "Writing the data-frame to Excel"
writer = pd.ExcelWriter('myDataFrame.xlsx')
df_1.to_excel(writer, 'DataFrame')
writer.save()
print "Done"
print "-" * 60


