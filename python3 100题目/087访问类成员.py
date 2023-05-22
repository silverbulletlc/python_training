# 实例087：访问类成员
# 题目：回答结果（结构体变量传递）。
# 程序分析：无。

if __name__ == '__main__':
    class student:
        x = 0
        c = 0
    def f(stu):
        stu.x = 20
        stu.c = 'c'
    a= student()
    a.x = 3
    a.c = 'a'
    f(a) # 虽然上面有对a.x和a.c赋值，但经过f（）函数，又重新赋值了
    print(a.x,a.c)