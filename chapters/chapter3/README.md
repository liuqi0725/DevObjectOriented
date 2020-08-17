## 第三章 当对象是相似的

### 基本继承

跟 JAVA 、PHP 的意境差不多，唯一需要注意的是 `共享变量` 。详情参看 [NormalExtend_A.py](/NormalExtend_A.py)

+ 继承
+ 共享变量
+ 重写
+ super

### 重内置的类继承
跟 JAVA 的意思差不多，可以继承的内置类一般有 Object,list,dict,file,str,int,float,boolean 详情参看 [NormalExtend_B.py](/NormalExtend_B.py)

### 多重继承

python 独有，不推荐多继承。现实中需要多继承的情况少之又少。 简单示例详情参看 [MultipleExtend.py](/MultipleExtend.py)

+ 示例中有其他解决方案

### 多态

调用不同子类产生不同结果。示例查看 [NormalExtend_C.py](/NormalExtend_C.py)


### 综合案例

简单的房产租赁、销售应用系统。允许一个代理管理租赁、销售的房产。通过、继承、重写、多态、多继承来实现。示例只是为了本章内容服务，现实中可以用更好的设计方案来实现。

+ 录入房产信息
+ 列出目前手头的房产列表
+ 把一个房产标记为已租、已售

查看 [example](/example)
示例开始程序: [example/MultipleExtend.py](/example/MultipleExtend.py)
