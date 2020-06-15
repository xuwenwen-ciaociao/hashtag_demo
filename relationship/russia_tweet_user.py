from app import db

tags = db.Table('user_tweets',
                db.Column('user_id', db.String, db.ForeignKey('russia_troll_users.id'), primary_key=True),
                db.Column('tweet_id', db.String, db.ForeignKey('russia_troll_tweets.tweet_id'), primary_key=True)
                # db.Column('followers_count', db.String, 'russia_troll_users.followers_count',  nullable=True)
                # db.Column('friends_count', db.String, 'russia_troll_users.friends_count',  nullable=True)
                # db.Column('favorite_count', db.String, 'russia_troll_tweets.favorite_count', nullable=True)
                # db.Column('retweet_count', db.String, 'russia_troll_tweets.retweet_count', nullable=True)
                # db.Column('text', db.String, 'russia_troll_tweets.text', nullable=True)
                )
