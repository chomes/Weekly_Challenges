# PROBLEM:
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# --------------------------------------------------------------------
# This method takes the starting number and end number of your range
# it then takes the number you wish to find multiples of
# it then returns a list of natural numbers base on your provided multiple
# This was my answer to https://projecteuler.net/problem=1


def multiples_of_multiples(start_num, end_num, multiple_num):
    # init list of multiple items
    multiples_of_num = []
    # loop through the range provided by the arguments
    for i in range(start_num, end_num):
        # check to see if the number has a remainder of 0
        if i % multiple_num == 0:
            # if the number is remainder 0 then add it to the list
            multiples_of_num.append(i)
            # returns a list of multiple numbers
    return multiples_of_num

# This function takes any number of lists as an argument
# it then iterates through the lists and returns the sum total


def return_sum_of_multiples(*args):
    # init of sum total
    sum_total = 0
    print(args)
    # loop over args which come in as tuples
    for arg in args:
        # loop over items in the lists inside the tuples
        for i in arg:
            # add each item in the lists to the sum total
            sum_total += i
    return sum_total


a = return_sum_of_multiples(multiples_of_multiples(1, 1001, 3), multiples_of_multiples(1, 1001, 5))

print("Your total is: %a" % a)
