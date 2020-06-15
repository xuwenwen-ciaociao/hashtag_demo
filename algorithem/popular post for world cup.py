import re
import pandas as pd
import datetime
import pymysql
import numpy as np
import json

# connect Mysql
db = pymysql.connect(host='172.24.135.80', port=3306, user='root', password='123456', db='hashtag_demo')
# connect cursor
cur = db.cursor(cursor=pymysql.cursors.DictCursor)
# get data
# cur.execute('SELECT retweets,followers,friends,`like` FROM world_cup_2018_tweets UNION ALL ')
cur.execute('SELECT tweet_id world_tweetID,retweets world_retweet,`like` world_like,followers world_followers,'
            'friends world_friends,`date` created_date FROM world_cup_2018_tweets ')
parameter_for_tweets = cur.fetchall()

# parameter list
world_cup_like = list()
world_cup_followers = list()
world_cup_friends = list()
world_cup_retweets = list()
dict_world_cup = dict()
popular_score_world_cup = dict()
collected_datetime = datetime.datetime.strptime("2018-08-14 00:00:00", "%Y-%m-%d %H:%M:%S")

def nonetoint(str):
    if str == "":
        return 0
    elif str is None:
        return 0
    else:
        return int(str)


def normalization(int, created_date, collected_date, mean, std):
    td = collected_date - created_date
    time_differents = td.days * 24 + td.seconds/3600
    data = (int/time_differents - mean) / std
    return data


def popular_score(dict):
    tweet_score = dict['world_like'] * 0.3 + dict['world_followers'] * 0.2 + dict['world_friends'] * 0.1 + dict['world_retweet'] * 0.4
    return tweet_score


for items in parameter_for_tweets:
    dict_world_cup[items['world_tweetID']] = {'world_like': nonetoint(items['world_like']),
                                          'world_followers': nonetoint(items['world_followers']),
                                          'world_friends': nonetoint(items['world_friends']),
                                          'world_retweet': nonetoint(items['world_retweet']),
                                          "world created_time": items['created_date']}

world_cup_like = [dict_world_cup[key]['world_like'] for key in dict_world_cup]
world_cup_followers = [dict_world_cup[key]['world_followers'] for key in dict_world_cup]
world_cup_friends = [dict_world_cup[key]['world_friends'] for key in dict_world_cup]
world_cup_retweets = [dict_world_cup[key]['world_retweet'] for key in dict_world_cup]

mean_world_cup_like = np.mean(world_cup_like)
std_world_cup_like = np.std(world_cup_like)
mean_world_cup_followers = np.mean(world_cup_followers)
std_world_cup_followers = np.std(world_cup_followers)
mean_world_cup_friends = np.mean(world_cup_friends)
std_world_cup_friends = np.std(world_cup_friends)
mean_world_cup_retweets = np.mean(world_cup_retweets)
std_world_cup_retweets = np.std(world_cup_retweets)

for items in dict_world_cup.values():
    items['world_like'] = normalization(items['world_like'], items['world created_time'], collected_datetime, mean_world_cup_like, std_world_cup_like)
    items['world_followers'] = normalization(items['world_followers'], items['world created_time'], collected_datetime, mean_world_cup_followers, std_world_cup_followers)
    items['world_friends'] = normalization(items['world_friends'], items['world created_time'], collected_datetime, mean_world_cup_friends, std_world_cup_friends)
    items['world_retweet'] = normalization(items['world_retweet'], items['world created_time'], collected_datetime, mean_world_cup_retweets, std_world_cup_retweets)

for key, value in dict_world_cup.items():
    popular_score_world_cup[key] = popular_score(value)
print(popular_score_world_cup)

with open('E:/recommendation system/flask_hashtag/models/' + 'tweet_sore1 .txt', 'w') as f:
    for k, v in popular_score_world_cup.items():
        f.write(str(k) + ' ' + str(v) + '\n')
    # f.write(json.dumps(popular_score_world_cup))