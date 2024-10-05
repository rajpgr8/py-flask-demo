import unittest
from app import create_app, db
from app.models import Book

class TestBookModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_book_model(self):
        book = Book(title='Test Book', author='Test Author')
        db.session.add(book)
        db.session.commit()

        retrieved_book = Book.query.get(1)
        self.assertEqual(retrieved_book.title, 'Test Book')
        self.assertEqual(retrieved_book.author, 'Test Author')

    def test_book_to_dict(self):
        book = Book(id=1, title='Test Book', author='Test Author')
        book_dict = book.to_dict()
        self.assertEqual(book_dict, {
            'id': 1,
            'title': 'Test Book',
            'author': 'Test Author'
        })

if __name__ == '__main__':
    unittest.main()