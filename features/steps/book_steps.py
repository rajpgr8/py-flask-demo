from behave import given, when, then
import requests
import json

API_URL = "http://localhost:5000"

@given('the API is running')
def step_impl(context):
    response = requests.get(f"{API_URL}/")
    assert response.status_code == 200

@given('there is a book with id {id}')
def step_impl(context, id):
    # Ensure a book exists with the given id
    data = {"title": "Existing Book", "author": "Existing Author"}
    response = requests.post(f"{API_URL}/books", json=data)
    assert response.status_code == 201
    context.book_id = json.loads(response.text)['id']

@when('I send a GET request to "{endpoint}"')
def step_impl(context, endpoint):
    context.response = requests.get(f"{API_URL}{endpoint}")

@when('I send a POST request to "{endpoint}" with the following data')
def step_impl(context, endpoint):
    data = context.table[0].as_dict()
    context.response = requests.post(f"{API_URL}{endpoint}", json=data)

@when('I send a PUT request to "{endpoint}" with the following data')
def step_impl(context, endpoint):
    data = context.table[0].as_dict()
    context.response = requests.put(f"{API_URL}{endpoint}", json=data)

@when('I send a DELETE request to "{endpoint}"')
def step_impl(context, endpoint):
    context.response = requests.delete(f"{API_URL}{endpoint}")

@then('I should receive a {status_code:d} status code')
def step_impl(context, status_code):
    assert context.response.status_code == status_code

@then('I should receive an empty list of books')
def step_impl(context):
    assert context.response.json() == []

@then('the response should contain the new book details')
def step_impl(context):
    data = context.response.json()
    assert 'id' in data
    assert data['title'] == "Test Book"
    assert data['author'] == "Test Author"

@then('the response should contain the book details')
def step_impl(context):
    data = context.response.json()
    assert 'id' in data
    assert 'title' in data
    assert 'author' in data

@then('the response should contain the updated book details')
def step_impl(context):
    data = context.response.json()
    assert data['title'] == "Updated Book"
    assert data['author'] == "Updated Author"