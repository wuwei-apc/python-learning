"""
@FileName：2_all_object02.py
@Description：python object 02
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/20 22:09
"""
a = 1

b = 'abc'

# type 可以判断一个对象类型，并且type也可以是用于创建类
print(type(a))

# 一切皆对象，对象是由类创建而来
print(type(int))

"""
python中的数据类型是由类型类创建而来
python中的类型是由type创建出来的
"""
print(type(b))
print(type(str))

"""
python 中的所有对象由type创建而来
"""


class User:
    pass


class Student(User):
    pass


user = User()
print(type(user))
print(type(User))

student = Student()
print(type(student))
print(type(Student))
# __________________________________
# python 中的Object(超类（顶级类）)类
print(int.__bases__) #查询继承关系
print(User.__bases__) #默认继承object类
print(Student.__bases__)
# type创建了所有的对象，object也是一个对象
print(type(object))
print(type.__bases__)

"""
1.object是被type创建
2.type继承object
"""
print(object.__bases__)

#__________________

# type本身被自己创建
print(type(type))
