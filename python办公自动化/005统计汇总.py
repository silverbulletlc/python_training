import xlrd
from xlutils.copy import copy

def read_data():
    wb=xlrd.open_workbook('./base_data/data01.xls')
    sh=wb.sheet_by_index(0)
    fen_type={} # 分类价格总和{a:110,b:300}
    count_price=[] # 总价格

    for r in range(sh.nrows):
        count=sh.cell_value(r,3) * sh.cell_value(r,4)
        count_price.append(count)
        key=sh.cell_value(r,0)
        if fen_type.get(key):
            fen_type[key]+=count
        else:
            fen_type[key]=count

    return fen_type,count_price #返回分类及总价

def save(fen,count):
    wb=xlrd.open_workbook('./base_data/data01.xls')
    sh_t=wb.sheet_by_index(0)
    wb2=copy(wb)
    sh=wb2.get_sheet(0)
    for r in range(sh_t.nrows):
        sh.write(r,sh_t.ncols,count[r]) # sh_t.ncols的数代表数据后第一列空白
    
    sh2=wb2.add_sheet('汇总数据')
    for i,key in enumerate(fen.keys()): # 双遍历获取fen.key(),比如i=0,fen.keys(0)=a
        sh2.write(i,0,key)
        sh2.write(i,1,fen.get(key)) # 通过get()方法获取字典的对应值
    wb2.save('./create_data/05汇总数据.xls')

if __name__=="__main__":
    f,c=read_data()
    save(f,c)

'''备注：代码中xlrd部分内容不支持xlsx，解决方法：
一、调低xlrd版本
xlrd过高，卸载旧版本重新安装1.2.0
1、打开terminal
2、卸载现在的版本 pip uninstall xlrd
3、安装低本班xlrd：pip install xlrd==1.2.0
二、调低excel版本
excel文件的版本过高，复制源文件，另存为：xls格式
1、在报错的excel文件所在的文件夹里可以新建一个excel文件，将文件格式设置成Excel97―2003工作薄（.xls），
不能设置成WPS加密文档格式(*xls)格式，名称必须为：new.xls（名称可以自定义，后缀必须一致，而且必须用
office/wps创建，如果名称后缀与原excel一致，保存时需要替换原文件，切记不能自己新建一个文件，然后修改后缀）
原文链接：https://blog.csdn.net/qq_45975931/article/details/128379809'''