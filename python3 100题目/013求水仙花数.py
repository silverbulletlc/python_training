# 实例013：所有水仙花数
# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。

def is_narc(n):
    c=n%10
    b=(n%100-c)/10
    a=(n-b*10-c)/100
    if n==a**3+b**3+c**3:
        return True
    else:
        return False

for i in range(100,1000):
    if is_narc(i):
        print(i)

# 参考方案更简单，用字符串来取百十个的数字

for i in range(100,1000):
    s=str(i) #把数字变成字符串
    one=int(s[-1])
    ten=int(s[-2])
    hun=int(s[-3])
    if i == one**3+ten**3+hun**3:
        print(i)
