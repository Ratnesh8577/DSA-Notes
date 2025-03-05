#Write aPython Program to find largest element in an array
#function definition
def largestarray(arr):
    if not arr:
        return "Array is empty"
    largestarray = arr[0]
    for i in arr:
        if i > largestarray:
            largestarray = i
    return largestarray

#Driver code
arr=[1,4,55,3,7,4,23,45]
result=largestarray(arr)
print("Largest Array is: ",result)