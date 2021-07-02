#7_Program to cyclically rotate an array by one

"""
Given an array, cyclically rotate the array clockwise by one. 

Examples:  

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}

Solution:

1) Store last element in a variable say x. 
2) Shift all elements one position ahead. 
3) Replace first element of array with x.

"""
def display(n):
    for i in range(0,n):
        print(arr[i], end=",")

def rotate(arr,n):
    x = arr[n-1]

    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]

    arr[0] = x
        
arr = [1,2,3,4,5,6,7]
n = len(arr)

print("Before rotate :")
display(n)

rotate(arr,n)

print("\n\nAfter rotate :")
display(n)

