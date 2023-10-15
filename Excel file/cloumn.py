
import openpyxl
 

path = "C:\\Users\\\Acer\\Documents\\try.xlsx"
 

wb_obj = openpyxl.load_workbook(path)
 
sheet_obj = wb_obj.active
 

print(sheet_obj.max_column)