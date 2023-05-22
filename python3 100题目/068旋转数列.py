# 实例068：旋转数列
# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
# 程序分析：无。

from collections import *
li=[1,2,3,4,5,6,7,8,9]
deq=deque(li,maxlen=len(li))
print(li)
deq.rotate(int(input('rotate:')))
print(deq)

'''deque()可以创建一个队列容器，供我们消费，它与python的队列的区别在于deque()在增加元素的时候，
超出设定元素个数大小时，会默认删除最早的那个;同时deque不像list是一个线性存储，deque是一个双向链表，
数据量大的时候插入效率大大高于list
deque包含的方法：其中pop从队列的 尾部抛出数据，如果想从队列头部取数据则用popleft（）
'''

'''rotate的主要目的就是将【first-middle】的元素和【middle-last】的元素互换位置，middle所指向的元素会成为整个容器的第一个元素。
def rotate(self, n: int) -> None: …可以看出他需要传入的参数是int类型的一个整数【也是上面所说的middle的位置】。
​​​​​（从后往前数的位数默认从1开始）一般和collection中的deque模块配合使用，deque模块是Python标准库collections中的一项. 
它提供了两端都可以操作的序列, 这意味着, 你可以在序列前后都执行添加或删除.'''