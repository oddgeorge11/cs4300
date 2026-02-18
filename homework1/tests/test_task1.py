#script to test task 1
#this script tests that task 1 prints the exact Hello, World! output

#import the main function from the task 1 code so we can call it in the test
from homework1.src.task1 import main


#define a function that runs main, captures what it prints, and checks that it matches exactly
def test_task1(capsys):

    #run the task 1 main function so it prints to standard output
    main()

    #capture the printed output so we can compare it to the expected string
    captured_stdout_variable = capsys.readouterr()

    #assert that the captured output matches the exact expected output including the newline
    assert captured_stdout_variable.out == "Hello, World!\n"

