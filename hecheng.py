import pandas as pd
import os
import sheet_name as sn


def hecheng():
	'''
	合成多个子表，表名按1,2,3,4,5,6……的规则进行命名
	:return:
	'''
	sheets = sn.sheet_name()
	D = []
	for x in sheets:
		data = pd.read_excel('D:/财务数据/结果居民/' + str(x) + '.xlsx', sheet_name='Sheet1')

		print(data)
		if data.empty is True:
			continue
		# data.rename(columns={'状态归类':'状态'},inplace=True)#状态归类和状态是同一个属性，所以我将状态归类替换成了状态
		D.append(data.loc[:, ['电厂（交易对象）编码', '名称', '动作标记', '发行日期', '含税电费', '月份', '钱', '合并时间']])
	num = pd.concat(D, axis=0)  # 合并list表D中的元素
	num.to_excel('D:/财务数据/结果居民/居民台账总表.xlsx', index=False)
