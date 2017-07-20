import os
import pandas as pd

# Read csv File
try:
    in_file = open(os.getcwd() + os.path.sep + 'in.csv')
    pd.read_csv(in_file)

except Exception as e:
    print 'Exception : ', str(e)

else:
    print "inside else"
    in_file.close()

print "Input Data : {}".format(dir(pd))
print "-"*60
