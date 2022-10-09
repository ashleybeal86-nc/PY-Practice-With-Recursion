# Write code for algorithm 1 below
#1. Write a program that takes a positive number as an argument and prints the numbers from n to zero.

def numbers_count_down(v):
    # Base case
    if v==0:
        return
    
    # Recursive case
    else:
        print(v)
        numbers_count_down(v-1)

    # test case
    v=8
    numbers_count_down(v)



    ######### Another Possible Way to Solve ########


def numbers_count_down(v):
    # inherent base case
    # (will stop if v <= 0)
    if v>0:
        #recursive case
        print(v)
        numbers_count_down(v-1)

    # test case
    v=8
    numbers_count_down(v)
