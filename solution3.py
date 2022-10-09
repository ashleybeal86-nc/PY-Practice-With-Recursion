# Write code for algorithm 3 below
# 3. Write a function that returns the nth elements in the Fibonacci Sequence.

#(The Fibonacci Sequence is the series of numbers where the next number is found by adding up the two numbers before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...)
#(For example, if n=4, then the result would be '2' and if n=2, the result would be '1')

def nth_fib_sequence_num(n):
    if n <= 0:
        print("not a correct number")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fib_sequence_num(n-1) + nth_fib_sequence_num(n-2)
    print("second number in the sequence:")
    print(nth_fib_sequence_num(2))
    print("fourth number in the sequence:")
    print(nth_fib_sequence_num(4))
    print("eighth number in the sequence:")
    print(nth_fib_sequence_num(8))
