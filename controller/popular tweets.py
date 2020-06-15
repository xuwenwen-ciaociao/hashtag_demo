from flask import request, jsonify
from models.top100_tweet import Top100Tweets
from app import app, db
from models.world_cup_2018_tweet import WorldCup2018Tweets


@app.route('/hashtag/GetAll', methods={'GET'})
def get_all_tweets():
    list = WorldCup2018Tweets.query.all()
    _list = []
    for item in list:
        _list.append(item)
    return jsonify(_list)
