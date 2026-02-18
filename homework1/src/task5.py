#script to complete task 5
#this script uses a list of favorite books and a dictionary student database


#main function
#the main function prints the first three favorite books and then prints the student database entries
def main():

    #get the full list of favorite books
    favorite_books = get_favorite_books()

    #use list slicing to get only the first three books
    first_three_books = get_first_three_favorite_books(favorite_books)

    #loop through the first three books and print each title and author
    for book_title, book_author in first_three_books:
        print(f"{book_title} by {book_author}")

    #get the student database dictionary
    student_database = get_student_database()

    #loop through the student database and print each student name and student identifier
    for student_name, student_identifier in student_database.items():
        print(f"{student_name}: {student_identifier}")


#define a function that returns a list of favorite books as (title, author) pairs
def get_favorite_books():

    #create the list of favorite books
    favorite_books = [
        ("Holes", "Louis Sachar"),
        ("The Maze Runnerr", "James Dashner"),
        ("Garfield (various)", "Jim Davis"),
        ("It", "Steven King"),
        ("Calvin and Hobbes", "Bill Watterson"),
    ]

    #return the list of favorite books
    return favorite_books


#define a function that returns only the first three books using list slicing
def get_first_three_favorite_books(favorite_books):

    #use list slicing to take the first three items from the list
    first_three_books = favorite_books[:3]

    #return the sliced list
    return first_three_books


#define a function that returns a dictionary mapping student names to student identifiers
def get_student_database():

    #create the student database dictionary
    student_database = {
        "Alice Alison": 1001,
        "Brandon Brandonsen": 1002,
        "Eric Cartman": 1003,
    }

    #return the student database dictionary
    return student_database


if __name__ == "__main__":
    main()

