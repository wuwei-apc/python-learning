"""
@FileName：3_python_inner_type.py
@Description：python 内置类型
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/20 22:30
"""
"""
对象的三个特征:
     1.唯一标识
     2.类型
     3.值
"""

a = 1

print(id(a))
print(type(a))
print(a)

def my_func():
    pass
print("_______________")
print(id(my_func))
print(type(my_func))
print(my_func)

class User:
      pass
print("_______________")
print(id(User))
print(type(User))
print(User)

# None 类型 全局只有一个
data_1 = None
data_2 = None
print("_______________")
print(id(data_1))
print(id(data_2))

