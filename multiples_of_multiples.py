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
    multiples_of_num = []
    for i in range(start_num, end_num):
        if i % multiple_num == 0:
            multiples_of_num.append(i)
    return multiples_of_num

