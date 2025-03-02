#function definition 
#Time complexity:-O(n^2)
#Space comlexity:-O(n^2)
def selectionsort(arr):
    n=len(arr)
    for i in range(n):
#to store the index of the miminum element
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<min_idx:
                min_idex=j
#swap of the element at i and min_idx
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr

#Driver code
arr=[50,38,75,29,11,17,20,37]
result=selectionsort(arr)
print("Selection sort of the given array element is",result)

#output:-Selection sort of the given array element is [50, 38, 75, 29, 11, 17, 20, 37]



