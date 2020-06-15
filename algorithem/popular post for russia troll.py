import re
import pandas as pd
import pymysql
import numpy as np
import datetime
import json

# connect Mysql
db = pymysql.connect(host='172.24.135.80', port=3306, user='root', password='123456', db='hashtag_demo')
# connect cursor
cur = db.cursor(cursor=pymysql.cursors.DictCursor)
# get data
# cur.execute('SELECT retweets,followers,friends,`like` FROM world_cup_2018_tweets UNION ALL ')
cur.execute('SELECT tweets.tweet_id russia_tweetID,tweets.retweet_count russia_retweet,'
            'tweets.favorite_count russia_like, users.followers_count russia_followers,users.friends '
            'russia_friends,tweets.create_str created_date FROM russia_troll_tweets tweets, russia_troll_users users '
            'WHERE tweets.user_id = users.id')
parameter_for_tweets = cur.fetchall()

russia_like = list()
russia_followers = list()
russia_friends = list()
russia_retweets = list()
dict_russia = dict()
popular_score_russia = dict()
collected_datetime = datetime.datetime.strptime("2018-02-15 00:00:00", "%Y-%m-%d %H:%M:%S")


def nonetoint(str):
    if str == "":
        return 0
    elif str is None:
        return 0
    else:
        return int(str)


def normalization(int, created_date, collected_date, mean, std):
    td = collected_date - created_date
    time_differents = td.days * 24 + td.seconds / 3600
    data = (int / time_differents - mean) / std
    return data


def popular_score(dict):
    tweet_score = dict['russia_like'] * 0.3 + dict['russia_followers'] * 0.2 + dict['russia_friends'] * 0.1 + dict[
        'russia_retweet'] * 0.4
    return tweet_score


for items in parameter_for_tweets:
    dict_russia[items['russia_tweetID']] = {'russia_like': nonetoint(items['russia_like']),
                                            'russia_followers': nonetoint(items['russia_followers']),
                                            'russia_friends': nonetoint(items['russia_friends']),
                                            'russia_retweet': nonetoint(items['russia_retweet']),
                                            "russia created_time": items['created_date']}

russia_like = [dict_russia[key]['russia_like'] for key in dict_russia]
russia_followers = [dict_russia[key]['russia_followers'] for key in dict_russia]
russia_friends = [dict_russia[key]['russia_friends'] for key in dict_russia]
russia_retweets = [dict_russia[key]['russia_retweet'] for key in dict_russia]

mean_russia_like = np.mean(russia_like)
std_russia_like = np.std(russia_like)
mean_russia_followers = np.mean(russia_followers)
std_russia_followers = np.std(russia_followers)
mean_russia_friends = np.mean(russia_friends)
std_russia_friends = np.std(russia_friends)
mean_russia_retweets = np.mean(russia_retweets)
std_russia_retweets = np.std(russia_retweets)

for items in dict_russia.values():
    items['russia_like'] = normalization(items['russia_like'], items['russia created_time'], collected_datetime,
                                         mean_russia_like, std_russia_like)
    items['russia_followers'] = normalization(items['russia_followers'], items['russia created_time'],
                                              collected_datetime, mean_russia_followers, std_russia_followers)
    items['russia_friends'] = normalization(items['russia_friends'], items['russia created_time'], collected_datetime,
                                            mean_russia_friends, std_russia_friends)
    items['russia_retweet'] = normalization(items['russia_retweet'], items['russia created_time'], collected_datetime,
                                            mean_russia_retweets, std_russia_retweets)

for key, value in dict_russia.items():
    popular_score_russia[key] = popular_score(value)
print(popular_score_russia)

with open('E:/recommendation system/flask_hashtag/models/' + 'tweet_sore1 .txt', 'a+') as f:
    for k, v in popular_score_russia.items():
        f.write(str(k) + ' ' + str(v) + '\n')
