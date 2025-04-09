"""
@FileName：8_class_super.py.py
@Description：
super函数 作用：调用'父类'构造方法
@Author：zpc20 
@productName: PyCharm
@Time：2023/11/29 13:47
"""
class A:
    def __init__(self):
        print('A')

class B(A):
      def __init__(self):
          A.__init__(self)
          super().__init__()
          print('B')
b = B()
print('-------------------')

# 场景
#  1.需要类具有多线程性质
#  2. 代码重用

import threading


class mythread(threading.Thread):

    def __init__(self,thread_name, user):
        self.user = user
        # self.thread_name = thread_name
        super().__init__(name = thread_name)
