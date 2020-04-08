
#Name: HsinHui Lin ; student ID:28464176 ; the start date:16 Mar 2018 ; the last modified date: 26 Mar 2018
#Task one:
"""I hope the dictionay could present the Morse Code well. The CODE is key: value design. Then format CODE_REVERSED. Using
    CODE_REVERSED in extracting the translated words. Add * in the dictionary. The * represents the meaning of blank. """
CODE = {"A": "01", "B":"1000", "C":"1010","D":"100","E":"0","F":"0010","G":"110","H":"0000","I":"00", "J":"0111","K":"101" \
        ,"L":"0100","M":"11","N":"10","O":"111","P":"0110","Q":"1101","R":"010","S":"000","T":"1","U":"001","V":"0001",
        "W":"011", "X":"1001","Y":"1011","Z":"1100","0":"11111","1":"01111","2":"00111","3":"00011","4":"00001","5":"00000" \
        ,"6":"10000","7":"11000","8":"11100","9":"11110", " ":" "}
CODE_REVERSED = {value:key for key,value in CODE.items()}

#I tried several ways and found that using def function which could translate unlimited morse codes.

def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())


keyinput1=input("The first sequence ?")

"""I use the if-else clause at the very beginning, but the clause could not present well. Then I use ValueError
   as the except condtion which is not enough. I add TypeError which could complete all the Except condition.
"""

try:
    print("Work! It's the Morse code.The first sequence is",from_morse(keyinput1))
except ValueError and TypeError:
    print("Not Morse Code.You should try again.")

"""Inorder to let the user input valid morse code. I think yes/no choice here could be a good point for users to
 think if they want to move on or stop."""
"""I made a mistake here. I used <if input in yesChoice> and the system runed in error. The problem solved when I 
changed into<if ask1 in yesChoice>. I choose exit(0) to end the program. Because exit(0) is a simple expression. I 
also check the difference between exit(1) and exit(0)."""

yesChoice = ['yes','y']
noChoice = ['no','n']
ask1=input("Do you wish to continune?(y/n) ").lower()
# Check the answer in one of two sets.
if ask1 in yesChoice:
   pass
else:
   exit(0)

keyinput2=input("The second sequence ?")

try:
    print("Work! The second sequence is", from_morse(keyinput2))
except ValueError and TypeError:
    print("Not Morse Code.You should try again.")

yesChoice = ['yes', 'y']
noChoice = ['no', 'n']
ask2=input("Do you wish to continune?(y/n) ").lower()
if ask2 in yesChoice:
   pass
else:
   exit(0)

"""There is no need to ask user if want to move on at the third sequence."""

keyinput3=input("The third sequence ?")

try:
    print("Work! The third sequence is", from_morse(keyinput3))
except ValueError and TypeError:
    print("Not Morse Code.You should try again.")

keyinput1=input("The first sequence ?")

keyinput2=input("The second sequence ?")

keyinput3=input("The third sequence ?")
a=(from_morse(keyinput1))
b=(from_morse(keyinput2))
c=(from_morse(keyinput3))

#Use collections library
from collections import Counter


print("The analysis of the first sequence :")
print(Counter(a))
print("The analysis of the second sequence :")
print(Counter(b))
print("The analysis of the third sequence :" )
print(Counter(c))

#all the sequences
x=a+b+c
print("The analysis of all the sequences :")
print(Counter(x))
