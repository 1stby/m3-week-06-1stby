from app import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age =age

    def __repr__(self):
        return f'使用者名稱為 {self.name} ，年齡為 {self.age} 歲。'
    
class Users(db.Model):
    __tablename__ = 'users'
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column(db.String(100))
    mobile = db.Column('mobile', db.String(100))
    def __init__(self, name, email, mobile):
        self.name = name
        self.email =email
        self.mobile = mobile
