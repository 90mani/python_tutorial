#import openpyxl module
import openpyxl

#call a workbook() function of openpyxl
#to create a new blank workbook object
wb = openpyxl.Workbook()
#Get workbook active sheet
#from the active attribute
sheet = wb.active

#once have the Worksheet object.
#one can get its name from the 
# title attribute
sheet_title = sheet.title
print("active sheet title:" + sheet_title) 