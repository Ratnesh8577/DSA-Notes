def binarysearch(arr,i,j,x):
    #check Base case
    #arr,i=starting index,j=last index
    if j>=i:
        #mid term find
        mid=i+(j-i)//2
        #if mid==key(x) ,key is mid
        if x==arr[mid]:
            return mid
        elif arr[mid]>x:
            #if key<mid so last index(j) is mid-1
            return binarysearch(arr,i,mid-1,x)
        else:
            #if key(x)>mid so starting index is mid+1
            return binarysearch(arr,mid+1,j,x)
    else:
        return -1
    
#driver code
arr=[20,30,45,50,70,98]
key=70
#function call
result=binarysearch(arr,0,len(arr)-1,key)
print(result)