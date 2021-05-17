def binarySearch(itemList, item):
    first = 0
    last = len(itemList)-1

    found = False

    while(first <= last and not found):
        mid = (first+last)//2

        if itemList[mid] == item:
            found = True
            print ("Item Founded")
        else:

            if item < itemList[mid]:
                last = mid-1
            else:
                first = mid+1
    return found

itemList = [2,3,4,5,6,7,8,9]
print("Sorted Array List ",itemList)

item = 5
print("Found Value ",item)

result = binarySearch(itemList,item)
print(result)
