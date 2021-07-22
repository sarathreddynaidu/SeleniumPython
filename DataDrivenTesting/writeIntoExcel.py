import openpyxl

filePath = "C:\SeleniumPython\DataDrivenTesting\TestData.xlsx"

workbook = openpyxl.load_workbook(filePath)
sheet = workbook.active

for r in range(1, 6): # 5 rows
    for c in range(1, 4): # 3 columns
        sheet.cell(row=r, column=c).value = "Hello"

workbook.save(filePath)
