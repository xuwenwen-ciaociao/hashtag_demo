from app import db


class HashTagCount(db.Model):

    __tablename__='hashtag_count'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    hashtag = db.Column(db.String(255), nullable=False)