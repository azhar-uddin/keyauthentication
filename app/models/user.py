from flask import current_app as app
from app.models import db, ma
from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(40))
    company = db.Column(db.String(80))
    phone = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(140), nullable=False)

    def __init__(self, email, name, company, phone, password):
      self.name = name
      self.email = email
      self.company = company
      self.phone = phone
      self.hash_password(password)

    def __repr__(self):
        return '<User - {}>'.format(self.email)

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)

    def save(self):
      db.session.add(self)
      db.session.commit()

    def delete(self):
      db.session.delete(self)
      db.session.commit()

