

import openpyxl
 
path = "C:\\Users\\\Acer\\Documents\\try.xlsx"
 
wb_obj = openpyxl.load_workbook(path)
 
sheet_obj = wb_obj.active

cell_obj = sheet_obj.cell(row = 4, column = 4)
 
 
print(cell_obj.value)
