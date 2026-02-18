#script to complete task 6
#this script reads a text file and counts how many words it contains

#import regular expressions so we can find word-like chunks of text
import re

#import Path so we can build file paths reliably
from pathlib import Path


#main function
#the main function builds the file path to task6_read_me.txt and prints the word count
def main():

    #get the homework1 directory by starting from this file location and going up one folder
    homework1_directory = Path(__file__).resolve().parents[1]

    #create the full path to the task6_read_me.txt file inside the homework1 folder
    read_me_path = homework1_directory / "task6_read_me.txt"

    #print the number of words found in the file
    print(count_words_in_file(read_me_path))


#define a function that reads a file and returns how many words it contains
def count_words_in_file(file_path):

    #convert the incoming file path into a Path object so we can read the file
    file_path_object = Path(file_path)

    #read the entire file into one string
    file_contents = file_path_object.read_text(encoding="utf-8")

    #find every sequence of letters and digits and treat each sequence as one word
    words = re.findall(r"[A-Za-z0-9]+", file_contents)

    #return the number of word matches found
    return len(words)


if __name__ == "__main__":
    main()

