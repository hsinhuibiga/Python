#print (hellow)

print ("hellow")

# Program to generate a random number between 0 and 9

# import the random module
import random

print(random.randint(0,9))


# Python Program to find the factors of a number

# define a function
def print_factors(x):
   # This function takes a number and prints the factors

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

# change this value for a different result.
num = 320

# uncomment the following line to take input from the user
#num = int(input("Enter a number: "))

print_factors(num)

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2014
mm = 11

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

import calendar

yy= 2017
mm= 12

print(calendar.month(yy,mm))



# Program to sort alphabetically the words form a string provided by the user

# change this value for a different result
my_str = "Hello this Is an Example With cased letters"

# uncomment to take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
#my exercise

my_str = "I am the most beatiful woman of the world"
words= my_str.split()
words.sort()
print("The sorted words are:")
for word in words:
    print(word)
# Python program to find the sum of natural numbers up to n using recursive function

def recur_sum(n):
   """Function to return the sum
   of natural numbers using recursion"""
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = 16

# uncomment to take input from the user
#num = int(input("Enter a number: "))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))

