def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
 
arr=[2,4,6,8,9]
x=4
result=linearSearch(arr,x)
print(result)

#Insert the element
arr=[2,4,6,8,9]
arr.insert(1,5) #(1,2)==1 is index number and 5 is element insert
print(arr)
#output:-[2, 5, 4, 6, 8, 9]

