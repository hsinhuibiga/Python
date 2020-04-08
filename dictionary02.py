#Creat a Morse Code dictionary
#task 1
dict = {"01": "A", "1000":"B", "1010":"C","100":"D","0":"E","0010":"F","110":"G","0000":"H","00":"I", "0111":"J","101":"K" \
        ,"0100":"L","11":"M","10":"N","111":"O","0110":"P","1101":"Q","010":"R","000":"S","1":"T","001":"U","0001":"V",
        "011":"W", "1001":"X","1011":"Y","1100":"Z","11111":"0","01111":"1","00111":"2","00011":"3","00001":"4","00000":"5" \
        ,"10000":"6","11000":"7","11100":"8","11110":"9"," ":" "}

print (dict)

#import dictionary
#task 2

input01= input("You should ask three Morse Code. Press enter to continue.")

keyinput1 = input("what is the first sequence?:")
if keyinput1 in dict:
   print("The first sequence is", "{value}".format(key=keyinput1, value=dict[keyinput1]))
else:
   while True:
       a = input("It's not the Morse Code.Enter yes/no to continue")
       if a == "yes":
           keyinput1()
           continue
       elif a == "no":
           break
       else:
           print("Enter either yes/no")

keyinput2= input("what is the second sequence:")
if keyinput2 in dict:

    print("The second sequence is", "{value}".format(key=keyinput2, value=dict[keyinput2]))
else:
    print("Please reput again.")
keyinput3= input("what is the third sequence:")
if keyinput3 in dict:

    print("The third squence is", "{value}".format(key=keyinput3, value=dict[keyinput3]))
else:
    print("Please reput again.")
#task 3

originalmessage = keyinput1+keyinput2+keyinput3

print("Original message:"+ originalmessage)
x=("{value}".format(key=keyinput1, value=dict[keyinput1]))
y=("{value}".format(key=keyinput2, value=dict[keyinput2]))
z=("{value}".format(key=keyinput3, value=dict[keyinput3]))

translatemessage =x+y+z
print("Translate message : "+ translatemessage)
#task 4
#part 1
for character in translatemessage:
    print(len(character))
#part 2

from itertools import chain

print(x.count)



