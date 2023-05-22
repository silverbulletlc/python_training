# 实例006：斐波那契数列
# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），从1,1开始，后面每一项等于前面两项之和。图方便就递归实现，图性能就用循环。

# 递归实现，代码简单
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=int(input("请输入数列序号。"))
print("数列的第{}项是{}".format(n,fib(n)))

# 朴素实现,性能好
target=int(input("请输入数列序号。"))
res=0
a,b=1,1
for i in range(target-1):
    a,b=b,a+b
print("数列的第{}项是{}".format(target,a))