from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db


class Top100Tweets(db.Model):

    __tablename__='top100_tweets'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    hashtag = db.Column(db.String(255), nullable=False)
    tweet = db.relationship('WorldCup2018Tweets', backref='popular_tweet_for_world_cup', uselist=False)
    tweet_id = db.Column(db.String(255), nullable=False)
