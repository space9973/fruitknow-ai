# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FAQ(db.Model):
    __tablename__ = 'faqs'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<FAQ {self.question}>'
