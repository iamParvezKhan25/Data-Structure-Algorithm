#3_Find the "Kth" max and min element of an array

"""
Source : https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

Problem :

Given an array and a number k where k is smaller than the size of the array,
we need to find the k’th smallest element in the given array.
It is given that all array elements are distinct.

example:

Input: arr[] = {7, 10, 4, 3, 20, 15} 
k = 3 
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15} 
k = 4 
Output: 10

"""

# Simple solution
def kthSmallest(arr,n,k):
    arr.sort()
    return arr[k-1]

def kthLargest(arr,n,k):
    arr.sort()
    return arr[-k]

arr = [7,10,4,20,15]
n = len(arr)

k = 2

print("K'th Smallest element is :", kthSmallest(arr,n,k))
print("K'th Largest element is :", kthLargest(arr,n,k))
