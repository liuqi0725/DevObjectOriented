# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : Property.py
# @Created  : 2020/8/17 4:31 下午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 房产模块
# -------------------------------------------------------------------------------

from .Utils import get_valid_input

class Property:
    '''
    房产类
    '''

    def __init__(self , square_feet='' , beds='', baths='', **kwargs):
        '''
        房产基本信息,例子为了方便，没有判空，类型都为 str。现实中肯定会考虑为空，类型转化等
        :param square_feet: 平方
        :param beds: 卧室数量
        :param baths: 洗手间数量
        :param kwargs: 其他参数
        '''
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_bathrooms = baths

    def display(self):
        print("房产详情")
        print("===============")
        print("面积：{}".format(self.square_feet))
        print("卧室：{}".format(self.num_bedrooms))
        print("洗手间：{}".format(self.num_bathrooms))
        print()

    # 静态方法
    # 提供控制台选项给用户
    @staticmethod
    def prompt_init():
        return dict(
            square_feet=input("输入房产面积:"),
            beds = input("输入卧室数量:"),
            baths = input("输入洗手间数量:"))

class Apartment(Property):
    '''
    公寓，继承自房产
    '''

    # 洗衣房 ， 浴室套件
    valid_laundries = ("coin","ensuite","none")
    # 阳台 ，有、无、阳光飘窗
    valid_balconies = ("yes","no","solarium")

    def __init__(self, balcony='' , laundry='' , **kwargs):
        '''
        初始化公寓房产
        :param balcony:
        :param laundry:
        :param kwargs:
        '''
        super().__init__(**kwargs)
        self.laundry = laundry
        self.balcony = balcony

    def display(self):
        super().display()
        # 重写
        print("公寓信息")
        print("洗衣房：{}".format(self.laundry))
        print("阳台：{}".format(self.balcony))
        print()


    # 提供控制台选项给用户
    @staticmethod
    def prompt_init():
        # 获取父类命令行值，并添加子类的命令行值在里面
        parent_init = Property.prompt_init()

        laundry = get_valid_input("有哪些洗衣设备？", Apartment.valid_laundries)
        balcony = get_valid_input("有没有阳台？", Apartment.valid_balconies)

        # 调用 dict 的 update 函数更新父类的命令行值
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init


class House(Property):
    '''
    商品房 房产，继承自房产
    '''

    # 车库 , 带车位，独立车位，没有
    valid_garage = ("attached","detached","none")
    # 花园 , 有，无
    valid_fenced = ("yes","no")

    def __init__(self, num_stories='' , garage='' , fenced='', **kwargs):
        '''
        初始化 房产
        :param num_stories: 楼层
        :param garage: 车库
        :param fenced: 花园
        :param kwargs: 其他参数
        '''
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced = fenced

    def display(self):
        super().display()
        # 重写
        print("商品房详情")
        print("# 楼层 ：{}".format(self.num_stories))
        print("车位 ：{}".format(self.garage))
        print("花园 ：{}".format(self.fenced))
        print()

    # 提供控制台选项给用户
    @staticmethod
    def prompt_init():
        # 获取父类命令行值，并添加子类的命令行值在里面
        parent_init = Property.prompt_init()

        fenced = get_valid_input("是否有花园？", House.valid_fenced)
        garage = get_valid_input("有没有车位？", House.valid_garage)
        num_stories = input("有几楼?")

        # 调用 dict 的 update 函数更新父类的命令行值
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories":num_stories
        })
        return parent_init
