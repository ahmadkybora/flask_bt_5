from enum import unique
import os
from flask import Flask
import sqlalchemy

app = Flask(__name__)

# اینجا یک دیتابیس بوسیله 
# orm sqlAlchemy
# ساخیتیم و کنفیگ کردیم
file_dir = os.patch.direname(__file__)
goal_route = os.path.join(file_dir, "app.db")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + goal_route
db = sqlalchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Writers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    writer_id = db.Column(db.Integer, db.ForiegnKey("writer.id"))
    writer = db.relationship("Writers", backref = db.backref("books"))

@app.route("/addBook")
def addBook():
    writer = Writers(name="ali")
    book = Books(name="tb", writer=writer)
    db.session.add(book)
    db.session.commit()

@app.route("/books")
def showBooks():
    books = Books.query.all()
    
@app.route("/")
def home():
    goal_str="moh"
    users = User.query.filter(User.name.like(f"%{goal_str}%")).all()
    return users

@app.route("/add")
def addUser():
    try:
        user = User(name="mo")
        db.session.add(user)
        db.session.commit()
        return "success"
    except Exception as ex:
        return "add " + ex
# بوسیله کامیت میتوان ذخیره سازی کرد

@app.route("/update")
def updateUser():
    try:
        goal_user = User.query.filter_by(name = "m").first()
        goal_user.name = "kk"
        db.session.commit()
        return "up"
    except Exception as ex:
        return ex

# اینجا یک کلاس تعریف کردیم که از 
# orm
# ارث بری میکند
# روش ارث بری در پایتون به این صورت است که 
# برای کلاس پرانتز گذاشته و داخل آن کلاس پدر را مینو یسیم
class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.Email, nullable=True)