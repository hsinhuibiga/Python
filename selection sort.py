def selection_sort(the_list):

    n=len(the_list)
    #print(n)
    for i in range(n-1):
        smallest = i
        #print(i)
        for j in range(i+1,n):
            #print(j)
            if the_list[j]<the_list[smallest]:
                smallest = j

        the_list[smallest],the_list[i]=the_list[i],the_list[smallest]



    return the_list

print(selection_sort(the_list=[2, 4, 5, 7, 3, 6, 9, 1]))
