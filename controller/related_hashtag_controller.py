from algorithem.related_hashtag import relatde_hashtag
from gensim.models import word2vec
from flask import request, jsonify
from app import app


@app.route('/related_hashtag', methods={'GET'})
def get_related_hasgtag():
    related_list_for_hashtag = dict()
    hashtag = request.args.get('hashtag')
    related_list_for_hashtag['related_hashtags'] = relatde_hashtag(hashtag)
    return related_list_for_hashtag
