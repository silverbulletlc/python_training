# 实例001：数字组合
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：遍历全部可能，把有重复的剃掉。

# 常规方法
total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
                if i!=j & j!=k & k!=i:
                    print(i,j,k)
                    total+=1
print(total)

# 采用itertools导入
import itertools
sum2=0
a=[1,2,3,4]
for i in itertools.permutations(a,3):# permutations(a,3)代表从a序列中取3项的全排列，此外combinations是全组合
    print(i)
    sum2+=1
print(sum2)