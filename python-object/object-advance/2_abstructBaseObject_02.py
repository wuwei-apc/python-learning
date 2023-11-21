"""
@FileName：2_abstructBaseObject_02.py
@Description：抽象基类
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/21 13:28
"""
from collections.abc import  Sized
from abc import  ABC,abstractmethod

# 判断对象中是否实现计算长度方法
class Student:
    def __init__(self, student_list):
        self.student_list = student_list

    def __str__(self):
        return 'Studnet类'

    def __repr__(self):
        return 'Student类'

    def __getitem__(self, item):
        return self.studnet_list[item]

    # def __len__(self):
    #     return len(self.student_list)


student =Student(["Tom","Jack"])
print(hasattr(student,'__len__'))
print("------------------------")
print(isinstance(student,Sized))


# 开发web开发框架,实现缓存

class Cache(ABC):
    @abstractmethod
    def get_cache(self):
        pass
    @abstractmethod
    def set_cache(self,value):
        pass


class MyOnline(Cache):
    def get_cache(self):
        pass
    def set_cache(self,value):
        pass

myOnline = MyOnline()
