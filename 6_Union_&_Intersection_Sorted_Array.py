#6 Find the Union & Intersection of two sorted arrays

"""
Source : https://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/

Problem :

Given two sorted arrays, find their union and intersection.

Example:

Input : arr1[] = {1, 3, 4, 5, 7}
        arr2[] = {2, 3, 5, 6} 
Output : Union : {1, 2, 3, 4, 5, 6, 7} 
         Intersection : {3, 5}

Input : arr1[] = {2, 5, 6}
        arr2[] = {4, 6, 8, 10} 
Output : Union : {2, 4, 5, 6, 8, 10} 
         Intersection : {6}

"""
# Union O(m+n)
def union(arr1,arr2,m,n):
    i,j = 0,0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            print(arr2[j])
            j += 1
        else:
            print(arr2[j])
            j += 1
            i += 1
    # Print remaining element of large size array
    while i < m:
        print(arr1[i])
        i += 1

    while j < n:
        print(arr2[j])
        j += 1

# Intersection O(m+n)
def intersection(arr1,arr2,m,n):
    i,j = 0,0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
            
        elif arr2[j] < arr1[i]:
            j += 1
            
        else:
            print(arr2[j])
            j += 1
            i += 1

        
arr1 = [1,2,4,5,6]
m = len(arr1)

arr2 = [2,3,5,7]
n = len(arr2)

union(arr1,arr2,m,n)
intersection(arr1,arr2,m,n)
