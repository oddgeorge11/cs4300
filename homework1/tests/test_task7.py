#script to test task 7
#this script tests that numpy matrix addition works correctly in our function

#import numpy so we can create the expected numpy arrays for comparison
import numpy

#import the function we wrote so we can test it
from homework1.src.task7 import add_two_matrices


#define a function that tests adding two integer matrices
def test_add_two_matrices_integers():

    #create the first matrix using integers
    first_matrix = [[1, 2], [3, 4]]

    #create the second matrix using integers
    second_matrix = [[10, 20], [30, 40]]

    #create the expected result matrix after addition
    expected_matrix = numpy.array([[11, 22], [33, 44]], dtype=float)

    #call the function and store the returned result matrix
    result_matrix = add_two_matrices(first_matrix, second_matrix)

    #assert that the result matrix matches the expected matrix exactly
    assert numpy.array_equal(result_matrix, expected_matrix)


#define a function that tests adding two float matrices
def test_add_two_matrices_floats():

    #create the first matrix using float values
    first_matrix = [[1.5, 2.5], [3.5, 4.5]]

    #create the second matrix using float values
    second_matrix = [[0.5, 1.5], [2.5, 3.5]]

    #create the expected result matrix after addition
    expected_matrix = numpy.array([[2.0, 4.0], [6.0, 8.0]], dtype=float)

    #call the function and store the returned result matrix
    result_matrix = add_two_matrices(first_matrix, second_matrix)

    #assert that the result matrix matches the expected matrix exactly
    assert numpy.array_equal(result_matrix, expected_matrix)

