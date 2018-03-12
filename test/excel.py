# -*- coding: utf-8 -*-

import xlrd

from datetime import date,datetime

def read_excel():
    ExcelFile=xlrd.open_workbook(r'C:\Users\wuzfigao\Documents\R9_M2_ProductionTestDescription_v5.xlsm')

#获取目标EXCEL文件sheet名

    print(ExcelFile.sheet_names())

#------------------------------------

#若有多个sheet，则需要指定读取目标sheet例如读取sheet2

    #sheet_name=ExcelFile.sheet_names()[5]

#------------------------------------

#获取sheet内容【1.根据sheet索引2.根据sheet名称】

    sheet=ExcelFile.sheet_by_index(5)

#打印sheet的名称，行数，列数

    #print (sheet.name,sheet.nrows,sheet.ncols)

#获取整行或者整列的值
    for i in range(0,sheet.nrows):
        print(i)
    rows=sheet.row_values(sheet.nrows-1)#第三行内容

    #cols=sheet.col_values(1)#第二列内容

    print (rows)

#获取单元格内容

    #print (sheet.cell(1,0).value.encode('utf-8'))

    #print (sheet.cell_value(1,0).encode('utf-8'))

    #print (sheet.row(1)[0].value.encode('utf-8'))

#打印单元格内容格式

    #print (sheet.cell(1,0).ctype)

if __name__ == '__main__':
    read_excel()
