def ternarysearch(arr,left,right,key):
    while left<right:
        mid1=left+(right-left)//3
        mid2=right-(right-left)//3
        if key==arr[mid1]:
            return mid1
        elif key==arr[mid2]:
            return mid2
        elif arr[mid1]>key:
            return ternarysearch(arr,left,mid1-1,key)
        elif key>arr[mid2]:
            return ternarysearch(arr,mid2+1,key)
        else:
            return ternarysearch(arr,mid1+1,mid2-1,key)
        
        return -1

#Driver code
arr=[2,4,6,8,10,12]
key=4
result=ternarysearch(arr,0,len(arr)-1,key)
print(result)