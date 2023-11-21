"""
@FileName：1_Object_01.py
@Description：鸭子类型多态 多个类中实现同一个方法，那么这些类可以看做同一类型
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/21 13:07
"""

"""
方法多态
"""


class Cat:
    def say(self):
        print("猫~~")


class Dog:
    def say(self):
        print("狗~~")


class Duck:
    def say(self):
        print("鸭子~~")


# animal = Dog
# animal().say()


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


class Student:
    def __init__(self, student_list):
        self.student_list = student_list

    def __getitem__(self, item):
        return self.student_list[item]


class_student = Student(['Tom', 'Jack'])
# ---------------------Test-------------
new_student = ['Rose']
student_tuple = ('LiSi',)
new_student.extend(student_tuple)
print("____________________________")
print(new_student)

new_student.extend(class_student)
print(new_student)
"""
只要多个类实现了同一个方法，就可一归为一类
"""


# ----------------多态-------------
class Animal:
    def run(self):
        print("动物跑")


class Dog(Animal):
    def run(self):
        print("狗在跑")


class Cat(Animal):
    def run(self):
        print("猫在跑")

"""
多个类同时继承同一个类且对父类方法进行重写，每个类的实例同一个方法返回不同行为
"""
print("----------------")
dog = Dog()
dog.run()

cat = Cat()
cat.run()


