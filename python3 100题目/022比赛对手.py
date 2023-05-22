# 实例022：比赛对手
# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
# 有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
# 程序分析：找到条件下不重复的三个对手即可。

# 参考答案
a=set(['x','y','z'])
b=set(['x','y','z'])
c=set(['x','y','z'])
c-=set(('x','z'))
a-=set('x')
for i in a:
    for j in b:
        for k in c:
            if len(set((i,j,k)))==3: # 集合会删除重复的元素，如果有三个元素则说明都不同
                print('a:%s,b:%s,c:%s'%(i,j,k))

# 自己改写更简单一点
print('自己改写后')
a=set({'y','z'})
b=set({'x','y','z'})
c=set('y')
for i in a:
    for j in b:
        for k in c:
            if len(set((i,j,k)))==3: # 集合会删除重复的元素，如果有三个元素则说明都不同
                print('a:%s,b:%s,c:%s'%(i,j,k))