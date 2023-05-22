# 实例042：变量作用域
# 题目：学习使用auto定义变量的用法。
# 程序分析：python中的变量作用域。

i=0
n=0
def dummy():
    # 函数里的i是内部变量，和外部不发生关系
    i=0
    print(i)
    i+=1
def dummy2():
    global n # n为全局变量和外部发生关系，是同一个n，也就是函数内可以修改外部的参数n
    print(n)
    n+=1
print('函数内部的同名变量')
for j in range(20):
    print(i)
    dummy()
    i+=1
print('global声明同名变量')
for k in range(20):
    print(n)
    dummy2()
    n+=10
