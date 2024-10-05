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


### Building the Docker Image

To build the Docker image:

1. Ensure you're in the root directory of the project where the Dockerfile is located.
2. Run the following command:

   ```
   docker build -t flask-book-api .
   ```

### Running the Container

To run the container:

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

### Building the Docker Image

To build the Docker image:

1. Ensure you're in the root directory of the project where the Dockerfile is located.
2. Run the following command:

   ```
   docker build -t flask-book-api .
   ```

### Running the Container

To run the container:


The API will be available at `http://localhost:5000`

### Dockerfile Optimizations

Our Dockerfile includes several optimizations:

1. **Multi-stage build**: We use a multi-stage build to create a smaller final image. The `builder` stage installs the dependencies, and we only copy the installed packages to the final image.

2. **Caching dependencies**: By copying and installing the `requirements.txt` file before copying the rest of the application code, we leverage Docker's cache mechanism for faster builds when requirements don't change.

3. **Combining ENV instructions**: Multiple ENV instructions are combined into a single instruction to reduce the number of layers in the final image.

4. **Slim base image**: We use the slim version of the Python image to reduce the final image size.

5. **No cache for pip**: The `--no-cache-dir` flag for pip is used to keep the image size down.

6. **Strategic COPY instruction**: The `COPY . .` instruction is placed near the end of the Dockerfile to leverage cache for most layers when only application code changes.

These optimizations result in a smaller final image and potentially faster build times, especially when making frequent changes to the application code.

### Rebuilding the Image

If you make changes to your application, you'll need to rebuild the Docker image to include those changes. Just run the `docker build` command again:

