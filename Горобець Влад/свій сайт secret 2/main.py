from flask import Flask, request, session
from flask import render_template
import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from sqlalchemy.engine import row

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = 'A78Zrejn35985'
class admin_data(db.Model):
    __tablename__ = 'admin_data'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(16),  nullable=False)
    password = db.Column(db.String(16),  nullable=False)
    def __init__(self, login, password):
        self.login = login
        self.password = password

class add_thriller1(db.Model):
    __tablename__ = 'add_thriller'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    video_url = db.Column(db.String, nullable=False)
    area = db.Column(db.String, nullable=False)
    def __init__(self, title, video_url, area):
        self.title = title
        self.video_url = video_url
        self.area = area

#with app.app_context():
     #db.create_all()
     #admin = admin_data('1','1')
     #db.session.add(admin)
     #db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/news/addthriller', methods =['GET'])
def addthriller_get():
    if 'user' in session:
        return render_template('addthriller.html')
    else:
        session['link'] = '/news/addthriller'
        msg = "ой ви лох"
        return render_template('add_thriller.html', msg=msg)

@app.route('/news/addthriller', methods =['POST'])
def addthriller_post():
    title = request.form['title']
    video_url = request.form['video_url']
    area = request.form['area']
    row = add_thriller1(title, video_url, area)
    db.session.add(row)
    db.session.commit()
    return render_template('addthriller.html')


@app.route('/news/add_thriller', methods =['GET'])
def add_thriller():
    msg = "Введіть логін та пароль"
    return render_template('add_thriller.html', msg=msg)

@app.route('/news/add_thriller', methods = ['POST'])
def admin_login():
    login = request.form['login']
    password = request.form['password']
    if admin_data.query.filter_by(login=login, password=password).all()!= []:
        return render_template('addthriller.html')
    else:
        return render_template('add_thriller.html')

@app.route('/news')
def add_thriller_news():
    articles = add_thriller1.query.all()
    return render_template('news.html', articles=articles)


@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/news/add_img')
def add_img():
    return render_template('add_img.html')

if __name__ == '__main__':
    app.run(debug=True)
