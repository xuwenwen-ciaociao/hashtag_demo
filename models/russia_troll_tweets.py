from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db
from app import db


class RussiaTrollTweet(db.Model):

    __tablename__ = 'russia_troll_tweets'
    tweet_id = db.Column(db.String(255), primary_key=True,  nullable=False)
    user_id = db.relationship('russia_troll_users', secondary='user_tweets', backref='cou')
    text = db.Column(db.String(4096), nullable=False)
    retweet_count = db.Column(db.int(11), nullable=True)
    favorite_count = db.Column(db.int(11), nullable=True)

    def __int__(self, tweet_id=None, user_id=None, text=None, retweet_count=None, favorite_count=None):
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.orig_tweets = text
        self.retweet_count = retweet_count
        self.favorite_count = favorite_count

    def __repr__(self):
        return'<RussiaTrollTweet %r>' % self.title