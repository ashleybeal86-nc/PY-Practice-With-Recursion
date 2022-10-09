# Bonus: Write a function that when given two numbers, finds their greatest common divisor.

## (The greatest common divisor of two integers is the largest positive integer that divides both of the integers. For example, look at the numbers 10 and 15: 10 can be divided by 1, 5, and 10, 15 can be divided by 1, 3, 5, and 15.)
## (When we say 'can be divided' here we mean divided evenly, so in other words there is no remainder. For example when 15 is divided by 6, there is a remainder of 3 because 15=6(2)+3 so 6 is not a divisor of 15.)
## (The greatest common divisor of 15 and 10 is 5 since both numbers can be divided by 5.)


def greatest_common_divider(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divider(b, a % b)

print("greatest common divider of 15 and 10:", greatest_common_divider(15,10))
print("greatest common divider of 46 and 12:", greatest_common_divider(46,12))
