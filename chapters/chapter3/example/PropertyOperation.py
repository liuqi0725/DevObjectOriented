# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : Property.py
# @Created  : 2020/8/17 4:31 下午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 房产操作模块
# -------------------------------------------------------------------------------

from .Utils import get_valid_input

class Purchase:
    '''
    房产购买操作
    '''

    def __init__(self , price='' , taxes='', **kwargs):
        '''
        :param price: 价格
        :param taxes: 税费
        :param kwargs: 其他参数
        '''

        # 由于要演示多继承，所有仍然要实现父类 object 的初始化函数，因为我们不知道 super().__init__的调用顺序
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("销售情况")
        print("销售价格：{}".format(self.price))
        print("付税：{}".format(self.taxes))
        print()

    # 静态方法
    # 提供控制台选项给用户
    @staticmethod
    def prompt_init():
        return dict(
            price=input("销售价格多少?"),
            taxes = input("税费多少?"))

class Rental:
    '''
    房产租赁操作
    '''

    def __init__(self , furnished='' , utilities='', rent='' , **kwargs):
        '''
        :param furnished: 带家具
        :param utilities: 公共设施
        :param rent: 租金
        :param kwargs: 其他参数
        '''

        # 由于要演示多继承，所有仍然要实现父类 object 的初始化函数，因为我们不知道 super().__init__的调用顺序
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        # 多继承，并且顺序正确 ，才有效 。否则父类 Object 没有该方法
        super().display()
        print("出租情况")
        print("租金：{}".format(self.rent))
        print("公共设施：{}".format(self.utilities))
        print("带家具：{}".format(self.furnished))
        print()

    # 静态方法
    @staticmethod
    # 提供控制台选项给用户
    def prompt_init():
        return dict(
            rent = input("每月租金多少?"),
            utilities=input("有些什么公共设施?"),
            furnished = get_valid_input("是否带家具?" , ("yes","no")))