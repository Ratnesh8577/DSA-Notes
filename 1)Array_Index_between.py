def reversed_array(n, arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
left = int(input("Enter left index: "))
right = int(input("Enter right index: "))

result = reversed_array(n, arr, left, right)
print("Reversed subarray:", result)


"""
output=

Enter number of elements: 6
Enter the elements: 1 2 3 4 5 6
Enter left index: 2
Enter right index: 5
Reversed subarray: [1, 2, 6, 5, 4, 3]
"""