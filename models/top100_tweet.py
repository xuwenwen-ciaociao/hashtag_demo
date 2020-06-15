from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db


class Top100Tweets(db.Model):

    __tablename__='top100_tweet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    tweet_id = db.relationship('world_cup_2018_tweet', backref='tweet', lazy=True)
    hashtag = db.Column(db.String(255), nullable=False)

    def __int__(self, tweet_id=None, hashtag=None):
        self.tweet_id = tweet_id
        self.hashtag = hashtag

    def __repr__(self):
        return'<Top100Tweets %r>' % self.tweet_id