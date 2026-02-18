#script to complete task 2
#this script demonstrates different python data types by printing values and their types


#define a function that gets a dictionary of example values and prints each value with its type
def main():
    value_dict = get_task_values()

    #loop through each key and value in the dictionary and print the value and its data type name
    for variable_name, variable_value in value_dict.items():
        print(f"{variable_name}: {variable_value} ({type(variable_value).__name__})")


#define a function that creates example values and returns them in a dictionary
def get_task_values():

    #create an integer example value
    int_value = 25

    #create a float example value
    float_value = 13.4

    #create a string example value
    string_value = "Yo mama!"

    #create a boolean example value
    bool_value = False

    #return all values in a dictionary so main can print them
    return {
        "int_value": int_value,
        "float_value": float_value,
        "string_value": string_value,
        "bool_value": bool_value,
    }


if __name__ == "__main__":
    main()

