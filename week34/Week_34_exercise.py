import random

#exercise_1
""" Write a program that divides two integers:
• Use the input function to prompt the user for two
integer values
• Divide the first number on the second number
• Display the result of the operation with one decimal
"""
user_input_1 = int(input("put your first number that you want to divide: "))
user_input_2 = int(input("put your second number that you want to divide by:  "))
result = user_input_1/user_input_2
print(f"Result : {result:.1f}")

#exercise_2
''' 
• Write a program that divides two floats:
• Use the input function to prompt the user for two
float values
• Divide the first number on the second number
• Display the result of the operation with two decimals
'''

user_3 = float(input("put your first float number that you want to divide: "))
user_4 = float(input("put your second float number that you want to divide by:  "))
result_2 = user_3/user_4
print(f"Result : {result_2:.2f}")

#exercise_3
'''
Write a program that draws a random number between
a lower and upper bound:
• Use the input function to prompt the user for a lower
and upper bound
• Use randint function from random to draw a random
integer between the user-supplied bounds (see the
function documentation ℎ𝑒𝑟𝑒)
• Display the random number
'''
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))
random_number = random.randint(lower_bound, upper_bound)
print(f"Random number: {random_number}")

#exercise_4
'''Write a program that converts a temperature from
Fahrenheit to Celsius:
• Use the input function to prompt the user for a
temperature in Fahrenheit
• Convert the temperature using the formula:
𝐶𝑒𝑙𝑐 = 5
9 × (𝐹𝑎ℎ𝑟 − 32)
• Display the converted temperature rounded to the
nearest integer
'''

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = 5/9 * (fahrenheit - 32)
print(f"Temperature in Celsius: {round(celsius)}°C")
