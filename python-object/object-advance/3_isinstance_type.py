"""
@FileName：3_isinstance_type.py
@Description：isinstance type
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/21 13:46
"""
class A:
    pass

class B(A):
    pass

# 判断传入的对象是否是指定类型
# 也判断类的继承关系
b = B()
print(isinstance(b,B))
print(isinstance(b,A))
print('-------------------------')
# == 是判断值是否相等
print(type(b)==B)
print(type(b)==A)
print('-------------------------')
# is 判断内存地址
print(type(b) is B)
print(type(b) is A)