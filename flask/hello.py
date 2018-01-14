from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager=Manager(app)

@app.route('/user/<id>')
def user(id) :
    #print(id)
    return render_template('user.html',name=id)

@app.route('/')
def hello():
    return "Hello, Flask!"


if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=8000,debug=True) # 使用 flask 自带的服务器
    manager.run() # script parameters: runserver