# pip3 install xlutils 需要安装第三方模块xlutils
import xlrd
from xlutils.copy import copy

# 打开excel
read_book=xlrd.open_workbook('./create_data/01电影数据.xlsx')
# 复制数据
wb=copy(read_book)
# 选择工作薄
sh1=wb.get_sheet(0)
# 修改单元格
sh1.write(1,1,'心花路放')

# 增加工作薄
sh2=wb.add_sheet('总分统计')
# 通过修改来统计excel内数据
count=0
rs=read_book.sheet_by_name('电影')
for r in range(1,rs.nrows):
    num=rs.cell(r,2).value
    count+=int(num)
sh2.write(0,0,'评分总和')
sh2.write(1,0,count)
wb.save('./create_data/03电影数据（统计评分）.xlsx') # 因为修改了文件名，会另存生成一个新文件