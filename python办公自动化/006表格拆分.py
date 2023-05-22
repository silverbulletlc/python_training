import xlrd
from xlutils.copy import copy

def get_data():
    wb = xlrd.open_workbook('./base_data/data01.xls')
    sh = wb.sheet_by_index(0)
    all_data = {} # 整体数据做成大字典，{a:[{}{}{}],b:[{}{}{}],c:[{}{}{}]},字典套列表，列表里再套字典
    for r in range(sh.nrows):
        # 因为列不多，所以可以不用循环，直接用字典来做;字典比列表方便，不用记下标，可以用key
        d = {'type':sh.cell_value(r,1),'name':sh.cell_value(r,2),'count':sh.cell_value(r,3),'price':sh.cell_value(r,4)}
        key = sh.cell_value(r,0)
        if all_data.get(key):
            all_data[key].append(d) # all_data[key]是一个序列，所以可以用append（）
        else:
            all_data[key] = [d] # 注意d是字典，要放进去序列[d]，这样后面才能append（），所以必需方括号
    return all_data

def save(data):
    wb = xlrd.open_workbook('./base_data/data01.xls')
    wb2 = copy(wb)
    for key in data.keys():
        temp_sheet = wb2.add_sheet(key)
        for i,d in enumerate(data.get(key)):
            temp_sheet.write(i,0,d.get('type'))
            temp_sheet.write(i,1,d.get('name'))
            temp_sheet.write(i,2,d.get('count'))
            temp_sheet.write(i,3,d.get('price'))
    wb2.save('./create_data/06拆分表格.xls')

if __name__ == "__main__":
    f = get_data()
    save(f)