# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : NormalExtends.py
# @Created  : 2020/8/17 10:12 上午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 普通继承
# -------------------------------------------------------------------------------

class ParentClass:

    # 这个成员变量很有意思，因为他每次都会新建子类都会实例化，他有一个特性是 "实例共享"，特点如下：
    # 1. 每次新建子类/父类时，这个列表因为都会被显示的实例化，所有都会把当前所有该对象的实例中的共享变量值赋值给这个属性
    # 2. 所有子类共享这个变量，直到子类显示的去修改这个变量
    # 3. 子类显示的修改，仅能修改子类变量内容，并不能影响共享变量的数据
    # 4. 子类显示的修改这个变量后，该变量就不会再随新增的子类，改变这个值
    # 如果你不希望实现这种目的。可以设置为 None 或者在 __init__ 中用 self 去新建
    names = []

    def __init__(self, name):
        self.names.append(name)
        print("我是父类共享变量 append name {}".format(name))

    def search(self,filter):
        return [name for name in self.names if filter in name]

class ChildrenClass(ParentClass):
    pass

a = ChildrenClass("alex")
b = ChildrenClass("alexliu")
c = ChildrenClass("John")

# 测试共享变量，每个子类添加的变量，都会主动添加到父类的集合中
print("测试共享变量-A：", a.names)
print("测试共享变量-B：", b.names)
print("测试共享变量-C：", c.names)

# 测试修改共享变量
a.names = ["libai","zhangsanfeng","zhangwuji"]
b.names = ["ig","tes","lgd","fpx"]
c.names = []

print("测试修改后的共享变量-A：", a.names)
print("测试修改后的共享变量-B：", b.names)
print("测试修改后的共享变量-C：", c.names)

# 测试修改共享变量后，其他子类能否共用 , ！！！不能！！！
assert not a.search("tes")
assert not b.search("san")
assert not c.search("alex")
print("测试修改共享变量后，其他子类能否共用：【不能】通过")

# 继续测试新增子类
d = ChildrenClass("lucy")
e = ChildrenClass("lily")
f = ChildrenClass("mike")

print("继续测试新增子类共享变量情况-A：", a.names)
print("继续测试新增子类共享变量情况-B：", b.names)
print("继续测试新增子类共享变量情况-C：", c.names)
print("继续测试新增子类共享变量情况-D：", d.names)
print("继续测试新增子类共享变量情况-E：", e.names)
print("继续测试新增子类共享变量情况-F：", f.names)

print("--------------------------------------------------")

# 共享变量为 None 时
class ParentClassB:

    names = None

    def __init__(self, name):
        self.names = []
        self.names.append(name)
        print("我是父类 append name {}".format(name))

    def serch(self,filter):
        return [name for name in self.names if filter in name]

class ChildrenClassB(ParentClassB):

    # 重写 init 调用父类的 init
    def __init__(self, name):
        name = name+"_override"
        super().__init__(name)

a1 = ChildrenClassB("lucy")
b1 = ChildrenClassB("lily")
c1 = ChildrenClassB("mike")

print("测试共享变量为 None 时情况-A：", a1.names)
print("测试共享变量为 None 时情况-B：", b1.names)
print("测试共享变量为 None 时情况-C：", c1.names)