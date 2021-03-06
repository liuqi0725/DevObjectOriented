## 第二章 Python 对象

### 对象的定义 class 及命名
    
```python
# 驼峰命名法
class FirstClass:
    pass
```
    
### class `__init__` 函数说明

```python
class FirstClass:
    
  def __init__(self):
      # 构造函数为 __new__ 一般不用
      # 初始化函数
      pass
```

### 模块说明
py文件本身就是模块，项目大了以后，可以用文件夹组装模块。模块文件下必须包含 `__init__.py` 文件。否则无法子文件夹外用 import 导入

### docstring 编写文档说明

```python
class FirstClass:
  
  '''
      用 3 个 `'` 或者 `"` 表示 docstring
  '''

  def __init__(self):
      # 构造函数为 __new__ 一般不用
      # 初始化函数
      pass
```

### help(<className>) 查看类文档

```bash
# 命令执行
python -i menu.py
# help(<clasName>)
help(Menu)
```
### 对象 public、protected、private 
python 没有区分。都是public 的。但是有规则 ，在函数前用"__"开始表示该方法是私有，外部尽量不要调用造成错误。

### 简单的对象引用例子  
入口 menu.py
