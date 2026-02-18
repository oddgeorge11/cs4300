#script to test task 4
#this script tests that calculate_discount returns correct results and rejects invalid inputs

#import pytest so we can test for exceptions
import pytest

#import the calculate_discount function so we can test it
from homework1.src.task4 import calculate_discount


#define a function that tests integer price and integer discount percent
def test_calculate_discount_integer_inputs():

    #assert that 20 percent off of 100 is 80.0
    assert calculate_discount(100, 20) == 80.0


#define a function that tests float price and float discount percent
def test_calculate_discount_float_inputs():

    #assert that 10 percent off of 199.99 is 179.991
    assert calculate_discount(199.99, 10.0) == 179.991


#define a function that tests mixed inputs where the price is a float and the discount is an integer
def test_calculate_discount_mixed_inputs():

    #assert that 20 percent off of 100.0 is 80.0
    assert calculate_discount(100.0, 20) == 80.0


#define a function that tests that a negative price raises an error
def test_calculate_discount_negative_price_raises_error():

    #assert that a negative price is rejected
    with pytest.raises(ValueError):
        calculate_discount(-1, 20)


#define a function that tests that a discount below 0 raises an error
def test_calculate_discount_discount_below_zero_raises_error():

    #assert that a discount percent below 0 is rejected
    with pytest.raises(ValueError):
        calculate_discount(100, -1)


#define a function that tests that a discount above 100 raises an error
def test_calculate_discount_discount_above_one_hundred_raises_error():

    #assert that a discount percent above 100 is rejected
    with pytest.raises(ValueError):
        calculate_discount(100, 101)

