#2_ Find max and min Element in Array

#LargestElement
def largestElement(arr,size):

    maxElement = arr[0]

    for i in range(size):
        if arr[i] > maxElement:
            maxElement = arr[i]

    print("Largest Element In Array List : {}".format(maxElement))

#SmallestElement
def smallestElement(arr,size):

    minElement = arr[0]

    for i in range(size):
        if arr[i] < minElement:
            minElement = arr[i]

    print("Smallest Element In Array List : {}".format(minElement))

#SecondLargest / 2nd Largest Elemet
def secondLargestElement(arr,size):

    if size < 2:
        print("Array-List size should be GT 2")
        return
    
    larger = -99999
    secLarger = -99999

    for i in range(size):
        if arr[i] > larger:
            secLarger = larger
            larger = arr[i]

        elif arr[i] > secLarger and arr[i] != larger:
            secLarger = arr[i]

    if secLarger == -99999:
        print("Second Largest Element Not Found!")
    else:
        print("Second Largest Element : {}".format(secLarger))

#SecondSmallest / 2nd Smallest Element
def secondSmallestElement(arr,size):

    if size < 2:
        print ("Array-List size should be GT 2")
        return

    smaller = 99999
    secSmaller = 99999

    for i in range(size):
        if arr[i] < smaller:
            secSmaller = smaller
            smaller = arr[i]

        elif arr[i] < secSmaller and arr[i] != smaller:
            secSmaller = arr[i]

    if secSmaller == 99999:
        print("Second Smallest Element Not Foind")
    else:
        print("Second Smallest Element : {}".format(secSmaller))
        
#Main Function & Function Calling 
arr = [25,11,95,15,12,96,15,8,96,1,2,3,4,5,6]
print("Array - List : {}".format(arr))

size = len(arr)

largestElement(arr,size)
smallestElement(arr,size)
secondLargestElement(arr,size)
secondSmallestElement(arr,size)
