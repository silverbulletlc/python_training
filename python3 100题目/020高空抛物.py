# 实例020：高空抛物
# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# 程序分析：无

# 应该用序列，而不能用集合、元祖，元祖不能更改，集合重复的会被剔除
high_list=list() 
high=100
high_list.append(high)
s_list=list()
s=100
s_list.append(s)

for i in range(10):
    high=high/2
    s=high*2
    high_list.append(high)
    s_list.append(s)
print(high_list)
print(s_list)
print(sum(s_list))

#参考答案，虽然参考答案更简单，但是我自己的更加严密完整
high=200.
total=100
for i in range(10):
    high/=2
    total+=high
    print(high/2)
print('总长：',total)

