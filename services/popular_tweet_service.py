from flask import request
from models.top100_tweets import Top100Tweets
from utils.util import do_dict

class PopularTweetService(Top100Tweets, do_dict):
    
    list_for_hahstag = []
    tweet_id_list = Top100Tweets.query.filter(Top100Tweets.hashtag.in_(request.args.getlist('hashtag'))).all()
    for item in tweet_id_list:
        list_for_hahstag.append(do_dict(item, item.__class__, [item.tweet_for_world_cup], [item.tweet_for_russia_troll]))