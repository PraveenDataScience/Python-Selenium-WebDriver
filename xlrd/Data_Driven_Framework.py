import xlrd
import openpyxl

wb = xlrd.open_workbook("C://Users//priya pandey//Desktop//Project//Python-Selenium-WebDriver//xlrd//DataFile.xls")
#C:\Users\priya pandey\Desktop\Project\Python-Selenium-WebDriver\xlrd\DataFile.xls
sh = wb.sheet_by_name("Sheet1")
# Total No. of rows & Column:
row=sh.nrows
col=sh.ncols
print("Row count: ",row)
print("Column count: ",col)

for data in range(1,row):
    first_name=sh.cell_value(data,0)
    last_name=sh.cell_value(data,1)
    print(first_name+" "+last_name)

