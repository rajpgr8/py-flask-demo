from flask import Blueprint, jsonify, request, current_app
from .models import Book
from . import db

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Book API!"}), 200

@api.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@api.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@api.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())

@api.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.json
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    db.session.commit()
    return jsonify(book.to_dict())

@api.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

@api.route('/shutdown', methods=['GET'])
def shutdown():
    if not current_app.testing:
        return "Shutdown route is only available in testing mode.", 403
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        return "Unable to shutdown the server.", 500
    func()
    return 'Server shutting down...'