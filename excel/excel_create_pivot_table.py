"""
To see how much each gender has spent on each product line 
and sum the amount of money spent on each product.

for the case - gender in the index, product line in the column
"""

import pandas as pd

df_data = pd.read_excel('supermart_sales.xlsx')

# to select the columns
df = df_data[['Gender', 'Product line', 'Total']]

# to create a pivot table
# indicate the index, columns, values and aggfunc(optional)
pivot_table = df_data.pivot_table(index='Gender', columns='Product line', 
                                  values='Total', aggfunc = 'sum').round(0)

# export to excel file and name the sheet 'Report'(optional)
pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=2)












