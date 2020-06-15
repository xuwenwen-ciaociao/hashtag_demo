import numpy as np
import pandas as pd
import csv
import os
import pymysql
import operator
import json

import re
import datetime


start = datetime.datetime.now()
# connect Mysql
db = pymysql.connect(host='172.24.135.80', port=3306, user='root', password='123456', db='hashtag_demo')
# connect cursor
cur = db.cursor(cursor=pymysql.cursors.DictCursor)
# get data
cur.execute('SELECT tweet_id, hashtag FROM russia_troll_tweets '
            'UNION ALL '
            'SELECT tweet_id, hashtag FROM world_cup_2018_tweets '
            'UNION ALL '
            'SELECT tweet_id, hashtag FROM twitter_friends')
hashtags_for_tables = cur.fetchall()


hashtag_dict = dict()
hashtag_list = list()
hashtag_frequency_dict = dict()

for items in hashtags_for_tables:
    tweet_id = items['tweet_id']
    hashtags = items['hashtag']

    if hashtags == '[]':
        continue
    if hashtags is None:
        continue
    else:
        hashtags_lower = hashtags.lower()
        hashtags_removesymbol = re.sub(r'[\[\]]', "", hashtags_lower)
        hashtags_removesymbol2 = re.sub(r'[#]', "", hashtags_removesymbol)
        hashtags_removesymbol4 = re.sub(r'[\"]', "", hashtags_removesymbol2)
        hashtag_cleaned = hashtags_removesymbol4.split(',')
        hashtag_dict[items['tweet_id']] = hashtag_cleaned

for key, value in hashtag_dict.items():
    hashtag_list.extend(value)
    # print(hashtag_list)

for word in hashtag_list:
    key = ''.join(word.split())
    # dic[word] = dic.get(word, 0) + 1
    if key not in hashtag_frequency_dict.keys():
        hashtag_frequency_dict[key] = 1
    else:
        hashtag_frequency_dict[key] = hashtag_frequency_dict[key] + 1
swd = sorted(hashtag_frequency_dict.items(), key=operator.itemgetter(1), reverse=True)
print(swd)

end = datetime.datetime.now()

print((end - start).seconds)
with open('E:/recommendation system/flask_hashtag/models/' + 'hashtag_count2.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join('%s %s' % x for x in swd))