from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db


class Top100Tweets(db.Model):

    __tablename__='top100_tweet'
    list_id = db.Column(db.Integer, primary_key=True, unique=True)
    hashtag = db.Column(db.String(255), nullable=False)
    tweet_id =db.relationship('WorldCup2018Tweets', backref='popular_tweet_for_world_cup', lazy='dynamic')

    def __int__(self, list_id=None, tweet_id=None, hashtag=None):
        self.popular_list = list_id
        self.tweet_id = tweet_id
        self.hashtag = hashtag

    def __repr__(self):
        return'<Top100Tweets %r>' % self.popular_list