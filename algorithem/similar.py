import pymysql
import logging

from gensim import models
from gensim.models import word2vec

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
            )
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
        # hashtags_lower = hashtags.lower()
        hashtags_removesymbol = re.sub(r'[\[\]]', "", hashtags)
        hashtags_removesymbol2 = re.sub(r'[#]', "", hashtags_removesymbol)
        hashtags_removesymbol4 = re.sub(r'[\"]', "", hashtags_removesymbol2)
        hashtag_cleaned = hashtags_removesymbol4.split(',')
        hashtag_cleaned_remove_duplication = list(set(hashtag_cleaned))
        hashtag_dict[items['tweet_id']] = hashtag_cleaned_remove_duplication

hashtag_list = [hashtag_dict[key] for key in hashtag_dict]


def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # sentences = word2vec.LineSentence("output.txt")
    model = word2vec.Word2Vec(hashtag_list, size=250)

    # 保存模型，供以后使用
    model.save("word2vec.model")

    # 模型读取
    # model = word2vec.Word2Vec.load("your_model_name")

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = models.Word2Vec.load('word2vec.model')

    print("提供 3 种测试模式\n")
    print("输入一个词，则去寻找前10个该词的相似词")
    print("输入两个词，则去计算两个词的余弦相似度")
    print("输入三个词，进行类比推理")

    # while True:
    #     try:
    #         query = input('')
    #         q_list = query.split()
    #
    #         if len(q_list) == 1:
    #             print("相似词前 10 排序")
    #             res = model.most_similar(q_list[0], topn=10)
    #             for item in res:
    #                 print(item[0] + "," + str(item[1]))
    #
    #         elif len(q_list) == 2:
    #             print("计算 Cosine 相似度")
    #             res = model.similarity(q_list[0], q_list[1])
    #             print(res)
    #         else:
    #             print("%s之于%s，如%s之于" % (q_list[0], q_list[2], q_list[1]))
    #             res = model.most_similar([q_list[0], q_list[1]], [q_list[2]], topn=100)
    #             for item in res:
    #                 print(item[0] + "," + str(item[1]))
    #         print("----------------------------")
    #     except Exception as e:
    #         print(repr(e))


if __name__ == "__main__":
    main()