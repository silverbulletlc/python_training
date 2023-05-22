# 实例067：交换位置
# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
# 程序分析：无。

li=[3,2,5,7,8,1,5]
# 通过max、min和index可以追溯倒最大、小值的序号
num_of_max=(li.index(max(li)))
num_of_min=(li.index(min(li)))

li[0],li[num_of_max]=li[num_of_max],li[0]
li[-1],li[num_of_min]=li[num_of_min],li[-1]
 
# m=li[0]
# ind=li.index(max(li))
# li[0]=li[ind]
# li[ind]=m
 
print(li)