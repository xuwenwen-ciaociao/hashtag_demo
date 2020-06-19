from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db


class WorldCup2018Tweets(db.Model):

    __tablename__ = 'world_cup_2018_tweets'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tweet_id = db.Column(db.String(255), db.ForeignKey('top100_tweets.tweet_id'), nullable=True)
    Name = db.Column(db.String(255), nullable=False)
    Orig_tweet = db.Column(db.String(4096), nullable=False)
    RTs = db.Column(db.String(255), nullable=True)
    Likes = db.Column(db.String(255), nullable=True)
    Followers = db.Column(db.String(255), nullable=True)
    Friends = db.Column(db.String(255), nullable=True)

    # def __int__(self, tweet_id=None, user_id=None, text=None, retweet_count=None, favorite_count=None):
    #     self.tweet_id = tweet_id
    #     self.user_id = user_id
    #     self.orig_tweets = text
    #     self.retweet_count = retweet_count
    #     self.favorite_count = favorite_count