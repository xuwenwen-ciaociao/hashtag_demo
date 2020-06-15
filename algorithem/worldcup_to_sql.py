# import pandas as pd
# import pymysql
#
# db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='hashtag_demo')
# # 自动确认commit True
# db.commit()
# # 设置光标
# cursor = db.cursor()
#
# origin_data = pd.read_csv('E:/文档/调研/推荐系统/hashtag/worldcup_2018_tweets.csv', encoding='utf-8', usecols=[0,2,5,6,7,8,9,12,14,15])
# df2 = origin_data.astype(object).where(pd.notnull(origin_data), None)
# columns = df2.columns.tolist()
# types = df2.ftypes
# # 添加id 制动递增主键模式
# make_table = []
# for item in columns:
#     if 'int' in types[item]:
#         char = item + ' INT'
#     elif 'float' in types[item]:
#         char = item + ' FLOAT'
#     elif 'object' in types[item]:
#         char = item + ' VARCHAR(4096)'
#     elif 'datetime' in types[item]:
#         char = item + ' DATETIME'
#     make_table.append(char)
# make_table = ','.join(make_table)
#
# # 一个根据pandas自动识别type来设定table的type
# # def make_table_sql(DataFrame):
# #     columns = DataFrame.columns.tolist()
# #     types = DataFrame.ftypes
# #     # 添加id 制动递增主键模式
# #     make_table = []
# #     for item in columns:
# #         if 'int' in types[item]:
# #             char = item + ' INT'
# #         elif 'float' in types[item]:
# #             char = item + ' FLOAT'
# #         elif 'object' in types[item]:
# #             char = item + ' VARCHAR(4)'
# #         elif 'datetime' in types[item]:
# #             char = item + ' DATETIME'
# #         make_table.append(char)
# #     return ','.join(make_table)
#
# # csv 格式输入 mysql 中
# def csv2mysql(db_name, table_name, df, date):
#     cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(db_name))
#     #选择连接database
#     db.select_db(db_name)
#     # 创建table
#     cursor.execute('DROP TABLE IF EXISTS {}'.format(table_name))
#     cursor.execute('CREATE TABLE {}({})'.format(table_name,df))
#     # 提取数据转list 这里有与pandas时间模式无法写入因此换成str 此时mysql上格式已经设置完成
#     # date['Date'] = date['Date'].astype('str')
#     values = date.values.tolist()
#     # 根据columns个数
#     s = ','.join(['%s' for _ in range(len(date.columns))])
#     # executemany批量操作 插入数据 批量操作比逐个操作速度快很多
#     cursor.executemany('INSERT INTO {} VALUES ({})'.format(table_name, s), values)
#
#
# csv2mysql(db_name='hashtag_demo', table_name='world_cup_2018_tweets', df=make_table, date=df2)
# cursor.execute('SELECT * FROM world_cup_2018_tweets LIMIT 5')
# # scroll(self, value, mode='relative') 移动指针到某一行; 如果mode='relative',则表示从当前所在行移动value条,如果 mode='absolute',则表示从结果集的第一行移动value条.
# cursor.scroll(4)
# cursor.fetchall()

import pandas as pd
from sqlalchemy import create_engine

# 初始化数据库连接，使用pymysql模块
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/hashtag_demo')

# 读取本地CSV文件
df = pd.read_csv("E://文档//调研//推荐系统//hashtag//tweets.csv", dtype=str, error_bad_lines=False)
df2 = df.astype(object).where(pd.notnull(df), None)

# 将新建的DataFrame储存为MySQL中的数据表，不储存index列
df2.to_sql('russian_troll_tweets', engine, if_exists='replace', index=False)


print("Write to MySQL successfully!")


