# 实例031：字母识词
# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：这里用字典的形式直接将对照关系存好。

# 用嵌套字典来实现周一到周日
weekT={'h':'thursday',
       'u':'tuesday'}
weekS={'a':'saturday',
       'u':'sunday'}
week={'t':weekT,
      's':weekS,
      'm':'monday',
      'w':'wensday',
      'f':'friday'}
a=week[str(input('请输入第一位字母:')).lower()]# lower()表示转化小写字符串
if a==weekT or a==weekS:
    print(a[str(input('请输入第二位字母:')).lower()])
else:
    print(a)

# 巩固一下，字典的调用使用[键值]，例如下列尝试
print(week['m'])
print(week['f'])