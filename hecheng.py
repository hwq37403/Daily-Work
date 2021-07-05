import pandas as pd
import os
#合成文件的上一级文件夹路径
path = "C:\\Users\\去\\Documents"
# 合成excel的列名
list = ['电厂（交易对象）编码', '名称', '动作标记', '发行日期', '含税电费', '月份', '钱', '合并时间']
#合成总表结果存放路径
out_path=path+'\\合成总表.xlsx'

def hecheng():
	'''
	合成多个子表，表路径为path下的xlsx文件,只需修改path，
	:return: void
	'''
	sheets = os.listdir(path)  # 获取path目录下的所有excel
	D = []
	for x in sheets:
		data = pd.read_excel(path + str(x) + '.xlsx', sheet_name='Sheet1')

		print(data)
		if data.empty is True:
			continue
		# data.rename(columns={'状态归类':'状态'},inplace=True)#状态归类和状态是同一个属性，所以我将状态归类替换成了状态
		D.append(data.loc[:, list])
	num = pd.concat(D, axis=0)  # 合并list表D中的元素
	num.to_excel(out_path, index=False)

if __name__ == '__main__':
    hecheng()