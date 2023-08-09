from openpyxl import load_workbook
from openpyxl.styles import Font

# to load and select worksheet
wb = load_workbook('report.xlsx')
worksheet = wb['Report']

worksheet['A1'] = 'Sales Report'
worksheet['A2'] = 'January'
worksheet['A1'].font = Font('Arial', bold=True, size=20)
worksheet['A2'].font = Font('Arial', bold=True, size=10)

wb.save('report_january.xlsx')



