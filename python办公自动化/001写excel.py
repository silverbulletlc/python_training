# pip3 install xlwt 要先安装第三方库xlwt
import xlwt
# 创建一个excel
wb=xlwt.Workbook()
# 选择工作薄
sh=wb.add_sheet('电影')
# 写入数据到单元格
sh.write(0,0,'序号') # 行号+列号
sh.write(0,1,'电影名') # 行号+列号
sh.write(0,2,'评分') # 行号+列号
sh.write(1,0,'1') # 行号+列号
sh.write(1,1,'生化危机') # 行号+列号
sh.write(1,2,'95') # 行号+列号
sh.write(2,0,'2') # 行号+列号
sh.write(2,1,'黑天鹅') # 行号+列号
sh.write(2,2,'60') # 行号+列号
sh.write(3,0,'3') # 行号+列号
sh.write(3,1,'变形金刚') # 行号+列号
sh.write(3,2,'70') # 行号+列号
# 保存excel
wb.save('./create_data/01电影数据.xlsx')

# 备注：vscode里预览office文件要安装“office viewer”