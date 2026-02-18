#script to test task 5
#this script tests that the task 5 functions return the correct data types and expected contents

#import the task 5 functions so we can test them
from homework1.src.task5 import get_favorite_books, get_first_three_favorite_books, get_student_database


#define a function that tests that get_favorite_books returns a list of (title, author) pairs
def test_favorite_books_is_list_of_title_author_pairs():

    #call the function to get the favorite books list
    favorite_books = get_favorite_books()

    #assert that the returned value is a list
    assert isinstance(favorite_books, list)

    #assert that the list has at least three books so slicing can work
    assert len(favorite_books) >= 3

    #get the first book entry so we can check its structure
    first_book = favorite_books[0]

    #assert that a single book entry is a tuple
    assert isinstance(first_book, tuple)

    #assert that the tuple has exactly two items: title and author
    assert len(first_book) == 2

    #unpack the tuple into a title and an author
    book_title, book_author = first_book

    #assert that the title is a string
    assert isinstance(book_title, str)

    #assert that the author is a string
    assert isinstance(book_author, str)


#define a function that tests that the first three books are returned using list slicing
def test_first_three_favorite_books_slicing():

    #get the full favorite books list
    favorite_books = get_favorite_books()

    #get the first three books using the function
    first_three_books = get_first_three_favorite_books(favorite_books)

    #assert that the function result matches what list slicing would do
    assert first_three_books == favorite_books[:3]

    #assert that the returned list has exactly three items
    assert len(first_three_books) == 3


#define a function that tests that get_student_database returns a dictionary from name to identifier
def test_student_database_is_dictionary_name_to_identifier():

    #call the function to get the student database dictionary
    student_database = get_student_database()

    #assert that the returned value is a dictionary
    assert isinstance(student_database, dict)

    #assert that the dictionary has at least one entry
    assert len(student_database) > 0

    #loop through each key and value to check their types
    for student_name, student_identifier in student_database.items():

        #assert that the student name is a string
        assert isinstance(student_name, str)

        #assert that the student identifier is an integer
        assert isinstance(student_identifier, int)

