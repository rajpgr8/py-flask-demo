# Flask Book API

This is a simple Flask-based REST API for managing a book collection. It provides basic CRUD operations for books and includes unit tests, integration tests, and BDD tests.

## Prerequisites

- Python 3.7+
- pip
- virtualenv (optional, but recommended)
- Docker (optional, for containerization)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/flask-book-api.git
   cd flask-book-api
   ```

2. Create and activate a virtual environment (optional):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask application:
   ```
   python run.py
   ```

2. The API will be available at `http://localhost:5000`

## API Endpoints

- GET /books: Retrieve all books
- POST /books: Add a new book
- GET /books/<id>: Retrieve a specific book
- PUT /books/<id>: Update a specific book
- DELETE /books/<id>: Delete a specific book

## Running Tests

### Unit Tests and Integration Tests

Run the following command:
```
python -m unittest discover tests
```

### BDD Tests

1. Ensure that the Flask application is running in a separate terminal window.

2. Run the behave tests:
   ```
   behave
   ```

## Docker Support

To build and run the application using Docker:

1. Build the Docker image:
   ```
   docker build -t flask-book-api .
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 flask-book-api
   ```

The API will be available at `http://localhost:5000`

## Development

To add new features or modify existing ones:

1. Create a new branch:
   ```
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and write tests for new functionality.

3. Run all tests to ensure everything is working:
   ```
   python -m unittest discover tests
   behave
   ```


