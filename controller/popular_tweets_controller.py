from flask import request, jsonify
from models.top100_tweets import Top100Tweets
from app import app
from utils.util import do_dict


@app.route('/popular_tweets', methods={'GET'})
def get_popular_tweets():
    list_for_hahstag = []
    tweet_id_list = Top100Tweets.query.filter(Top100Tweets.hashtag.in_(request.args.getlist('hashtag'))).all()
    for item in tweet_id_list:
        list_for_hahstag.append(do_dict(item, item.__class__, [item.tweet_for_world_cup], [item.tweet_for_russia_troll]))
    return jsonify(code=0, result=list_for_hahstag)

    # for item in tweet_id_list:
    #     tweet = item.tweet
    #     hashtag = item.hashtag
    #     if hashtag not in list_for_hahstag:
    #         list2 = []
    #         list_for_hahstag.append(hashtag)
    #         for tweet_list in tweet:
    #             dict = {}
    #             for table in tweet_list.__table__.columns:
    #                 v = getattr(tweet_list, table.name)
    #                 dict[table.name] = v
    #         list2.append(dict)
    #         dict_for_popular_tweet['hahstag'] = hashtag
    #         dict_for_popular_tweet['tweets'] = list2
    #     else:
    #         for tweet_list in tweet:
    #             dict = {}
    #             for table in tweet_list.__table__.columns:
    #                 v = getattr(tweet_list, table.name)
    #                 dict[table.name] = v
    #             dict_for_popular_tweet['tweets'].append(dict)
    # return jsonify(code=0, result=dict_for_popular_tweet)

