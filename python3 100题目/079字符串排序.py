# 实例079：字符串排序
# 题目：字符串排序。
# 程序分析：无。

l=['baaa','aaab','aaba','aaaa','abaa']
t=sorted(l)
print(l)
print(t) # sorted方法可以不改变原列表

l.sort() # sort方法直接修改原列表
print(l)