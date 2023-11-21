"""
@FileName：4_Objectatrribut.py
@Description：类属性和实例属性
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/21 13:51
"""

class A:
    a = 1
    def __init__(self,b,c):
        # 实例属性
        self.b = b
        self.c = c

a = A(2,3)
print(a.a,a.b,a.c)
print("----------------")
print(A.a)
print("----------------")
# 类不能访问实例属性，但实例可以访问类属性
# print(A.b,A.c)
# 对类属性值修改
A.a = 11
print(A.a)
print(a.a)
# 能否使用实力对向修改类属性
a.a = 22
print("-------------------")
print(A.a) # 实例属性无法修改类属性
print(a.a) # 当前代码是通过实例对象新建一个实例属性