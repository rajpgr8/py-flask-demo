Feature: Book API
  As an API user
  I want to manage books
  So that I can keep track of my library

  Scenario: Get all books
    Given the API is running
    When I send a GET request to "/books"
    Then I should receive a 200 status code
    And I should receive an empty list of books

  Scenario: Add a new book
    Given the API is running
    When I send a POST request to "/books" with the following data:
      | title       | author        |
      | Test Book   | Test Author   |
    Then I should receive a 201 status code
    And the response should contain the new book details

  Scenario: Get a specific book
    Given the API is running
    And there is a book with id 1
    When I send a GET request to "/books/1"
    Then I should receive a 200 status code
    And the response should contain the book details

  Scenario: Update a book
    Given the API is running
    And there is a book with id 1
    When I send a PUT request to "/books/1" with the following data:
      | title           | author            |
      | Updated Book    | Updated Author    |
    Then I should receive a 200 status code
    And the response should contain the updated book details

  Scenario: Delete a book
    Given the API is running
    And there is a book with id 1
    When I send a DELETE request to "/books/1"
    Then I should receive a 204 status code
