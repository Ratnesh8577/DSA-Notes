#Two pointer approach
#Reverse Array
def reverse(List):
    low ,high=0,len(List)-1
    while low<high:
        #swap the list[low],lost[high]
        List[low],List[high]=List[high],List[low]
        #increment the value of low
        low +=1
        #decrement the value of high
        high -=1
    return List  
#Driver code
List=[2,4,3,5,6,2,6,12,11,13,33]
#Function calling
print(reverse(List))



##(2)USe the append function
#Time complexity:-O(n)
#Space compexity:-O(n)
def reverse(arr):
    #Write your own code
    #ans as a list of n elements
    ans=[]
    for i in range(1,len(arr)+1):
        ans.append(arr[-i])
    return ans
#Driver code
arr=[2,3,4,6,7,9,1]
result=reverse(arr)
print("Reverse Array",result)




# (3)  Slicing Method

arr1=[2,3,4,6,7,9,1]
print(arr1[::-1])







