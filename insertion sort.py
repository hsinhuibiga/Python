



# sorts the list in an ascending order using insertion sort
def insertion_sort(the_list):
    # obtain the length of the list
    n = len(the_list)

    # begin with the first item of the list
    # treat it as the only item in the sorted sublist
    for i in range(1, n):
        # indicate the current item to be positioned
        #print(i)
        current_item = the_list[i]
        #print(current_item)
        # find the correct position where the current item
        # should be placed in the sorted sublist
        pos = i
        #print(the_list[pos])
        while pos > 0 and the_list[pos - 1] > current_item:
            # shift items in the sorted sublist that are
            # larger than the current item to the right
            the_list[pos] = the_list[pos - 1]
            pos -= 1
            print(the_list[pos])
        # place the current item at its correct position
        the_list[pos] = current_item
    return the_list
the_list = [54,26,93,17,77,31,44,55,20]
#the_list = [77,31,55,20]
print(insertion_sort(the_list))


"""
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
"""