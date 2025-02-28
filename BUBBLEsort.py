#Method definition
#Space complexity:-O(n)
#Time complexity:-O(n^2)
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
#first index comparion  to second index
            if arr[j]>arr[j+1]:
#swap of th elements
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


#Driver code
arr=[70,20,50,30,90,5,15]
result=bubblesort(arr)
print("Array after applying bubble sort",result)

#output Array after applying bubble sort [5, 15, 20, 30, 50, 70, 90]