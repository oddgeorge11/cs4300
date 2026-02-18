#script to complete task 3
#this script includes multiple small functions that practice conditionals, loops, and basic logic


#main function
#the main function runs the task 3 functions and prints their results
def main():

    #print the result of checking a positive number
    print(check_number_value(6))

    #print the result of checking a negative number
    print(check_number_value(-49))

    #print the result of checking zero
    print(check_number_value(0))

    #loop through the first 10 prime numbers and print each one
    for prime_number in first_10_primes():
        print(prime_number)

    #print the sum of the numbers from 1 to 100
    print(sum_1_to_100())


#define a function that checks if a number is positive, negative, or zero
def check_number_value(number_to_check):

    #if the number is greater than zero, return the string "positive"
    if number_to_check > 0:
        return "positive"

    #if the number is less than zero, return the string "negative"
    elif number_to_check < 0:
        return "negative"

    #if the number is exactly zero, return the string "zero"
    elif number_to_check == 0:
        return "zero"


#define a function that checks if a number is prime and returns True or False
def is_number_prime(number):

    #numbers less than 2 are not prime numbers
    if number < 2:
        return False

    #2 is prime
    if number == 2:
        return True

    #any even number greater than 2 is not prime
    if number % 2 == 0:
        return False

    #start checking divisors at 3, and only check odd divisors
    divisor = 3

    #only check divisors up to the square root of the number
    while divisor * divisor <= number:

        #if the number divides evenly, it is not prime
        if number % divisor == 0:
            return False

        #move to the next odd divisor
        divisor += 2

    #if no divisor worked, the number is prime
    return True


#define a function that returns a list containing the first 10 prime numbers
def first_10_primes():

    #create an empty list where we will store prime numbers
    primes = []

    #try candidate numbers starting at 2, and keep going until we find 10 primes
    for candidate in range(2, 1000):

        #if the candidate is prime, add it to the list
        if is_number_prime(candidate):
            primes.append(candidate)

            #stop once we have found 10 prime numbers
            if len(primes) == 10:
                break

    #return the list of the first 10 prime numbers
    return primes


#define a function that sums the integers from 1 to 100 and returns the total
def sum_1_to_100():

    #start the running total at zero
    sum = 0

    #start counting at 1
    i = 1

    #keep adding numbers until we reach 100
    while i <= 100:

        #add the current number to the running total
        sum += i

        #move to the next number
        i += 1

    #return the final sum
    return sum


if '__name__' == '__main__':
    main()
