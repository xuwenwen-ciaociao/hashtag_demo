from DateTime import DateTime
from flask import request, jsonify
from sqlalchemy import Numeric

from models.top100_tweets import Top100Tweets
from app import app, db
from models.world_cup_2018_tweet import WorldCup2018Tweets


@app.route('/hashtag', methods={'GET'})
def get_popular_tweets():
    hashtag_list = request.args.getlist('hashtag')
    dict_for_hashtag = dict()
    for item in hashtag_list:
        list_for_popular_tweet = []
        tweet_id_list =Top100Tweets.query.filter(Top100Tweets.hashtag == item).all()
        for tweet_id in tweet_id_list:
            fas = dict()
            tweet = tweet_id.tweet
            fas[tweet_id.tweet_id] = to_dict(tweet)
            list_for_popular_tweet.append(fas)
        dict_for_hashtag[item] = list_for_popular_tweet
    return jsonify(code=0, result=dict_for_hashtag)


def to_dict(self):
    def convert_datetime(value):
        if value:
            return value.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return ""
    for col in self.__table__.columns:
        if isinstance(col.type, DateTime):
            value = convert_datetime(getattr(self, col.name))
        elif isinstance(col.type, Numeric):
            value = float(getattr(self, col.name))
        else:
            value = getattr(self, col.name)
        yield (col.name, value)


