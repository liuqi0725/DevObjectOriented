# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : ExampleClass.py
# @Created  : 2020/8/18 10:01 下午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 第五章 何时使用面向对象编程
#               论数据、行为
# -------------------------------------------------------------------------------

# 比如读取 excel
# 1. 读取特定 cell 的值
# 2. 读取总行数
# 3. 提取 row x ~ y cell 的值集合


class lxml:
    # 模拟读取 excel 的 lxml 工具。没有实际意义

    def __init__(self ,path):
        self.nrows = 0

    def get_cell_val(self, cell):
        return None

    def get_row_vals(self, row_number:int):
        return []

# ===============
# 用函数方式
# ===============
excel = lxml("path")

def read_cell_val(cells:list):
    data = []
    for cell in cells:
        data.append(excel.get_cell_val(cell))

    return data

def get_rows_val(row_number, start=0, end=0):
    vals = excel.get_row_vals(row_number)
    if vals:
       return vals[start:len(vals)]


# 调用方式
print(read_cell_val(["A4","B3","C5"]))
print(excel.nrows)
print(get_rows_val(row_number=3))


# ===============
# 用 class 方式
# ===============

class ExcelReader:

    def __init__(self, path):
        self.excel = lxml(path)

    def get_cell_val(self, cell):
        return self.excel.get_cell_val(cell)

    def get_row_number(self):
        return self.excel.nrows

    def get_row_val(self,row_number, start=0, end=0):
        vals = excel.get_row_vals(row_number)
        if vals:
            return vals[start:len(vals)]

reader = ExcelReader("path")
reader.get_cell_val("A4")
reader.get_cell_val("B3")
reader.get_cell_val("C5")
reader.get_row_number()
reader.get_row_val(row_number=5)


# 看起来用 class 的方式代码要多一点，并且不支持获取多个cell 的值
# 其实，类中的函数可以扩展，让其可以支持多个cell 的值
#
# 另外，用 class 的方式，比用函数的方式更容易让人理解。
# 维护性也更高，比如随着业务的扩展，需要读取多行的值，excel 改变 cell 颜色，修改，删除，与其他 excel 数据交换，excel 进程的打开关闭。
# 用函数的方式，代码将会变得越来越复杂，一大堆代码放在一起，可读性差，扩展性差。
# 用 class 的方式，可以通过继承的关系，抽象对象，比如 Excel 父类有打开关闭 excel 进程， 子类有 ExcelReader,ExcelWriter,MultiExcel...等。之间可以用 api 进行交互
# 这些用函数的方式，是不能将其融合在一起的。
# 使用对象，要从数据的复杂性，交互性，行为的多变性上来考虑。