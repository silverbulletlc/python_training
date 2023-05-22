# 实例092：time模块II
# 题目：时间函数举例2。
# 程序分析：如何浪费时间。
if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(3000):
        print(i)
    end = time.time()
 
    print (end - start)
