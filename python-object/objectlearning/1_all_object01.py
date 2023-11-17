"""
@FileName：1_all_object01.py
@Description：python object learning
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/16 22:45
"""
# 获取类的id
num = 10
print(id(num))


# 函数
def print_info(name):
    print(name)


print(id(print_info))

my_func = print_info
my_func("测试")


class Person:
    def __init__(self):
        print("测试")


print(id(Person))

my_class = Person
my_class()

# 将上述函数和类对象添加到容器中
obj_list = list()
obj_list.append(my_func)
obj_list.append(my_class)
for item in obj_list:
    print(item)


# 通过装饰器将函数作为一个参数进行传递以及返回一个函数对象
def my_wrapper(func_object):  # 当前外部函数接收的是一个函数对象
    def wrapper():
        print("这是一个装饰器")
        func_object()  # 调用外层函数所接收到的函数对象

    return wrapper  # 外部函数返回外部函数对象


@my_wrapper
def print_wrapper():
    print("函数测试！")


func_object = my_wrapper(print_wrapper)
func_object()
print("_________________________")
print_wrapper()
