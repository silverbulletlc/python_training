# 实例005：三数排序
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：练练手就随便找个排序算法实现一下，偷懒就直接调函数。

raw=[]
for i in range(3):
    x=int(input('请输入第{}个数。'.format(i+1)))
    raw.append(x) # append方法不能直接键盘输入，要通过x变量一个个增加


for i in range(3):
    for j in range(i,3):
        if raw[i]<raw[j]:
            raw[i],raw[j]=raw[j],raw[i]
print(raw)

raw2=[]
for i in range(3):
    x=int(input('int%d: '%(i)))
    raw2.append(x)
print(sorted((raw2),reverse=False)) 
# sort()长用于对原列表进行排序，python中的内置方法sorted（）是将原列表复制一份，在副本上进行排序，而sort直接对原列表进行操作
# 通过reverse的True/False来设定顺序还是倒序排列