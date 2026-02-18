#script to test task 3
#this script tests that the task 3 functions return the correct results

#import pytest so we can use parametrized tests
import pytest

#import the functions we wrote so we can test them
from homework1.src.task3 import check_number_value, first_10_primes, sum_1_to_100


#define a set of test cases for checking if a number is positive, negative, or zero
@pytest.mark.parametrize(
    "number_to_check, expected",
    [
        (10, "positive"),
        (1, "positive"),
        (-1, "negative"),
        (-999, "negative"),
        (0, "zero"),
    ],
)
def test_check_number_value(number_to_check, expected):

    #assert that the function returns the expected string for each input
    assert check_number_value(number_to_check) == expected


#define a function that tests that the list of the first 10 primes is correct
def test_first_10_primes():

    #assert that the function returns the first 10 prime numbers in order
    assert first_10_primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


#define a function that tests that summing 1 through 100 returns 5050
def test_sum_1_to_100():

    #assert that the sum of integers from 1 to 100 is 5050
    assert sum_1_to_100() == 5050

