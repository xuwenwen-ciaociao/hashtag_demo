import pymysql
import numpy as np
import json

# connect Mysql
db = pymysql.connect(host='172.24.135.80', port=3306, user='root', password='123456', db='hashtag_demo')
# connect cursor
cur = db.cursor(cursor=pymysql.cursors.DictCursor)
# get data
# cur.execute('SELECT retweets,followers,friends,`like` FROM world_cup_2018_tweets UNION ALL ')
cur.execute(
    'SELECT tweet_id world_tweetID,retweets world_retweet,`like` world_like,followers world_followers,friends world_friends FROM world_cup_2018_tweets '
    'UNION ALL '
    'SELECT tweets.tweet_id russia_tweetID,tweets.retweet_count russia_retweet,tweets.favorite_count russia_like,users.followers_count russia_followers,users.friends russia_friends FROM russia_troll_tweets tweets, russia_troll_users users WHERE tweets.user_id = users.id')
parameter_for_tweets = cur.fetchall()

# parameter list
world_cup_like = list()
world_cup_followers = list()
world_cup_friends = list()
world_cup_retweets = list()
dict_world = dict()
nor_dict_world = dict()


def nonetoint(str):
    if str == "":
        return 0
    elif str is None:
        return 0
    else:
        return int(str)


def normalization(int, mean, std):
    data = (int - mean) / std
    return data


for items in parameter_for_tweets:
    dict_world[items['world_tweetID']] = {'world_like': nonetoint(items['world_like']),
                                          'world_followers': nonetoint(items['world_followers']),
                                          'world_friends': nonetoint(items['world_friends']),
                                          'world_retweet': nonetoint(items['world_retweet'])}

world_cup_like = [dict_world[key]['world_like'] for key in dict_world]
world_cup_followers = [dict_world[key]['world_followers'] for key in dict_world]
world_cup_friends = [dict_world[key]['world_friends'] for key in dict_world]
world_cup_retweets = [dict_world[key]['world_retweet'] for key in dict_world]

mean_world_cup_like = np.mean(world_cup_like)
std_world_cup_like = np.std(world_cup_like)
mean_world_cup_followers = np.mean(world_cup_followers)
std_world_cup_followers = np.std(world_cup_followers)
mean_world_cup_friends = np.mean(world_cup_friends)
std_world_cup_friends = np.std(world_cup_friends)
mean_world_cup_retweets = np.mean(world_cup_retweets)
std_world_cup_retweets = np.std(world_cup_retweets)

for items in dict_world.values():
    items['world_like'] = normalization(items['world_like'], mean_world_cup_like, std_world_cup_like)
    items['world_followers'] = normalization(items['world_followers'], mean_world_cup_followers, std_world_cup_followers)
    items['world_friends'] = normalization(items['world_friends'], mean_world_cup_friends, std_world_cup_friends)
    items['world_retweet'] = normalization(items['world_retweet'], mean_world_cup_retweets, std_world_cup_retweets)

with open('E:/recommendation system/flask_hashtag/models/' + 'Nor_post_parameter4 .txt', 'w') as f:
    f.write(json.dumps(dict_world))
