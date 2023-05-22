import xlwt
wb=xlwt.Workbook()
sh=wb.add_sheet('数据')

# 字体
ft=xlwt.Font() # 形成一个实例的字体样式
ft.name='微软雅黑' # 设置字体
ft.colour_index=2 # 设置颜色
ft.height=11*20 # 设置文字大小，注意11号和excel不同，需要20作为衡量单位即倍数
ft.bold=True # 设置粗体
ft.underline=True # 设置下划线
ft.italic=True # 设置斜体

# 对齐
alg=xlwt.Alignment()
alg.horz=2 # 1左对齐，2中对齐，3右对齐
alg.vert=1 # 0上对齐，1中对齐，2下对齐

# 设置边框
border=xlwt.Borders()
# 细实线——1；小粗实线——2；细虚线——3；中细虚线——4；大粗实线——5；双线——6;细点虚线——7
# 大粗虚线——8；细点划线——9；粗点划线——10；细双点划线——11；粗双点划线——12；斜点划线——13
border.left=1
border.right=1
border.top=1
border.bottom=1
border.left_colour=1
border.right_colour=2
border.top_colour=3
border.bottom_colour=4

# 设置背景颜色
pattern=xlwt.Pattern()
pattern.pattern=xlwt.Pattern.SOLID_PATTERN # 填充实体
pattern.pattern_fore_colour=5

# 设置单元格高度
sh.row(3).height_mismatch=True # 高度要先取消相关
sh.row(3).height=10*256 # 256衡量单位
# 设置单元格宽度
sh.col(3).width=20*256

# XFstyle()为总样式集合，包含各种如字体、边框等（下面为了对比所以分开设置）
style=xlwt.XFStyle() # 形成字体样式
style.font=ft
style2=xlwt.XFStyle() # 形成对齐样式
style2.alignment=alg
style3=xlwt.XFStyle() # 形成边框样式
style3.borders=border
style4=xlwt.XFStyle() # 形成背景样式
style4.pattern=pattern
style5=xlwt.easyxf('font:bold on,height 500,color_index 6;align: vert center,horiz center')# 简便样式套用，一口气解决方便

sh.write(1,1,'梁超')
sh.write(2,2,'梁超',style)
sh.write(3,3,'梁超',style2)
sh.write(4,4,'梁超',style3)
sh.write(5,5,'梁超',style4)
sh.write(6,6,'梁超',style5)

wb.save('./create_data/04样式修改.xlsx')