from gensim.models import word2vec

from algorithem.similar import main
def relatde_hashtag(hashtag):
    similar_world_list = []
    model = word2vec.Word2Vec.load('E:\\recommendation system\\hashtag_demo\\algorithem\\word2vec.model')
    set = model.wv.most_similar(positive=[hashtag], topn=10)
    for item in set:
        similar_world = item[0]
        similar_world_list.append(similar_world)
    return similar_world_list
