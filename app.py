from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_cors import CORS


pymysql.install_as_MySQLdb()
app = Flask(__name__)
# 数据库连接配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/hashtag_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
CORS(app)

from models.hashtag_count import HashTagCount
import controller


@app.route('/')
def home_page():
    return 'bbb'


@app.before_first_request
def init_db():
    return

if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(debug=True)

