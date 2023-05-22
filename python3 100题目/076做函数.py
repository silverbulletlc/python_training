# 实例076：做函数
# 题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
# 程序分析：无。

# 偶数运算
def peven(n):
    i = 0
    s = 0.0
    for i in range(2,n + 1,2):
        s += 1.0 / i
    return s
 
# 奇数运算
def podd(n):
    s = 0.0
    for i in range(1, n + 1,2):
        s += 1.0 / i
    return s

# 定义选择函数的函数，这个叫隐藏函数？
def dcall(fp,n):
    s = fp(n)
    return s
 
if __name__ == '__main__':
    n = int(input('input a number: '))
    # 如果偶数，选择peven函数
    if n % 2 == 0:
        sum = dcall(peven,n)
        # sum = peven(n) # 其实这样也可以更简单，就是不经过函数选择函数
    # 如果奇数，选择podd函数
    else:
        sum = dcall(podd,n)
        # sum = podd(n) # 也可以不经过函数选择函数
    print (sum)
 