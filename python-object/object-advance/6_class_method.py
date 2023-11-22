"""
@FileName：6_class_method.py
@Description：类方法
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/22 13:11
"""


class Student:
    address = '长沙'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 实例方法可以访问类中的所有属性和方法
    def set_info(self):
        self.age = 20
        print(self.address)

    # 静态方法:无法访问类中的属性和方法
    @staticmethod
    def parse_from_string_1(stu_info):
        name, age, gender = tuple(stu_info.split(','))
        return Student(name, age, gender)

    # 可以被类对象和实例对象调用，类方法可以访问类属性
    @classmethod
    def parse_from_string_2(cls, stu_info):
        name, age, gender = tuple(stu_info.split(','))
        print(cls.address)
        return cls(name, age, gender)

    def __str__(self):
        return f'{self.name},{self.age},{self.gender}'


stud = Student('Tom', 18, 'M')
print(stud)
stud.name = 'TOM'
print(stud)
stud.set_info()
print("------------------------")
stud1 = Student.parse_from_string_1('Tom,20,M')
print(stud1)

stud_3 = Student.parse_from_string_2('Tom1,23,W')
print(stud_3)
