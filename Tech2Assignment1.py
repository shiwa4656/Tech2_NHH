"""
TECH2 Assignment 1

Hello! Here is my attempt at Assigment 1 in TECH2.
I wanted to try and solve it without any help, so I have not used AI or any other sources.
There was just one thing I couldn't figure out that I had to google:
How to print the content of a list without spaces and brackets (see line 65)

"""

# Import random module to randomize
import random

# Import string module for character sets
import string

# Make string with special characters
special_character = '!@#$%^&*()-_=+'

# Create a tuple with the desired password lenghts
password_range = ('8', '9', '10', '11', '12', '13', '14', '15', '16')

# Ask user to enter password lenght
lenght = input('Enter the desired password lenght (8-16): ')

# Create self-defined function that checks user input and generates password
def password(lenght):
    
    # While loop that gives user an error message and asks for a new input as long as the input is out of range or non-numeric
    while lenght not in password_range:
        print('Error: password lenght must be between 8 and 16 charachters.')
        lenght = input('Enter the desired password lenght (8-16): ')
    
    # Make password lenght an integer
    lenght = int(lenght)
    
    # Create empty list to store the first character of the password
    password1 = []
    # Create empty list to store the remaining characters of the password
    password2 = []
    
    # Randomly generate first character, must be a lowercase or uppercase letter
    password1.append(random.choice(string.ascii_uppercase or string.ascii_lowercase))
    
    # Randomly generate one lowercase letter to meet the required minimum
    password2.append(random.choice(string.ascii_lowercase))
    
    # Randomly generate one uppercase letter to meet the required minimum
    password2.append(random.choice(string.ascii_uppercase))
    
    # Randomly generate one digit to meet the required minimum
    password2.append(random.choice(string.digits))
    
    # Randomly generate one special character to meet the required minimum
    password2.append(random.choice(special_character))
    
    # Randomly generate lowercase letters, uppercase letters, digits and special characters
    for i in range(lenght - 5):
        password2.append(random.choice(string.ascii_lowercase or string.ascii_uppercase or string.digits or special_character))
    
    # Shuffle list to make it random
    random.shuffle(password2)
    
    # Print the generated password to the user
    print('Generated password: ',*password1 + password2, sep = '')

password(lenght)


"""
Here is my abandoned attempt at checking if the user input is valid.
First I check whether the input is a digit.
If not, the user gets an error message and gets prompted until they write in a digit.
Then I go on to check whether that digit matches the password lenght (8-16).
If not, the user gets and error message and gets propmted again.
The problem is if the user at this point enters a non-digit.
Then it's not possible to convert it into an integer to check the lenght again.
I was not able to find a way to check the lenght at the same time as the input was a non-digit.
That's why I abandoned this method and decided to try a solution with a tuple, like I have done above.
I realize that if the range of the password lenght was bigger, the tuple would not be a great solution.
But for this program it works.


if not lenght.isdigit():
    
    while not lenght.isdigit() :
        print('Error: password lenght must be between 8 and 16 charachters.')
        lenght = input('Enter the desired password lenght (8-16): ')
    
    lenght = int(lenght)
    
    while not 8 <= lenght <= 16:
        print('Error: password lenght must be between 8 and 16 charachters.')
        lenght = input('Enter the desired password lenght (8-16): ')
        lenght = int(lenght)

else:
    lenght = int(lenght)
    
    while not 8 <= lenght <= 16:
        print('Error: password lenght must be between 8 and 16 charachters.')
        lenght = input('Enter the desired password lenght (8-16): ')
        lenght = int(lenght)
    

"""
    
    
    
    
