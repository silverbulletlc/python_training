# 实例083：制作奇数
# 题目：求0—7所能组成的奇数个数。
# 程序分析：
# 组成1位数是4个。1,3,5,7结尾
# 组成2位数是7*4个。第一位不能为0
# 组成3位数是784个。中间随意
# 组成4位数是788*4个。
if __name__ == '__main__':
    sum = 4
    s = 4
    for j in range(2,9):
        print (sum)
        if j <= 2:
            s *= 7 # 两位数第一位不能为0
        else:
            s *= 8
        sum += s
    print('sum = %d' % sum)
 