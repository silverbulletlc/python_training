# 实例019：完数
# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
# 程序分析：将每一对因子加进集合，在这个过程中已经自动去重。最后的结果要求不计算其本身。

def is_factor(n):
    sum=0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            sum+=i
    if n==sum:
        return True
    else:
        return False

for i in range(1,1001):
    if is_factor(i)==True:
        print(i)

# 原参考答案
def factor(num):
    target=int(num)
    res=set() # 将一个数的因数形成一个集合，集合本身就不可重复
    for i in range(1,num): # 其实不包含自身，感觉循环不用到自身，到一半就行
        if num%i==0:
            res.add(i)
            res.add(num/i) # 本条如果删除，则30行就不用减i
    return res
 
for i in range(2,1001):
    if i==sum(factor(i))-i:
        print(i)
