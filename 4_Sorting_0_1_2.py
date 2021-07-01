#4_Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

"""
Source : https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

Problem :

Given an array A[] consisting 0s, 1s and 2s.
The task is to write a function that sorts the given array.
The functions should put all 0s first, then all 1s and all 2s in last.

Example :

Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

Approch :

The problem was posed with three colours, here `0′, `1′ and `2′.
The array is divided into four sections: 

    1. a[1..Lo-1] zeroes (red)
    2. a[Lo..Mid-1] ones (white)
    3. a[Mid..Hi] unknown
    4. a[Hi+1..N] twos (blue)
    5. If the ith element is 0 then swap the element to the low range,
       thus shrinking the unknown range.
    6. Similarly, if the element is 1 then keep it as it is but
       shrink the unknown range.
    7. If the element is 2 then swap it with an element in high range.
"""
def sort012(arr, n):
    low = 0
    mid = 0
    high = n-1

    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]

            low += 1
            mid += 1
            
        elif arr[mid] == 1:
            mid += 1

        else:
            arr[mid],arr[high] = arr[high],arr[mid]

            high -= 1
            
    return arr

def printArray(arr):
    for i in arr:
        print(i, end=" ")

arr = [0,1,1,0,1,2,1,2,0,0,0,1]
print("Array Before Segrigation:\n")
printArray(arr)

n = len(arr)

solArr = sort012(arr,n)
print("\nArray After Segregation :\n")
printArray(solArr)
