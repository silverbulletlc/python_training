# 实例071：输入和输出
# 题目：编写input()和output()函数输入，输出5个学生的数据记录。
# 程序分析：无。

N = 3 # 一共三个学生
# stu 所有学生的档案
# num : string
# name : string
# score[4]: list
student = []
for i in range(5):
    student.append(['','',[]]) # 每个学生生成1个子序列，序号+名字+分数空序列
 
def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('input student num:\n')
        stu[i][1] = input('input student name:\n')
        for j in range(3):# 每人连续输入三个分数
            stu[i][2].append(int(input('score:\n')))
 
def output_stu(stu):
    for i in range(N):
        print ('%-6s%-10s' % ( stu[i][0],stu[i][1] ))
        for j in range(3):
            print ('%-8d' % stu[i][2][j])
 
if __name__ == '__main__':
    input_stu(student)
    print (student)
    output_stu(student)
