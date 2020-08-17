# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : NormalExtends.py
# @Created  : 2020/8/17 10:12 上午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 继承基本类型
# -------------------------------------------------------------------------------

class NameList(list):

    def search(self , filter):
        '''
        集合类提供 search 返回所有找到的对象
        :param filter:
        :return:
        '''
        # 这里的循环用 self ，self 本身就是 list
        return [name for name in self if filter in name]

class Names:

    # 这里用类，不是用[] 。意思都是创建一个 list，但是原生的 list 不具备 search 函数
    # 依然是共享变量
    names = NameList()

    def __init__(self, name):
        self.names.append(name)

a = Names("alex")
b = Names("alexliu")
c = Names("John")

# 测试共享变量，每个子类添加的变量，都会主动添加到父类的集合中
print("测试共享变量-A：", a.names)
print("测试共享变量-B：", b.names)
print("测试共享变量-C：", c.names)