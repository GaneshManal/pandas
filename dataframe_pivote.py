import pandas as pd

# Pivoting your data-frame
# pivot() : Create a new derived table out of your original one.
# Import pandas

products = pd.DataFrame({'category': ['Cleaning', 'Cleaning', 'Entertainment', 'Entertainment', 'Tech', 'Tech'],
                        'store': ['Walmart', 'Dia', 'Walmart', 'Fnac', 'Dia', 'Walmart'],
                         'price': [11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
                         'test-score': [4, 3, 5, 7, 5, 8]})

# Use pivot() to pivot the DataFrame
pivot_products = products.pivot(index='category', columns='store', values='price')
print "1. Pivot products : \n{} \ntype : {}".format(pivot_products, type(pivot_products))

# Use pivot() values to decide what to consider
pivot_products = products.pivot(index='category', columns='store')
print "1. Pivot products : \n{} \ntype : {}".format(pivot_products, type(pivot_products))

# Note: Data cannot have rows with duplicate values for the columns that you specify.
# If this is not the case, you will get an error message. If you can't ensure the uniqueness of your data,
# you will want to use the pivot_table method instead:

