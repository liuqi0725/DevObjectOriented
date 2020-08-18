# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : test.py
# @Created  : 2020/8/18 9:49 上午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 异常案例
# -------------------------------------------------------------------------------
import sys

print("异常案例-1 : 捕获异常")
print("============================")
def test_fn1(anumber):
    '''
    捕获异常
    :param anumber:
    :return:
    '''
    try:
        return 100/anumber
    except:
        print("something wrong with 100/",anumber)

test_fn1(0)
print()

print("异常案例-2 : 捕获指定异常")
print("============================")
def test_fn2(anumber):
    '''
    捕获指定异常
    :param anumber:
    :return:
    '''
    try:
        return 100 / anumber
    except ZeroDivisionError:
        print("ZeroDivisionError happened with 100/", anumber)

test_fn2(0)
print()



print("异常案例-3 : 捕获指定异常,同一个 except 捕获多个异常")
print("============================")
def test_fn3(anumber):
    '''
    捕获指定异常
    :param anumber:
    :return:
    '''
    try:
        return 100 / anumber
    except (ZeroDivisionError,TypeError):
        print("ZeroDivisionError or TypeError happened with 100/", anumber)

test_fn3(0)
test_fn3("s")
print()


print("异常案例-4 : 捕获指定异常，捕获多个异常")
print("============================")
def test_fn4(anumber):
    '''
    捕获指定异常
    :param anumber:
    :return:
    '''
    try:
        if anumber == 20:
            raise ValueError("20 不是幸运号码")
        return 100 / anumber
    except ZeroDivisionError:
        print("ZeroDivisionError happened with 100/", anumber)
    except TypeError:
        print("TypeError happened with 100/", anumber)
    except ValueError:
        print("ValueError happened with 100/", anumber)
        raise # 将异常继续抛到方法外

test_fn4(0)
test_fn4("s")
try:
    test_fn4(20)
except:
    # 处理异常，否则下面代码无法执行
    print(sys.exc_info())

print()


print("异常案例-5 : 异常别名")
print("============================")
def test_fn5(anumber):
    '''
    捕获异常
    :param anumber:
    :return:
    '''
    try:
        return 100 / anumber
    except Exception as e: # 别名异常，可以取异常信息
        print("something wrong ", e.args)
        print("something wrong ", str(e))

test_fn5(0)
print()



print("异常案例-6 : 异常 else,finally")
print("============================")

import random
some_error = [TypeError,ValueError,IndexError,None]
def test_fn6():
    '''
    捕获异常比较全面的情况
    :param anumber:
    :return:
    '''
    try:
        error = random.choice(some_error)
        if error:
            raise error("An Error")
    except TypeError:
        print("cache TypeError")
    except ValueError:
        print("cache ValueError")
    except IndexError:
        print("cache IndexError")
    else:
        # 代码片段没有异常时执行
        print("No Error")
    finally:
        # 不管正确错误，都会执行
        print("always run")

test_fn6()
test_fn6()
test_fn6()
test_fn6()
print()

