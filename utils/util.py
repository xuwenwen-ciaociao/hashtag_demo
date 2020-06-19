# def to_dict(self):
#     list = []
#     world_cup_dict = {
#         "origin_tweet": self.Orig_tweet,
#         "retweet_count": self.RTs,
#         "favorite_count": self.Likes,
#         "followers": self.Followers,
#         "friends": self.Friends
#     }
#     list.append(world_cup_dict)
#     return list


def do_dict(inst, cls, list1=None, list2=None):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    if list1 is not None:
        for list_item in list1:
            list_name = list_item._sa_adapter._key
            list_content = []
            for item in list_item:
                list_content.append(do_dict(item, item.__class__))
            d[list_name] = list_content
    if list2 is not None:
        for list_item in list2:
            list_name = list_item._sa_adapter._key
            list_content = []
            for item in list_item:
                list_content.append(do_dict(item, item.__class__))
            d[list_name] = list_content
    return d

# def result_to_dict(list=None):
#     dict_for_popular_tweet = dict()
#     list_hashtag = list()
#     def to_ditc()
#     for item in list:
#         list_tweet = list()
#         if item.hashtag not in list_hashtag:
#             list_hashtag.append(item.hashtag)
#             dict_for_popular_tweet["hashtag"] = item.hashtag


