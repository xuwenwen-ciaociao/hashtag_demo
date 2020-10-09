import pymysql
import heapq
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号
# connect Mysql
db = pymysql.connect(host='172.24.135.80', port=3306, user='root', password='123456', db='hashtag_demo')
# connect cursor
cur = db.cursor(cursor=pymysql.cursors.DictCursor)
# get data
# cur.execute('SELECT retweets,followers,friends,`like` FROM world_cup_2018_tweets')
cur.execute('SELECT tweets.tweet_id,tweets.retweet_count,tweets.favorite_count,users.followers_count,users.friends FROM russia_troll_tweets tweets, russia_troll_users users WHERE tweets.user_id = users.id')
parameter_for_world_cup = cur.fetchall()
data_like = []
data_followers = []
data_friends = []
data_retweets = []

for item in parameter_for_world_cup:
    like_count = item['favorite_count']
    followers_count = item['followers_count']
    friends_count = item['friends']
    retweets_count = item['retweet_count']
    if like_count == "":
        continue
    elif like_count is not None:
        data_like.append(int(like_count))
    if followers_count == "":
        continue
    elif followers_count is not None:
        data_followers.append(int(followers_count))
    if friends_count == "":
        continue
    elif friends_count is not None:
        data_friends.append(int(friends_count))
    if retweets_count == "":
        continue
    elif retweets_count is not None:
        data_retweets.append(int(retweets_count))


""",
绘制直方图
data:必选参数，绘图数据
bins:直方图的长条形数目，可选项，默认为10
normed:是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。
facecolor:长条形的颜色
edgecolor:长条形边框的颜色
alpha:透明度
"""
print(heapq.nlargest(10, data_followers))
print(np.mean(data_followers))
print(np.median(data_followers))
print(heapq.nlargest(10, data_like))
print(np.mean(data_like))
print(np.median(data_like))
print(heapq.nlargest(10, data_friends))
print(np.mean(data_friends))
print(np.median(data_friends))
print(heapq.nlargest(10, data_retweets))
print(np.mean(data_retweets))
print(np.median(data_retweets))
plt.hist(data_like, bins=20, density=0, facecolor="blue", edgecolor="black", alpha=0.7)
# 显示横轴标签
plt.xlabel("like_count")
# 显示纵轴标签
plt.ylabel("distribution")
# 显示图标题
plt.title("like_distribution")
plt.show()

plt.hist(data_followers, bins=5, density=0, facecolor="red", edgecolor="black", alpha=0.7)
# 显示横轴标签
plt.xlabel("followers_count")
# 显示纵轴标签
plt.ylabel("distribution")
# 显示图标题
plt.title("followers_distribution")
plt.show()

plt.hist(data_friends, bins=40, density=0, facecolor="yellow", edgecolor="black", alpha=0.7)
# 显示横轴标签
plt.xlabel("friends_count")
# 显示纵轴标签
plt.ylabel("distribution")
# 显示图标题
plt.title("friends_distribution")
plt.show()

plt.hist(data_retweets, bins=20, density=0, facecolor="grey", edgecolor="black", alpha=0.7)
# 显示横轴标签
plt.xlabel("retweets_count")
# 显示纵轴标签
plt.ylabel("distribution")
# 显示图标题
plt.title("retweets_distribution")
plt.show()
