"""
@FileName：5_atrributSearch.py
@Description：属性值查找顺序
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/21 13:59
"""


# class A:
#     name = 'class_A'
#     def __init__(self):
#         pass
#         # self.name = 'obj_a'


# 首先查找实例属性,查找从上往上查找
# a = A()
# print(a.name)


# 菱形继承

class D:
    name = "class_D"


class B(D):
    name = "class_B"


class C(D):
    name = "class_C"


class A(B, C):
    pass


a = A()
print(a.name)
print(type(a))
print(A.__bases__)
print(A.__mro__)
print("------------------------")


# 树状继承
class E:
    name = 'E-Tom'


class F:
    name = 'F-Tom'


class G(E):
    name = 'G-Tom'


class H(F):
    name = 'H-Tom'


class A1(H, G):
    pass


a1 = A1()
print(a1.name)
print(A1.__bases__)
print(A1.__mro__)
