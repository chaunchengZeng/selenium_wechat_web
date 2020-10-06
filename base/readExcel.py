# coding=utf-8
import xlrd
import os


class ExcelUtil(object):
    def __init__(self, excel_path, sheet_name="Sheet1"):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)

        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取行数
        self.row_num = self.table.nrows
        # 获取列数
        self.col_num = self.table.ncols

    def dict_data(self):
        if self.row_num <= 1:
            print("总行数小于等于1")
        else:
            r = []
            j = 1
            for i in range(self.row_num-1):
                s = {}
                # 从第二行开始读取对应的value值
                values = self.table.row_values(j)
                for x in range(self.col_num):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == "__main__":
    project_path = os.path.dirname(os.path.dirname(__file__))
    file_path = project_path + r'/common/data.xlsx'
    print(file_path)
    data = ExcelUtil(file_path)
    print(data.dict_data())
    print(data.dict_data()[0]['user'])
