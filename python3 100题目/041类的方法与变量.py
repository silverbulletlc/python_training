# 实例041：类的方法与变量
# 题目：模仿静态变量的用法。
# 程序分析：构造类，了解类的方法与变量。

def dummy():
    i=0
    print(i)
    i+=1

class cls:
    i=0
    # Python在类中定义方法的时候，方法会被传进一个参数，即当前对象的地址，所以一般在类中定义方法的时候，必须在方法中至少定义一个参数（一般约定self）
    def dummy(self):
        print(self.i)
        self.i+=1

a=cls()
for j in range(50):
    dummy()
    a.dummy()# 实例a中的i（a.i）是一个参数，会持续递增