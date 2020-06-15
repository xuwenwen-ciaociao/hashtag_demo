from app import db


class RussiaTrollUsers(db.Model):

    __tablename__ = 'russia_troll_users'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    followers_count = db.Column(db.String(4096), nullable=True)
    friends = db.Column(db.String(4096), nullable=True)

    def __int__(self, user_id=None, user_name=None, followers_count=None, friends=None):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = followers_count
        self.friends = friends

    def __repr__(self):
        return '<RussiaTrollUsers %r>' % self.user_name