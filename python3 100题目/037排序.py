# 实例037：排序
# 题目：对10个数进行排序。
# 程序分析：同实例005。

raw=[]
for i in range(10):
    x=int(input('请输入第{}个整数'.format(i+1)))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i]>raw[j]:
            raw[i],raw[j]=raw[j],raw[i]
print(raw)
