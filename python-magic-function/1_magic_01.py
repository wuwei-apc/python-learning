"""
@FileName：1_magic_01.py
@Description：python 魔法函数
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/20 22:38
"""


# 声明类
class Student:
    def __init__(self, student_list):
        self.student_list = student_list
    # 魔法方法,python 自带方法
    def __getitem__(self,item):
        # 序列特征
        return self.student_list[item]
student = Student(['李四','Tom','李华'])

# 迭代
for stud in student.student_list:
    print(stud)
print("_______________")
# 可以让当前学生类具有序列特性
for item in student:
    print(item)
print("_______________")
# 使用类似数组索引取值
print(student[1])

"""
1.魔术方法可以添加类不具有的特性
2.魔术方法是python解释器提供的，不能修改函数名
"""