# Write code for algorithm 4 below
# 4. Write a function that calculates the value of 'a' to the power of 'b'.

def a2b_power(a,b):
    if b < 1:
        print("not a possible value, b cannot be less than 1")
    elif b == 1:
        return a
    else:    
        return a * a2b_power(a, b-1)

    print("2^4:")
    print(a2b_power(2,4))
    
