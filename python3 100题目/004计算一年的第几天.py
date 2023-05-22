# 实例004：这天第几天
# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：特殊情况，闰年时需考虑二月多加一天：

# 判断年份是否是闰年
def is_Leap_Year(y):
    if y%400==0 or (y%100!=0 and y%4==0):
        return True
    else:
        return False
# 判断闰年可以更简单“return (y%400==0 or (y%4==0 and y%100!=0))”

# 输入年月日，需要转为为int整数类型
y=int(input("请输入年，四位整数。"))
m=int(input("请输入月份，1~12。"))
d=int(input("请输入日期，1~31。"))

sum=0
# 通过序列把每个月的总天数罗列，第一个0站位，最后12月31天可以省略
Day_of_Month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if is_Leap_Year(y)==True:
    Day_of_Month[2]=29
for i in range(m):
    sum+=Day_of_Month[i]
sum+=d
print("这是当年的第{}天".format(sum))