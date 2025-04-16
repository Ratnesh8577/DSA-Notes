def dist_element(n,arr):
    dict = {}
    for i in range(0,n,1):
        dict[arr[i]] = 0
    for i in range(0,n,1):
        dict[arr[i]] = dict[arr[i]] +1
    for k,v in dict.items():
        if v>1:
         
         print(k)
# Driver code
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
result = dist_element(n, arr)

# Print the result
print("Dist_elements:", result)


# 2nd Method 
def dist_element(n, arr):
    dict = {}
    for i in range(0, n, 1):
        dict[arr[i]] = 0
    for i in range(0, n, 1):
        dict[arr[i]] = dict[arr[i]] + 1

    # Get only the elements that appear exactly once
    result = []
    for k, v in dict.items():
        if v > 1:
            result.append(k)
    return result

# Driver code
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
result = dist_element(n, arr)

# Print the result
print("One-time elements:", result)