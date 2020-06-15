from flask import request, jsonify
from models.top100_tweet import Top100Tweets
from app import app, db
from models.world_cup_2018_tweet import WorldCup2018Tweets


@app.route('/hashtag/<id>/')
def get_popular_tweets(id):
    tweet_id = Top100Tweets.query.get(id)
    Origin_tweets = WorldCup2018Tweets.query.filter(WorldCup2018Tweets.tweet_id == tweet_id).all()
    return ','.join(a.Origin_tweets for a in Origin_tweets)


