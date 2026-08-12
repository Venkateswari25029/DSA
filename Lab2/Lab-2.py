#Linear search

n=int(input("Enter no.of elements:"))
arr=[]
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
key=int(input("enter the number:"))
def linear_search(arr,key):
    for i in range(0,len(arr)):
        if arr[i]==key:
            print(" Element found at Index:",i)
            return
    print("Not found")
linear_search(arr,key)
 
 
#binary search unsorted
 
n=int(input("Enter the no.of elements:"))
arr=[]
print("Enter the element:")
for i in range(n):
    arr.append(int(input()))
print("sorted:",arr)
key=int(input("Enter the target:"))
if arr==sorted(arr):
    print("It is sorted")
else:
    print("array is not sorted")
    arr.sort()
    print("sorted array:",arr)
def binary_search(arr,key):
    low=0
    
