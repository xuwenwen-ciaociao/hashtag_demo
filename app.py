from flask import Flask
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

import models
import controller


@app.route('/')
def hello_world():
    return 'bbbb'


@app.before_first_request
def init_db():
    db.create_all()



if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(debug=True)

