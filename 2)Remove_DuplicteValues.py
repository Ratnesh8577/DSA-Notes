# REMOVE DUPLICATE VALUES IN ARRAY USING HASHMAP

def remove_duplicate(n,arr):
    dict = {}
    for i in range(0,n,1):
        dict[arr[i]] = 0
    for k in dict.keys():
        print(k)

# Driver code
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
result = remove_duplicate(n, arr)

# Print the result
print("Unique elements:", result)

# TC = O(N)
# SC = O(1)