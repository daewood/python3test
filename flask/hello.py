from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, static_path='/static')
manager=Manager(app)
bootstrap=Bootstrap(app)
moment=Moment(app)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/user/<id>')
def user(id) :
    #print(id)
    return render_template('user.html',name=id)

@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())


if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=8000,debug=True) # 使用 flask 自带的服务器
    manager.run() # script parameters: runserver