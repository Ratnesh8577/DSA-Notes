def is_palindrome(n, arr):
    left = 0
    right = n - 1
    while left <= right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
result = is_palindrome(n, arr)
print("Is palindrome:", result)
