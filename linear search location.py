
"""
def linearSearch(intList,target):
    #print (target)
    found = False
    position = -1
    while position < len(intList):
        #print(intList[position])
        if intList[position] == target:



           position = position + 1

        return position

linearList = [3,5,9,7,6,12,15,9,1]
numInput = int(input("What number are you looking for? "))
numFound = linearSearch(linearList,numInput)
if numFound:
    print("The number is in index: ")
else:
    print("The number is not in the list")
"""
"""
list = [4,1,2,5,3]  #set up array
search = int(input("Enter search number"))    # ask for a number
for i in range(0,len(list)): # repeat for each item in list
  if search==list[i]: #if item at position i is search time
    print(str(search) + " found at position " + str(i)) #report find
"""


def linear_search(the_list, target_item):



    n=len(the_list)
    for i in range(n):
        #print (i)
        #if the_list[i]==target_item:
        if target_item==the_list[i]:
            print ("the index is" +" "+str(i))
    #return
    #return i


linear_search(['c', 'e', 'a', 'f', 'b', 'h'],'e')

#print((' found at position ' + (i))

    #return False

#linear_search(['c','e','a','f','b','h'],'d')
