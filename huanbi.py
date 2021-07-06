# -*- coding: utf-8 -*-

import pandas as pd
import os

from pandas import DataFrame

df = pd.read_excel(r'C:\Users\去\Documents\副本5月市场掌控环比.xlsx', sheet_name='市场掌控环比',skiprows=1,usecols=[28,29,30,31,32,33,34,35,36,37,38]
                   )
df_total = pd.read_excel(r'C:\Users\去\Documents\副本5月市场掌控环比.xlsx', sheet_name='市场掌控环比',skiprows=1,usecols=[28,29,30,31,32,33,34,35,36,37,38]
                   )
# df.columns = ['日均能力收入（万元）',	 '宽带净增（户）',	'个人客户净增（个）',	'三个升级',	'个人新动能（分）',	'家庭新动能（分）',	'5G终端（分）',	'5G资费（分）',	'企业微信（分）',	'分局关键过程项目综合积分（分）',	'服务负向动作扣罚'
# ]

sheet=df.columns.values
dist_down={}
dist_up={}
count=0

#降序
for i in sheet:
    i=i.replace(' ', '')

    df=DataFrame(df_total[i])
    df.columns=[i]

    i=str(i)
    df=df.sort_values(by=i,ascending=True)#升序
    df = df.reset_index(drop=True)

    dist_up[i]=str(df.loc[0,:].values)+'---'+str(df.loc[1,:].values)+'---'+str(df.loc[2,:].values)
    df = df.sort_values(by=i,ascending=False)  # 降序
    df = df.reset_index(drop=True)

    dist_down[i] = str(df.loc[0, :].values) + '---' + str(df.loc[1, :].values) + '---' + str(df.loc[2, :].values)
    print("------"+i+"中环比升序前三（最低）---")
    print(dist_up[i])

    print("------"+i+"中环比降序前三（最高）---")
    print(dist_down[i])
    print('')
    print('')
    count+=1








