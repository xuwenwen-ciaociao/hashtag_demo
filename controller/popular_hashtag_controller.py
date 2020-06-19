from flask import request, jsonify
from models.hashtag_count import HashTagCount
from app import app


@app.route('/hashtag_list', methods={'GET'})
def get_popular_hahstag():
        topn = request.args.get("id")
        topN = int(topn)
        list_for_hahstag = []
        hashtag_list = HashTagCount.query.filter(HashTagCount.id.__le__(topN)).all()
        for item in hashtag_list:
                hashtag = item.hashtag
                list_for_hahstag.append(hashtag)
        return jsonify(result=list_for_hahstag)
