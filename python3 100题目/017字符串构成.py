# 实例017：字符串构成
# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。

string=input("输入字符串：")
alp=0
num=0
spa=0
oth=0
for i in range(len(string)):
    if string[i].isspace():# 判断空格
        spa+=1
    elif string[i].isdigit():# 判断数字
        num+=1
    elif string[i].isalpha():# 判断字母
        alp+=1
    else:
        oth+=1
print('space: ',spa)
print('digit: ',num)
print('alpha: ',alp)
print('other: ',oth)