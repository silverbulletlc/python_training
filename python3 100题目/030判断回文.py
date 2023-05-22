# 实例030：回文数
# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
# 程序分析：用字符串比较方便,就算输入的不是数字都ok。

# 自己抄写练习
circle=input('请输入数字')
a=0
b=len(circle)-1
flag=True
while a<b:
    if circle[a]!=circle[b]:
        flag=False
        print('不是回文')
        break
    else:
        a,b=a+1,b-1
if flag==True:
    print("是回文")

# 参考答案
n=input("随便你输入啥啦：")
a=0
b=len(n)-1
flag=True
while a<b:
    if n[a]!=n[b]:
        print('不是回文串')
        flag=False
        break
    a,b=a+1,b-1
if flag:
    print('是回文串')