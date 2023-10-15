# import openpyxl module
import openpyxl
 
# Give the location of the file
path = "C:\\Users\\\Acer\\Documents\\try.xlsx"
 
# to open the workbook 
# workbook object is created
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
 
# print the total number of rows
print(sheet_obj.max_row)