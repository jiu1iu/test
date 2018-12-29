import ddt
import unittest
import xlrd
import random
class excel:
    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        self.keys = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols
        # print(self.colNum, self.rowNum, self.keys)


    def test_data(self):
        if self.rowNum <= 1:
            print('测试数据为空')
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                s["rowNum"] = i+2
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    try:

                        values1 = int(values[x])
                        print(type(values[x]))
                        s[self.keys[x]] = values1
                    except:
                        s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

