
#define function 
def linearSearch(arr,n,item):
    for i in range(n):
        if item==arr[i]:
            return True
    return False

#Driver code 
arr = [10,20,30,40,50,60,70,80,90,100]
item=int(input("Enter an element to  search: "))
result=linearSearch(arr,len(arr),item)
print(result)




arr = [2, 4, 6, 8, 9]
del arr[1:5]  # Removes elements from index 1 to 4 (element is 4,6,8,9) all delete
print(arr)
#output:-[2]

arr=[2,4,6,8,9]
arr.remove(2) #Element 2 delete
print(arr)
#output:-[4, 6, 8, 9]