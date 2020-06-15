from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db


class WorldCup2018Tweets(db.Model):

    __tablename__ = 'world_cup_2018_tweets'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tweet_id = db.Column(db.String(255), db.ForeignKey('Top100Tweets.tweet_id'), nullable=False)
    Name = db.Column(db.String(255), nullable=False)
    Orig_tweet = db.Column(db.String(4096), nullable=False)
    RTs = db.Column(db.String(255), nullable=True)
    Likes = db.Column(db.String(255), nullable=True)
    Followers = db.Column(db.String(255), nullable=True)
    Friends = db.Column(db.String(255), nullable=True)


    def __int__(self, tweet_id=None, Name=None, Orig_tweet=None, RTs=None, Likes=None, Followers=None, Friends=None):
        self.tweet_id = ID
        self.name = Name
        self.orig_tweet = Orig_tweet
        self.retweet_count = RTs
        self.favorite_count = Likes
        self.followers = Followers
        self.friends = Friends

    def __repr__(self):
        return'<RussiaTrollTweet %r>' % self.title