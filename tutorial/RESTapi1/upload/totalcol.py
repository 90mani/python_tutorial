# importing openpyxl module
import openpyxl

# Give the location of the file
path = "c:\\Users\\Admin\\Desktop\\she1.xlsx"
 

# workbook object is created
wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active

# print total number of column 
print(sheet_obj.max_column)
