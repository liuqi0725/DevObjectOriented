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
#               Property 为数据添加行为
# -------------------------------------------------------------------------------

print("Property 为数据添加行为 : 获取、修改属性")
print("============================")
class User1:
    '''
    普通的用户对象，初始化传入 name，age，
    通过 .name,.age 来获取，修改属性值
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User1("hanmeimei",18)
print(user.name , user.age)
user.age = 16
print(user.name , user.age)

print()


print("Property 为数据添加行为 : 设置 Property 属性获取、修改属性")
print("============================")
class User2:
    '''
    普通的用户对象，初始化传入 name，age，
    通过 _name 把name 设置为`半私有`，添加 set、get 方法。
    然后把 get、set 方法通过 property 设置为 name 属性。
    这样外部就修改 name 值时就通过 set，获取 name 值就通过 get。
    '''
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def _set_name(self,name):
        if not name:
            raise Exception("Invalid Name. Name can`t empty")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name,_set_name)

user = User2("hanmeimei",18)
print(user.name)
try:
    # 由于 set 方法中，不能传入空值，所以这行代码会抛出异常
    user.name = ""
except Exception as e:
    print("Error:", str(e))

print()


print("Property 为数据添加行为 : 装饰器 Property")
print("============================")

class User3:
    '''
    普通的用户对象，初始化传入 name，age，
    '''
    def __init__(self, name, age):
        self._name = name
        self.age = age

    # @property 等同于 name = property(name)
    # 设置一个 name 的属性
    @property
    def name(self):
        return self._name

    # 当 name 属性生效后，就有@name.setter 装饰器，提供 set 方法
    @name.setter
    def name(self,name):
        if not name:
            raise Exception("Invalid Name. Name can`t empty")
        self._name = name

user = User3("hanmeimei",18)
print(user.name)
try:
    # 由于 set 方法中，不能传入空值，所以这行代码会抛出异常
    user.name = ""
except Exception as e:
    print("Error:", str(e))

user.name = "lilei"
print(user.name)
print()

# 一般情况下使用普通属性，只有在特定某些操作时，我们才需要用到 property。
# 下面是场景举例：

import time

print("Property 使用场景举例-1")
print("============================")
# 页面爬虫缓存数据
# 比如获取 www.baidu.com 第一次可能请求 10s，第二次就直接从属性获取了,获取 content 只执行了一次
class Test1:

    def __init__(self , url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            import urllib.request
            print("connect to url {}".format(self.url))
            content_byte = urllib.request.urlopen(self.url).read()
            content_str = str(content_byte, 'utf-8')
            self._content = content_str
            time.sleep(5)
        return self._content

t = Test1("http://www.baidu.com")
now = time.time()
content1 = t.content
end = time.time()
print("第一次：",end - now)
# 第二次
now = time.time()
content2 = t.content
end = time.time()
print("第二次：",end - now)
print()


print("Property 使用场景举例-2")
print("============================")
# 页面爬虫缓存数据
# 比如一个班级求平均分

class SchoolClass:

    def __init__(self , score_list):
        self.score_list = score_list

    @property
    def average(self):
        return sum(self.score_list) / len(self.score_list)

c = SchoolClass([99,70,95,65])
print(c.average)

print()
