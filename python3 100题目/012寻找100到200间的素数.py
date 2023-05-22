# 实例012:100到200的素数
# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 

def is_prime(n):
    for i in range(2,int(n/2)):
        if n%i==0:
            return False
            break
    return True

for i in range(100,201):
    if is_prime(i)==True:
        print(i)
