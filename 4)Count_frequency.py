# COUNT FREQURNCY OF EACH ELEMENT IN AN ARRAY

def count_freq(n,arr):
    dict = {}
    for i in range(0,n,1):
        dict[arr[i]] = 0
    for i in range(0,n,1):
        dict[arr[i]] = dict[arr[i]] + 1
    for k ,v in dict.items():
        print(k,"occured",v,"items")

# Driver code
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
result = count_freq(n,arr)

# Print the result
print("Unique elements:", result)