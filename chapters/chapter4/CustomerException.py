# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : CustomerException.py
# @Created  : 2020/8/18 10:49 上午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 自定义异常
# -------------------------------------------------------------------------------

import sys

print("自定义异常-1")
print("============================")

class InvalidInput(Exception):
    pass

def customer_e1():
    raise InvalidInput("无效的输入!")

try:
    customer_e1()
except:
    print(sys.exc_info())

print()

print("自定义异常-2 ，异常中实现逻辑")
print("============================")
# 定义一个异常，实现判断用户余额不足
class NotEnoughMoney(Exception):

    def __init__(self , balance , amount):
        # 通过超类设置异常信息
        super().__init__("你的余额不足 {} ,不能提取!".format(amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance

try:
    # 可以自己尝试修改为正确的数字
    amount = 100
    balance = 50
    if balance > amount:
        print("你提取了 {} 元, 余额 {} 元".format(str(amount) , str(balance - amount)))
    else:
        raise NotEnoughMoney(balance,amount)
except NotEnoughMoney as e:
    print(str(e) , " 你提取的金额比余额多 {} 元".format(e.overage()))
print()



print("自定义异常-3 ，异常不是例外")
print("============================")

"""
2 个方法的结果一样
可以看出 execute_with_if 少了一个异常处理，但是更推荐使用异常来控制。
因为这只是一个简单的例子，现实中的例子更复杂，通过 if 判断后的结果需要在外部再进行二次过滤。过程中干扰太多，维护的值太多，代码维护性差
"""
def execute_with_exception(anumber):
    # 如果 anumber ==0 会抛出 ZeroDivisionError
    return 100 / anumber

def execute_with_if(anumber):

    if anumber == 0:
        return -1
    return 100 / anumber

try:
    print(execute_with_exception(0))
except ZeroDivisionError:
    print("无效数字，不能为 0")

result = execute_with_if(0)
if result == -1:
    print("无效数字，不能为 0")
else:
    print(result)

print()


print("自定义异常-4 ，异常不是例外，通过异常保证流程")
print("============================")
# 示例说明，商城把商品卖给客户，要保证：
# 库存不足不能销售
# 一个商品卖给一个人
# 可以理解，商品要加锁，锁定后不能卖给其他人

class InvliadItemType(Exception):
    pass

class OutOfStock(Exception):
    pass


class Inventory:

    '''
    库存，以下是一个库存的基本操作，仅仅是示例，没有代码实现
    '''

    def lock(self , item_type):
        '''
        方法将锁定 item_type 库存，以便在它被返回之前没有人可以操作该库存。 防止将同一个商品卖给不同的客户
        Select the type of item that is going to be manipulated.
        This method will lock the item so noboby else can manipulate the inventory until it is returned.
        This prevents selling the same item to two different customers.
        :param item_type:
        :return:
        '''
        pass

    def unlock(self, item_type):
        '''
        释放 item_type 库存类型，以便其他客户可以下单
        Relsase the given type so that other customers can access it
        :param item_type:
        :return:
        '''
        pass

    def purchase(self , item_type):
        '''
        If the item is not locked, raise an exception . # 如果扣除库存时，该库存未被锁定，抛出异常
        If the item type does not exist, raise an exception.    # 如果该库存类型不存在，抛出异常
        If the item is currently out of stock , raise an exception. # 如果没有库存，抛出异常
        If the item Is available , subtract one item and return the number of items left. # 以上无问题，减去一个库存，并返回库存数量
        :param item_type:
        :return:
        '''
        pass

# 下面模拟库存下单的操作。只有逻辑步骤
# 由于库存 Inventory 只构建了方法，没有内容，所以执行是没有效果的。
# 1. 用户下单，锁定库存
# 2. 对 item_type 类型的库存进行减少
# 3. 如果类型不存在，抛出 InvliadItemType 异常，反馈返回给客户
# 4. 如果库存不足，抛出 OutOfStock 异常，反馈给客户
# 5. 在 finally 中释放库存的锁
item_type = 'mobile'
inv = Inventory()
inv.lock(item_type)
try:
    num_left = inv.purchase(item_type)
except InvliadItemType:
    print("我们不销售这个 {} 类型的产品".format(item_type))
except OutOfStock:
    print("{} 类型的产品,库存不足".format(item_type))
else:
    print("下单完成 。{} 库存剩余 {}".format(item_type,num_left))
finally:
    # 释放库存，允许其他操作
    inv.unlock(item_type)