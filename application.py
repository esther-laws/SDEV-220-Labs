from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50), unique=True, nullable=False)
    author = db.Column(db.String(40))
    publisher = db.Column(db.String(40))

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Created by: Esther Laws on 9/28/23'

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []

    for book in books:
        book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {'books': output}