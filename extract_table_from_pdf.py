"""
Extract tables from pdfs
using camelot-py
"""

import camelot

# read pdf
tables = camelot.read_pdf('foo.pdf', pages='1')
#print(tables)

#export table to/into csv file
tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')