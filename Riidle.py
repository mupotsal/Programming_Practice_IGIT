######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your name
# Username: heggens             TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
my_input = input('What is Your birth year?')

print('You were born in: ' + my_input + '!')

print('')



# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples
if my_input == '2000':
    print('You were born in the year of a fire breathing beast!')
    print('The might Dragon!!!')

elif my_input == '2001':
    print('You slithering Snake')
    print('The animal for your birth year is snake')

elif my_input == '2002':
    print('You mighty stallion')
    print('You were born in the year of the horse')

elif my_input == '2003':
    print('You are the greatest of all time')
    print('You were born in the year of the Goat')

elif my_input == '2004':
    print('You must really like the yellow potassium berry')
    print('You were born in the year of the Monkey')

elif my_input == '2005':
    print('cock-a-doodle-do')
    print('Congratulation you big bird, You were born in the year of the rooster')

elif my_input == '2006':
    print('Who let the dogs out?')
    print('You were born in the year of the Dog')

elif my_input == '2007':
    print('oink oink')
    print('You were born in the year of the pig')

elif my_input == '2008':
    print("I heard bad convicts don't like this animal")
    print('You were born in the year of the Rat')

elif my_input == '2009':
    print('You are so healthy!, You are as strong as an ...?')
    print('You are as strong as an Ox')
    print('The animal for your year is an Ox')

elif my_input == '2010':
    print('You are a very big cat, not a Lion but a...? ')
    print('You are a Tiger')
    print('The animal for the year 2010 is a tiger')

elif my_input == '2011':
    print('What is a grown up bunny called?')
    print('A grown up bunny is called a rabbit and that is what you are')
    print('You were born in the year of the rabbit')
    print('')

######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
my_input = input('What is the birth year of year friend')

if my_input == '2000':
    print("your friend was born in the year of the Dragon")

elif my_input == '2001':
    print('your friend is a Snake')
elif my_input == '2002':
    print('your friend is a Goat')
elif my_input == "2003":
    print('your friend is a horse ')

elif my_input == "2004":
    print('your friend is a Monkey ')

elif my_input == "2005":
    print('your friend is a Rooster')

elif my_input == "2006":
    print('your friend is a Dog')

elif my_input == "2007":
    print('your friend is a Pig')

elif my_input == "2008":
    print('your friend is a Rat')
elif my_input == "2009":
    print('your friend is a OX')
elif my_input == "2010":
    print('your friend is a Tiger')
elif my_input == "2011":
    print('your friend is a Rabbit')

# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
