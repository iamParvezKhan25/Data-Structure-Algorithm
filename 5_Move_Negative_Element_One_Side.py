#5_Move all the negative elements to one side of the array

"""
Source : https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

Problem :

An array contains both positive and negative numbers in random order.
Rearrange the array elements so that all negative numbers appear
before all positive numbers.

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5

Two Pointer Approach:

The idea is to solve this problem with constant space and linear time is by using
a two-pointer or two-variable approach where we simply take two variables
like left and right which hold the 0 and N-1 indexes. Just need to check that :

    1. Check If the left and right pointer elements are negative then
       simply increment the left pointer.
       
    2. Otherwise, if the left element is positive and the right element is negative
        then simply swap the elements, and
        simultaneously increment and decrement the left and right pointers.
        
    3. Else if the left element is positive and the right element is also positive
        then simply decrement the right pointer.
        
    4. Repeat the above 3 steps until the left pointer ≤ right pointer.
    
"""
#Two ponter Approch

def shiftAll(arr, left, right):
    while left <= right:
        
        #if left & right negative
        if arr[left] < 0 and arr[right] < 0:
            left += 1
            
        #elif left is positive & right is negative
        elif arr[left] > 0 and arr[right] < 0:
            arr[left],arr[right] = arr[right],arr[left]

            left += 1
            right -= 1

        #elif left & right positive
        elif arr[left] > 0 and arr[right] > 0:
            right -= 1

        #else left is negative & right is positive
        else:
            left += 1
            right -= 1

def display(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

        
arr = [-12,11,-13,-5,6,-7,5,-3,11]
print("Before Sepration :")
display(arr)
n = len(arr)

#calling function
print("\nAfter Sepration :")
shiftAll(arr, 0, n-1)
display(arr)
