# 实例011：养兔子
# 题目：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 程序分析：我认为原文的解法有点扯，没有考虑3个月成熟的问题，人家还是婴儿怎么生孩子？考虑到三个月成熟，可以构建四个数据，其中：一月兔每个月长大成为二月兔，二月兔变三月兔，三月兔变成年兔，成年兔（包括新成熟的三月兔）生等量的一月兔。

sum_of_rab=0
month_1=1
month_2=0
month_3=0
month_elder=0
month=int(input('请输入第几个月。'))

for i in range(month):
    month_1,month_2,month_3,month_elder=month_elder+month_3,month_1,month_2,month_elder+month_3
    # python独有的方法，居然可以直接实现多重赋值，交换变量也可以
sum_of_rab=month_1+month_2+month_3+month_elder

print("{}个月后，共有{}对兔子，其中一月兔子{}对，二月兔子{}对，三月兔子{}对，成年兔子{}对".format(month,sum_of_rab,month_1,month_2,month_3,month_elder))
