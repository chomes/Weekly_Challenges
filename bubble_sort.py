# The challenge here is to create a bubble search in python
# without using the any sort functions

my_list = [12, 5, 13, 8, 9, 65, 1009, 84, 66, 69, 2, 11, 6, 6]


def bubble(a_list):
    length = len(a_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if a_list[i] > a_list[i+1]:
                sorted = False
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]


bubble(my_list)
print(my_list)
