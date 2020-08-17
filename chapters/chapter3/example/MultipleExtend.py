# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : Property.py
# @Created  : 2020/8/17 4:31 下午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 多继承
# -------------------------------------------------------------------------------

from chapters.chapter3.example.Property import House,Apartment
from chapters.chapter3.example.PropertyOperation import Rental,Purchase
from chapters.chapter3.example.Utils import get_valid_input

class HouseRental(Rental,House):
    # 这里注意继承的顺序 Rental(租赁)， House(商品房)
    # 如果是反过来，那么调用 display 将缺失数据
    # + 继承顺序：Rental,House 的 display() 执行步骤.
    #   - Rental 类的 display() -> super().display() [super=House] -> House.display() -> Property.display()
    # + 继承顺序：House,Rental 的 display() 执行步骤.
    #   - House 类的 display() -> Property.display()  会缺失 Rental.display() 数据

    '''
    租赁商品房
    '''


    # 获取 租赁 商品房 的控制台命令
    @staticmethod
    def prompt_init():
        # 获取 商品房 命令行
        house_init = House.prompt_init()
        # 获取 出租命令行
        rental_init = Rental.prompt_init()
        # 通过更新dict 方式，合并 dict
        house_init.update(rental_init)
        return house_init


class HousePurchase(Purchase, House):
    '''
    出售商品房
    '''

    # 获取 租赁 商品房 的控制台命令
    @staticmethod
    def prompt_init():
        # 获取 商品房 命令行
        house_init = House.prompt_init()
        # 获取 出租命令行
        purchase_init = Purchase.prompt_init()
        # 通过更新dict 方式，合并 dict
        house_init.update(purchase_init)
        return house_init


class ApartmentRental(Rental,Apartment):
    '''
    租赁 公寓
    '''

    # 获取 租赁 公寓 的控制台命令
    @staticmethod
    def prompt_init():
        # 获取 商品房 命令行
        apartment_init = Apartment.prompt_init()
        # 获取 出租命令行
        rental_init = Rental.prompt_init()
        # 通过更新dict 方式，合并 dict
        apartment_init.update(rental_init)
        return apartment_init


class ApartmentPurchase(Purchase, Apartment):
    '''
    出售 公寓
    '''

    # 获取 销售 公寓 的控制台命令
    @staticmethod
    def prompt_init():
        # 获取 公寓 命令行
        apartment_init = Apartment.prompt_init()
        # 获取 出售命令行
        purchase_init = Purchase.prompt_init()
        # 通过更新dict 方式，合并 dict
        apartment_init.update(purchase_init)
        return apartment_init


class Agent:
    '''
    代理
    '''

    def __init__(self):
        # 房产列表
        self.property_list = []
        # 返回一个操作列表
        self.choices = {
            "1" : self.display_properties,
            "2" : self.add_property
        }

    def display_menu(self):
        print("""
1. 显示房产列表
2. 添加房产        
""")

    def run(self):
        while True:
            self.display_menu()
            choice = input("请选择:")
            action = self.choices.get(choice)
            if not action:
                print("输入无效!")
            else:
                action()

    def display_properties(self):
        '''
        显示所有房产
        :return:
        '''
        for property in self.property_list:
            property.display()

    type_map = {
        ("商品房","出租") : HouseRental,
        ("商品房", "出售"): HousePurchase,
        ("公寓", "出租"): ApartmentRental,
        ("公寓", "出售"): ApartmentPurchase,
    }

    def add_property(self):

        property_type = get_valid_input("什么类型的房产",("商品房","公寓"))
        payment_type = get_valid_input("什么付款类型",("出租","出售"))

        # 获取实体类
        PropertyClass = self.type_map[(property_type,payment_type)]

        # 获取入参
        init_args = PropertyClass.prompt_init()

        # 添加房产
        self.property_list.append(PropertyClass(**init_args))


Agent().run()