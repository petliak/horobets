from flask import Flask, request , session
from flask import render_template
from werkzeug.utils import redirect
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import row
#host
basedir = os.path.abspath(os.path.dirname(__file__))
apap = Flask(__name__)
apap.config['SQLALCHEMY_DATABASE_URI'] =\
 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
apap.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(apap)

apap.secret_key = 'fwjqpejqidklfhnq;#$%^$36752f5526172r'

class admin_data(db.Model):
    __tablename__ = 'admin_data'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(16),  nullable=False)
    password = db.Column(db.String(16),  nullable=False)
    def __init__(self, login, password):
        self.login = login
        self.password = password


class add_article(db.Model):
    __tablename__ = 'add_article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(16), nullable=False)
    text = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text(250), nullable=False)
    continent = db.Column(db.String(64), nullable=False)
    def __init__ (self, title, text, url, continent):
        self.title = title
        self.text = text
        self.url = url
        self.continent = continent


#with apap.app_context():
    #db.create_all()
    #admin = admin_data('host','parol')
    #db.session.add(admin)
    #db.session.commit()



@apap.route('/')
def index():
    #return ('<h1>Головна сторінка сайту</h1>'
    #        '<p>Сторінка в розробці</p>')
    return render_template('index.html')
@apap.route('/articles')
def stati():
    list_articles = add_article.query.all()


    return render_template('articles.html', articles=list_articles)


@apap.route('/Admin', methods = ['GET'])
def admin():
    msg = "Введіть логін та пароль"
    return render_template('admin.html', msg=msg)

@apap.route('/addartkl', methods = ['GET'])
def addartkl_get():
    if 'user' in session:
        return render_template('addarticle.html')
    else:
        session['link']='/addartkl'
    msg = "Введіть логін та пароль"
    return render_template('admin.html', msg=msg)


@apap.route('/Admin', methods = ['POST'])
def admin_login():
    login = request.form['login']
    password = request.form['password']
    if admin_data.query.filter_by(login=login, password=password).all()!= []:
        return render_template('addarticle.html')
    else:
        return render_template('admin.html')


@apap.route('/<name>')
def name(name):
    return render_template('index.html', username=name)


@apap.route('/addartkl', methods=['POST'])
def addartkl():
    title = request.form['title']
    area = request.form['area']
    url = request.form['url']
    continent = request.form['continent']
    row = add_article(title, area, url, continent)
    db.session.add(row)
    db.session.commit()
    return render_template('addarticle.html')

@apap.route('/post_dateils/<number>')
def post(number):
    row = add_article.query.filter_by(id=number).first()
    return render_template('Details.html', row=row)

@apap.route('/del_article', methods = ['GET'])
def del_article():
    if 'user' in session:
        articles = add_article.query.all()
        return render_template('del_article.html', articles=articles)
    else:
        session['link']='/del_article'
        msg = "Введіть логін та пароль"
        return render_template('admin.html', msg=msg)

@apap.route('/del_article', methods = ['POST'])
def del_ar_but():
    id_list = request.form.getlist('id')
    for id in id_list:
        row = add_article.query.filter_by(id=id).first()
        db.session.delete(row) #Звернення
    db.session.commit() #оновити
    articles = add_article.query.all()
    return render_template('del_article.html', articles=articles)



if __name__ == '__main__':
    apap.run(debug=True)
