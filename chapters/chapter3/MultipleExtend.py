# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : MultipleExtend.py.py
# @Created  : 2020/8/17 11:24 上午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 多重继承
# -------------------------------------------------------------------------------


# 不推荐多重继承，在复杂条件下，会变得十分混乱。因为有多个父类，调用超类方法，实例化__init__ 的顺序会随着深度越来越复杂。
# 像下列例子，虽然抽象了对象，可以进行复用。但是还有更好的办法
# 比如 sendMail 可以：
# 1. 可以单一继承，缺点是所有需要sendMail的都需要去继承
# 2. Mail 单独为一个模块，外部直接调用即可。不需要通过继承去实现
# 3. 通过 monkey-patch 让 Contract 在其被创建的时候就有 sendMail 方法

class Contract:

    contract_list = []

    def __init__(self, name,phone,email):
        user = [name,phone,email]
        self.contract_list.append(user)

class MailSender:

    def sendMail(self, user_name , message):
        print("send mail to user:{} , message: {}".format(user_name,message))


class ContractMail(Contract, MailSender):
    pass

a = ContractMail("user-1" , "139xxxxxxx" , "test_1@aliyun.com")
b = ContractMail("user-2" , "139xxxxxxx" , "test_2@aliyun.com")

print(b.contract_list)

b.sendMail("user-1","Hello World")