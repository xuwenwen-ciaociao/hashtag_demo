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
top10_hashtag_list = list()
tweet_id_top10_hashtag = list()
top1_hashtagkeyword = dict()
list_tweet_id = list()
dict_tweet_with_score = dict()
popular_hashtag_tweet = dict()
top100_tweet = dict ()


def get_tweet(top10_hashtag_list, dict1, dict2):
    for hashtag_keyword in top10_hashtag_list:
        list = []
        for key, value in dict1.items():
            if hashtag_keyword in value:
                list.append(key)
                dict2[hashtag_keyword] = list
    return dict2

# def top10_tweet(top1_hashtagkeyword,dict):
#
#     swd = sorted(hashtag_frequency_dict.items(), key=operator.itemgetter(1), reverse=True)




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
top10_hahstag = swd[0:10]
for tuple in top10_hahstag:
    top10_hashtag_list.append(tuple[0])
print(top10_hashtag_list)
top1_hashtagkeyword = get_tweet(top10_hashtag_list, hashtag_dict, top1_hashtagkeyword)

# print(top1_hashtagkeyword)


sql = "SELECT tweet_id, score FROM tweet_score"
cur.execute(sql)
score_for_tweets = cur.fetchall()

for items in score_for_tweets:
    dict_tweet_with_score[items['tweet_id']] = items['score']

list_tweet_id = [key for key, value in dict_tweet_with_score.items()]
set1_tweetid = set(list_tweet_id)

for key, value in top1_hashtagkeyword.items():
    set_tweet_id__for_one_hashtag = set(value)
    set_tweet_id = set1_tweetid & set_tweet_id__for_one_hashtag
    popular_hashtag_tweet[key] = {key: value for key, value in dict_tweet_with_score.items() if key in set_tweet_id}
    # print(popular_hashtag_tweet)


for key, value in popular_hashtag_tweet.items():
    tweet_id_list = []
    swd = sorted(value.items(), key=operator.itemgetter(1), reverse=True)
    top10_tweet = swd[0:10]
    for tweet_id in top10_tweet:
        tweet_id_list.append(tweet_id)
    top100_tweet[key] = tweet_id_list


print(top100_tweet)


end = datetime.datetime.now()
print((end - start).seconds)

for key, value in top100_tweet.items():
    for item in value:
        sql_top100_tweet = "insert into `top100_tweet` (`tweet_id`,`score`,`hashtag`) values ('" + item[0]+ "', '" + str(item[1]) + "', '"+ key +"' )"
        try:
            cur.execute(sql_top100_tweet)
        except Exception as e:
            print("Error", str(e), sql)
            pass
db.commit()
db.rollback()
cur.close()

# with open('E:/recommendation system/flask_hashtag/models/' + 'top100_tweet.txt', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(top100_tweet))