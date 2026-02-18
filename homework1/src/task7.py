#script to complete task 7
#this script uses numpy to add two matrices together

#import numpy so we can use arrays and do matrix addition easily
import numpy


#define a function that takes two matrices and returns their sum as a numpy array
def add_two_matrices(first_matrix, second_matrix):

    #convert the first matrix into a numpy array so numpy can do element-by-element math
    first_matrix_as_array = numpy.array(first_matrix, dtype=float)

    #convert the second matrix into a numpy array so it matches the first one in type and shape
    second_matrix_as_array = numpy.array(second_matrix, dtype=float)

    #add the two numpy arrays together element-by-element to produce the summed matrix
    summed_matrix_as_array = first_matrix_as_array + second_matrix_as_array

    #return the resulting numpy array
    return summed_matrix_as_array


#main function
#the main function takes two example matricies, adds them, and prints the result
def main():

    #create the first example matrix as a nested list
    first_matrix = [[1, 2], [3, 4]]

    #create the second example matrix as a nested list
    second_matrix = [[10, 20], [30, 40]]

    #call the matrix addition function and print the summed matrix
    print(add_two_matrices(first_matrix, second_matrix))



if __name__ == "__main__":
    main()
