#script to complete task 4
#this script calculates a discounted price using a percent discount


#main function
#the main function calls calculate_discount with example values and prints the results
def main():

    #print the discounted result for an integer price and integer discount percent
    print(calculate_discount(100, 20))

    #print the discounted result for a float price and float discount percent
    print(calculate_discount(199.99, 10.0))


#define a function that validates inputs, converts inputs to floats, applies the percent discount, and returns the discounted price
def calculate_discount(price_value, discount_value):

    #try converting the price to a float so we can check that it is a valid number
    try:
        price_as_float = float(price_value)
    except (TypeError, ValueError):
        raise ValueError("price_value must be a number")

    #try converting the discount percent to a float so we can check that it is a valid number
    try:
        discount_as_float = float(discount_value)
    except (TypeError, ValueError):
        raise ValueError("discount_value must be a number")

    #check that the price is not negative
    if price_as_float < 0:
        raise ValueError("price_value must be nonnegative")

    #check that the discount percent is between 0 and 100 inclusive
    if discount_as_float < 0 or discount_as_float > 100:
        raise ValueError("discount_value must be between 0 and 100")

    #compute the discounted price by subtracting the discount percent from 100 percent
    discounted_price = price_as_float * (1.0 - (discount_as_float / 100.0))

    #return the final discounted price
    return discounted_price


if __name__ == "__main__":
    main()

