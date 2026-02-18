#script to test task 6
#this script tests that the task6_read_me.txt file has the expected word count

#import Path so we can build the file path to task6_read_me.txt
from pathlib import Path

#import pytest so we can use a parametrized test
import pytest

#import the word counting function so we can test it
from homework1.src.task6 import count_words_in_file


#define a list of test cases for the file name and expected word count
@pytest.mark.parametrize(
    "file_name, expected_word_count",
    [
        ("task6_read_me.txt", 104),
    ],
)
def test_task6_read_me_word_count(file_name, expected_word_count):

    #get the homework1 directory by starting from this test file location and going up one folder
    homework1_directory = Path(__file__).resolve().parents[1]

    #create the full path to the text file we want to count words in
    file_path = homework1_directory / file_name

    #assert that the counted number of words matches the expected number
    assert count_words_in_file(file_path) == expected_word_count

