## 第三章 异常处理

### 异常如何产生
程序中错误是不可避免的，所有的错误类 都继承自 BaseException 类。
程序中发生错误，会导致程序直接中断。所以需要在代码里尽可能的去捕获这些异常，保证程序的稳定。

```python
dlist = [1,2,3]
print(dlist[3]) # IndexError
temp = dlist + 2 # TypeError
```

### 异常处理

```python
#语法： 普通异常处理
try:
    # 代码片段
    print("hello world")
    # 抛出异常
    raise Exception("throw excpetion")
except:
    # 异常执行
    print("cache an exception")
else:
    # 只有代码片段没有错误执行
    pass
finally:
    # 正确错误都会执行
    pass
```

示例代码: [ExceptionCase.py](/chapters/chapter4/ExceptionCase.py)

### 自定义异常

示例代码: [CustomerException.py](/chapters/chapter4/CustomerException.py)

### 示例

一个登陆，授权的例子

示例开始程序: [main.py](/chapters/chapter4/main.py)

