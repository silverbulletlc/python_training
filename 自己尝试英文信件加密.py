# 加密原理，每个英文字符后移
# 关键的是ord和chr两个函数，分别用于字符转ASCII码和变回去

secret=(input('please input your secret words:'))
change=2 # 代表字母的后移位数
trans='' # 解码后的文
for i in secret:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        if i=='z' or i=='Z':
            # 根据需要将末端字母回调整，如果不调整就会变非字母，也可以设置特殊的转换
            num=ord(i)
            num-=25
            trans+=chr(num)
        else:
            trans+=chr(ord(i)+change) #代码可以合并一行更简单
    else: # 其它的字符比如空格、数字、标点等就不调整了
        trans+=i
print(trans)