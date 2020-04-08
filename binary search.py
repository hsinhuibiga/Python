
"""
def binary_search(the_list,target_item):
    low=0
    high=len(the_list)-1
    while low<=high:
        mid=(low+high)//2
        if the_list[mid]==target_item:
            return True
        elif target_item<the_list[mid]:
            high=mid-1
        else:
            low=mid+1
    return False

print(binary_search(['c','e','a','f','b','h'],'e'))

"""
def binary_search(the_list,target_item):
    low=0
    high=len(the_list)-1
    while low<=high:
        mid=(low+high)//2
        if target_item==the_list[mid]:
            print("index"+str(mid))
            break
        elif target_item<the_list[mid]:
            high=mid-1
        else:
            low=mid+1
    return False

binary_search(['c','e','a','f','b','h'],'b')