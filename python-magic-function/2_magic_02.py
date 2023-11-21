"""
@FileName：2_magic_02.py
@Description：you description
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/21 12:51
"""


class Student:
    def __init__(self, student_list):
        self.student_list = student_list

    def __getitem__(self, item):
        return self.student_list[item]

    def __len__(self):
        return len(self.student_list)

    # 自定义描述，默认为地址
    def __str__(self):
        return '这是一个自定义学生类，具有迭代和切片特性'


student = Student(["李四", "Tom", "AI"])
print(len(student))

print(student)
