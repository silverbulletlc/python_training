# 实例025： 阶乘求和
# 题目：求1+2!+3!+...+20!的和。
# 程序分析：1+2!+3!+...+20!=1+2(1+3(1+4(...20(1))))

# 定义阶乘函数
def factorial(n):
    t=1
    for i in range(1,n+1):
        t=t*i
    return t

res=0
for i in range(1,21):
    res+=factorial(i)
print(res)

# 参考答案，确实更简单，但要能想到运算方式
res=1
for i in range(20,1,-1): # 20到1，每次间隔为-1
    res=i*res+1
print(res)