'''string="Ratneshchauhan"
print(string[::-1])
print(string[:-1])
'''


'''
n=input("Enter the number")
while (n>0):
    b=n%10
    n=n//10
    print(b, end=" ")'''
#definition function
def reversearr(arr,left,right):
    left,right=0,len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

#Driver code
arr=[2,4,6,7,8,9,12]
result=reversearr(arr,0,len(arr))
print(result)

