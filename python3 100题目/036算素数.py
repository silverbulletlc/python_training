# 实例036：算素数
# 题目：求100之内的素数。
# 程序分析：用else执行for循环的奖励代码（如果for是正常完结，非break）

import math
def prime(n):
    for i in range(2,round(math.sqrt(n))+1):# round()函数表示四舍五入
        # 使用sqrt()平方根比n/2用的循环次数更少，可避免重复的部分
        if n>2 and n%i==0:
            return False
            break
    return True
sum=0
for i in range(2,101):
    if prime(i)==True:
        print(i)
        sum+=i
print(sum)

# 参考答案
lo=int(input('下限：'))
hi=int(input('上限：'))
sum=0
for i in range(lo,hi+1):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i)
            sum+=i
print(sum)