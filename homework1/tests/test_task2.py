#script to test task 2
#this script tests that task 2 creates values with the correct python data types

#import the function from task 2 so we can test the dictionary it returns
from homework1.src.task2 import get_task_values


#define a function that checks that each value in the dictionary has the correct data type
def test_task2_script():

    #call the task 2 function to get the dictionary of values
    vals = get_task_values()

    #assert that the int_value entry is an integer
    assert isinstance(vals["int_value"], int)

    #assert that the float_value entry is a float
    assert isinstance(vals["float_value"], float)

    #assert that the string_value entry is a string
    assert isinstance(vals["string_value"], str)

    #assert that the bool_value entry is a boolean
    assert isinstance(vals["bool_value"], bool)

