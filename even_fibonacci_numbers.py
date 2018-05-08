# PROBLEM:
# Each new term in the Fibonacci sequence is generated by adding
# the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.
# ---------------------------------------------------------------------------------
# The below function creates the fibonacci sequence based on the users end number.


def fibonacci_sequence(end_num):
    # creates the first two numbers in the sequence
    fibonacci_list = [1, 2]
    # this boolean value is used to keep the loop going until it reaches the
    # users number
    over_end_num = False
    while not over_end_num:
        # This section will add the last two terms together
        next_term = fibonacci_list[-2] + fibonacci_list[-1]
        # this checks if that number is above the user defined end term
        if next_term >= end_num:
            # if the term is above the user defined number then this is
            # set to true and the loop ends
            over_end_num = True
        else:
            # if the term is not above the user limit then it is added to the list
            fibonacci_list.append(next_term)
    return fibonacci_list


# this function returns the sum of all even numbers
def sum_of_even(a_list):
    # init sum var
    sum_of = 0
    # loops through the list
    for i in a_list:
        # this checks if the number returns no remainder when divided by two
        if i % 2 == 0.0:
            # if it does not then it is added to the sum var
            sum_of += i
    return sum_of


# this function returns the sum of all odd numbers
# it works in much the same way as the even
def sum_of_odd(a_list):
    sum_of = 0
    for i in a_list:
        # however its looking to see if the number divided by two is greater than 0.0
        if i % 2 > 0.0:
            sum_of += i
    return sum_of


print(sum_of_odd(fibonacci_sequence(120000000)))