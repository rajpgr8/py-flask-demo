
import unittest
import json
from app import create_app, db
from app.models import Book

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_books(self):
        book = Book(title='Test Book', author='Test Author')
        db.session.add(book)
        db.session.commit()

        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Test Book')

    def test_add_book(self):
        new_book = {
            'title': 'New Book',
            'author': 'New Author'
        }
        response = self.client.post('/books', json=new_book)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'New Book')
        self.assertEqual(data['author'], 'New Author')

    def test_get_book(self):
        book = Book(title='Test Book', author='Test Author')
        db.session.add(book)
        db.session.commit()

        response = self.client.get(f'/books/{book.id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Book')
        self.assertEqual(data['author'], 'Test Author')

    def test_update_book(self):
        book = Book(title='Test Book', author='Test Author')
        db.session.add(book)
        db.session.commit()

        updated_book = {
            'title': 'Updated Book',
            'author': 'Updated Author'
        }
        response = self.client.put(f'/books/{book.id}', json=updated_book)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Updated Book')
        self.assertEqual(data['author'], 'Updated Author')

    def test_delete_book(self):
        book = Book(title='Test Book', author='Test Author')
        db.session.add(book)
        db.session.commit()

        response = self.client.delete(f'/books/{book.id}')
        self.assertEqual(response.status_code, 204)

        # Verify the book is deleted
        response = self.client.get(f'/books/{book.id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
