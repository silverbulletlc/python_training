# 实例091：time模块
# 题目：时间函数举例1。
# 程序分析：无。
if __name__ == '__main__':
    import time
    print (time.ctime(time.time()))
    print (time.asctime(time.localtime(time.time())))
    print (time.asctime(time.gmtime(time.time())))
