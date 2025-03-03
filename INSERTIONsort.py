#funcion definition
def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr    

#Driver code
arr=[50,38,75,29,11,17,20,37]
result=insertionsort(arr)
print("insertion sort of the given array element is",result)


#Output:-insertion sort of the given array element is [11, 17, 20, 29, 37, 38, 50, 75]