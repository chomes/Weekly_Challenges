# The challenge here is to create a bubble search in python
# without using the any sort functions

my_list = [12, 5, 13, 8, 9, 65, 1009, 84, 66, 69, 2, 11, 6, 6]

# def reusable function
def bubble(a_list):
    # this determines the length of the list -1 because a list starts at 0
    length = len(a_list) - 1
    # this is a boolean value to allow the while loop to keep running
    sorted = False

    while not sorted:
        # set the loop to True so that if the if statement find nothing
        # to sort then it will end the while loop
        sorted = True
        for i in range(length):
            # test if the current list item is greater than that of the next list item
            if a_list[i] > a_list[i+1]:
                # if a value is found and needs to be sorted we set the list value back to
                # False so the while loop will run again.
                sorted = False
                # if it is then this code swaps them
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]


bubble(my_list)
print(my_list)
