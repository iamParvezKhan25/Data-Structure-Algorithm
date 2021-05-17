"""

Write a program to reverse an array or string.

Given an array (or string), the task is to reverse the array/string.
Examples : 
 

Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

"""

"""

Iterative way : Time Complexity : O(n)
 

    1) Initialize start and end indexes as
        start = 0, end = n-1 
    2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
        start = start +1, end = end – 1


Recursive Way : Time Complexity : O(n)
 

    1) Initialize start and end indexes as start = 0, end = n-1 
    2) Swap arr[start] with arr[end] 
    3) Recursively call reverse for rest of the array.

"""

#Iterative Function
def reverseListIteretive(array,start,end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

#Recursive Function
def reverseListRecersive(array,start,end):
    if start >= end:
        return
    array[start], array[end] = array[end], array[start]
    reverseListRecersive(array,start+1,end-1)

#Using Python List slicing
def reverseList(array):
    print(array[::-1])

array = [1,2,3,4,5]
print("Array List :",array)

n = len(array)- 1
print(n)


print("Iterative Function")
reverseListIteretive(array,0,n)
print("Array List :",array)

print("Recursive Function")
reverseListRecersive(array,0,n)
print("Array List :",array)

print("Using Python List slicing")
reverseList(array)
#print("Array List :",array)
