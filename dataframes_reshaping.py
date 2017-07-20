import pandas as pd
# Reshaping data-frames Using - stack, unstack, melt,


# The people DataFrame
people = pd.DataFrame({'FirstName': ['John', 'Jane'], 'LastName': ['Doe', 'Austen'],
                       'BloodType': ['A-', 'B+'], 'Weight': [90, 64]})
print("People Before: \n{}".format(people))
# Use 'melt()' on the people DataFrame
people = pd.melt(people, id_vars=['FirstName', 'LastName'], var_name='measurements')
print("People After: \n{}".format(people))
print "-"*60
