from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/emp_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer(),primary_key = True,autoincrement = True)
    name= db.Column(db.String(50))
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))


    def __init__(self,name,age,position):
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"{self.name}:{self.id}"


