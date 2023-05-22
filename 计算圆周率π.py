sum=0
import random
n=int(input("请输入精度，正整数"))
for i in range(n):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    if (x**2)+(y**2)<=1:
        sum+=1
pi=sum/n*4
print("估算圆周率π的值是{}".format(pi))