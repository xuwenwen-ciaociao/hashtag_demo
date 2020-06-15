import hashlib
from models.russia_troll_tweets import RussiaTrollTweet

import time
from app import db


def do_dict(inst, cls, list=None):
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
    if list:
        for list_item in list:
            list_name = list_item._sa_adapter._key
            list_content = []
            for item in list_item:
                list_content.append(do_dict(item, item.__class__))
            d[list_name] = list_content
    return d