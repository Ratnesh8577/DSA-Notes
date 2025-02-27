# Function definition
def maximumSubarraySum(n, arr):
    # Handle the case where all numbers are negative
    if all(i < 0 for i in arr):
        return max(arr)
    sum = 0
    maximum = float('-inf')  # Initialize to negative infinity for proper comparison
    
    # Traverse the array to find the maximum subarray sum
    for i in range(n):
        sum += arr[i] 
        if sum < 0:
            sum = 0  # Reset sum if it becomes negative
        elif sum > maximum:
            maximum = sum  # Update maximum if the current sum is larger
    return maximum

# Driver code
# Input
n = int(input("Enter the size of the array: "))  # Read the size of the array
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))  # Read the array elements

# Call the function
x = maximumSubarraySum(n, arr)

# Output the result
print(f"Maximum Subarray Sum: {x}")
