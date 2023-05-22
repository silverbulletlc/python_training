# 实例095：转换时间格式
# 题目：字符串日期转换为易读的日期格式。
# 程序分析：看看就得了，dateutil是个第三方库。

from dateutil import parser
dt = parser.parse("Aug 28 2015 12:00AM")
print (dt)