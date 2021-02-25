import pandas as pd
import openpyxl

###由于PD会覆盖重写sheet，为了保存一个EXCEL多个sheet，所有只能通过EXCELwriter使用一个句柄来写入多个sheet

'''
区县分局承包拆分表格
'''

file1 = pd.read_excel('E:\\WORK\\202101网格承包\\网格承包202101 - 专业室 - 副本.xlsx', sheet_name='分局汇总')
file2 = pd.read_excel('E:\\WORK\\202101网格承包\\网格承包202101 - 专业室 - 副本.xlsx', sheet_name='应知应会扣罚')
file3 = pd.read_excel('E:\\WORK\\202101网格承包\\网格承包202101 - 专业室 - 副本.xlsx', sheet_name='服务负向动作扣罚（数据未出）')
file4 = pd.read_excel('E:\\WORK\\202101网格承包\\网格承包202101 - 专业室 - 副本.xlsx', sheet_name='分局奖金包基数')

menu1 = file1.iloc[:, 2].drop_duplicates()  ########2
menu2 = file2.iloc[:, 0].drop_duplicates()  ########0
menu3 = file3.iloc[:, 0].drop_duplicates()
menu4 = file3.iloc[:, 0].drop_duplicates()

print(file1)
print(file2)
print(file3)
print(file4)

for name1,name2,name3,name4 in zip(menu1,menu2,menu3,menu4):
    df1 = file1[file1['区县'] == name1]
    df2 = file2[file2['区县'] == name2]
    df3 = file3[file3['区县'] == name3]
    df4 = file4[file4['区县'] == name4]



    path = "C:\\Users\\Admin\\Desktop\\网络承包区县拆分\\" + name1[0:2] + ".xlsx"

    #index隐藏序列号
    with pd.ExcelWriter(path) as writer:
        df1.to_excel(writer, sheet_name='分局汇总', index=None)
        df2.to_excel(writer,sheet_name='应知应会扣罚',index=None)
        df3.to_excel(writer, sheet_name='服务负向动作扣罚（数据未出）', index=None)
        df4.to_excel(writer, sheet_name='分局奖金包基数', index=None)








