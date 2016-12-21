"""
FizzBuzz

In the original game of Fizz Buzz, you count from 1 to a given number
If the number is divisible by 3, instead of the number you say fizz
If it is divisible by 5 you say buzz 
And finally if it is divisible by both 3 and 5 you say fizz buzz
"""

print("Please enter a number between 1 and 100")
number = input()

for i in range (1, number + 1):
    if i%3 == 0 and i%5 ==0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)