#Write a function to segrate even odd number
def segre(arr):
    ans=[]
    for i in range(len(arr)):
        if arr[i]%2==0:
            ans.append(arr[i])
    for i in range(len(arr)):
        if arr[i]%2 !=0:
            ans.append(arr[i])
    return ans

#Driver code
arr=[7,5,3,8,4,2,12,9,10,22]
result=segre(arr)
print(result)



#Time comp:-O(1),Space comp:-O(1)
def  segre(arr):
    i=-1
    j=0
    n=len(arr)
    while j!=n:
        if (arr[j]%2==0):
            i=j+1
            arr[i],arr[j]=arr[j],arr[i]
        j=j+1
    return arr

arr=[7,5,3,8,4,2,12,9,10,22]
result=segre(arr)
print(result)

#output=[8,4,2,12,10,22,7,5,9]

