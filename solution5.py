# Write code for algorithm 5 below
#5. Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.

#(A palindrome is a word that is the same when it is reversed, such as madam, radar, kayak, or tacocat.)

def is_a_palindrome(lettersinstring):
    if len(lettersinstring) == 1 or len(lettersinstring) == 0:
        return True
    else:
        return (lettersinstring[0]  == lettersinstring[-1]) and is_a_palindrome(lettersinstring[1:-1])

print("is 'apple' a palindrome?")
print(is_a_palindrome('apple'))
print("is 'tacocat' a palindrome?")
print(is_a_palindrome('tacocat'))
print("is 'racecar' a palindrome?")
print(is_a_palindrome('racecar'))
print("is 'madam' a palindrome?")
print(is_a_palindrome('madam'))
