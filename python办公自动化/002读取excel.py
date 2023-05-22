# pip3 install xlrd 安装第三方模块xlrd
import xlrd
# 打开excel
wb=xlrd.open_workbook('./create_data/01电影数据.xlsx')
# 了解工作薄
print(f'excel中有{wb.nsheets}个工作薄') # nsheets是属性
print(f'excel中有sheets的名字是：{wb.sheet_names()}') # sheets_names()是方法
# 选择工作薄
sh1=wb.sheet_by_index(0) # 通过序号来锁定工作薄
sh2=wb.sheet_by_name('电影') # 通过名称来锁定工作薄
# 分析行列
print(f'sheet里一共有{sh1.nrows}行，{sh2.ncols}列数据')
# 获取单元格的数据
print(f'第一行第一列数据：{sh1.cell_value(0,0)}') # 通过锁定单元格的坐标
print(f'第一行第一列数据：{sh1.cell(0,0).value}') # 换一种写法
print(f'第一行第一列数据：{sh1.row(0)[0].value}') # 再换一种写法，锁定行数，在找列

# 获取整行/列数据
print(sh1.row_values(0))
print(sh1.col_values(0))

# 遍历所有数据
for r in range(sh1.nrows):
    for c in range(sh1.ncols):
        print(f'第{r}行{c}列的数据是{sh1.cell(r,c).value}')