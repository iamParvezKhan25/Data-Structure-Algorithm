#8_Minimise the maximum difference between heights [V.IMP]

"""

Given heights of n towers and a value k. We need to either increase or decrease the height of every tower by k (only once) where k > 0. The task is to minimize the difference between the heights of the longest and the shortest tower after modifications and output this difference.
Examples: 

Input  : arr[] = {1, 15, 10}, k = 6
Output :  Maximum difference is 5.
Explanation : We change 1 to 7, 15 to 
9 and 10 to 4. Maximum difference is 5
(between 4 and 9). We can't get a lower
difference.

Input : arr[] = {1, 5, 15, 10} 
        k = 3   
Output : Maximum difference is 8
arr[] = {4, 8, 12, 7}

Input : arr[] = {4, 6} 
        k = 10
Output : Maximum difference is 2
arr[] = {14, 16} OR {-6, -4}

Input : arr[] = {6, 10} 
        k = 3
Output : Maximum difference is 2
arr[] = {9, 7} 

Input : arr[] = {1, 10, 14, 14, 14, 15}
        k = 6 
Output: Maximum difference is 5
arr[] = {7, 4, 8, 8, 8, 9} 

Input : arr[] = {1, 2, 3}
        k = 2 
Output: Maximum difference is 2
arr[] = {3, 4, 5}

"""


"""
Explaination :

First we try to sort the array and make each height of the tower maximum .
We do this by decreasing the height of all the towers
towards right by k and increasing all the height of the towers towards left (by k).
It is also possible that the tower you are trying to increase the height doesn’t have the maximum height .
Therefore we only need to check whether it has the maximum height or not
by comparing it with the last element towards the right side which is an-k.
Since the array is sorted if the tower’s height is greater than the an-k then it’s the tallest tower available.
Similar reasoning can also be applied for finding the shortest tower .  

Note:- We need not consider where a[i]<k because the height of the tower can’t be negative so we have to neglect that case.

"""
def getMinDiff(arr, n, k):
    arr.sort() #sorting the array
    print(arr)
    ans=arr[n-1]-arr[0] #it's same as substracting an+k-(ao+k) or an-k-(a0-k)
    print("ans :",ans,"=","arr[n-1]",arr[n-1],"arr[0]",arr[0])
    small,big=0,0
    print("small:",small)
    print("big:",big)

    for i in range(1,n):#trying to make each tower highest
        print(i)
        small=min(arr[0]+k,arr[i]-k) #finding minimum tower height
        print("small",small,"=","arr[0]",arr[0],"+","k",k,",","arr[i]",arr[i],"-","k",k)
        big=max(arr[i-1]+k,arr[-1]-k) #finding maximum tower height
        print("big",big,"=","arr[i-1]",arr[i-1],"+","k",k,",","arr[-1]",arr[-1],"-","k",k)
        ans=min(ans,big-small) #checking whether we get smaller value as result
        print("ans",ans,"=","ans",ans,"big",big,"-","small",small)

        return ans


arr=[1, 10, 14, 14, 14, 15]
print(arr)
k=6
print("k:",k)
print(getMinDiff(arr,len(arr),k))
