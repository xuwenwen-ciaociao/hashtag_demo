from app import db


class RussiaTrollTweet(db.Model):

    __tablename__ = 'russia_troll_tweets'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tweet_id = db.Column(db.String(255), db.ForeignKey('top100_tweets.tweet_id'), nullable=True)
    user_id = db.Column(db.String(4096), nullable=False)
    text = db.Column(db.String(4096), nullable=False)
    retweet_count = db.Column(db.String(255), nullable=False)
    favorite_count = db.Column(db.String(255), nullable=False)
    
    

    # def __int__(self, tweet_id=None, user_id=None, text=None, retweet_count=None, favorite_count=None):
    #     self.tweet_id = tweet_id
    #     self.user_id = user_id
    #     self.orig_tweets = text
    #     self.retweet_count = retweet_count
    #     self.favorite_count = favorite_count
    #
    # def __repr__(self):
    #     return'<RussiaTrollTweet %r>' % self.tweet_id