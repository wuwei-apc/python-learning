"""
@FileName：7_class_self.py
@Description：自省机制: 检测一个类的内部结构
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/29 13:33
"""


class Person:
    """Person类
    """
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


stu = Student('西南林业')


# 查询这个类对象包含的属性
print(stu.__dict__)
print(Person.__dict__)
# python 中对象都具有一个特殊的属性: __dict__ 只能查询属于自身的属性
# 可以创建属性
stu.__dict__['address'] = "云南"
print(stu.address)
print("---------------------")
# dir 函数可以查询一个对象中的所有方法，包含这个对象的父类
print(dir(stu))#列表
