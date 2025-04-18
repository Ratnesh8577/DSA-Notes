'''def sum_of_digit(n):
    sum = 0
    while n != 0:
        b = n% 10
        sum = sum + b
        n= n//10
    return sum
def palindrome(n):
    a = n
    sum = 0
    while n!= 0:
        b = n % 10
        sum = (sum * 10) + b
        n = n//10
    if sum == a:
        print("this is Palindrome")
    else:
        print("Not palindrome") 
def prime(n):
    if n<=1:
        return False
    i = 2
    while i <= (n//2):
        if n % i == 0:
            return False
        i +=1
    return True
def dist_sum_prime(n,arr):
    dict = {}
    for i in range(0,n,1):
        dict[arr[i]] = 0
    for i in range(0,n,1):
        dict[arr[i]] = dict[arr[i]] +1
    sum = 0
    for k,v in dict.items():
        if v>1:
            print(k)
            sum = sum + k*v
        return sum
# Driver code
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
total = dist_sum_prime(n, arr)
sum_of_digit = sum_of_digit(total)
if sum_of_digit % 2 == 0:
    print("Even_number",palindrome(sum_of_digit(total)))
else:
    print("Odd_number",prime(sum_of_digit))

        '''


def sum_of_digit(n):
    sum = 0
    while n != 0:
        b = n % 10
        sum = sum + b
        n = n // 10
    return sum

def palindrome(n):
    a = n
    rev = 0
    while n != 0:
        b = n % 10
        rev = (rev * 10) + b
        n = n // 10
    if rev == a:
        print("This is a Palindrome")
    else:
        print("Not a Palindrome") 

def prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= (n // 2):
        if n % i == 0:
            return False
        i += 1
    return True

def dist_sum_prime(n, arr):
    dict = {}
    for i in range(0, n):
        dict[arr[i]] = 0
    for i in range(0, n):
        dict[arr[i]] = dict[arr[i]] + 1
    sum = 0
    for k, v in dict.items():
        if v > 1:
            print("Repeated Element:", k)
            sum = sum + (k * v)
    return sum

# Driver code
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
total = dist_sum_prime(n, arr)
digit_sum = sum_of_digit(total)

if digit_sum % 2 == 0:
    print("Even Number")
    palindrome(digit_sum)
else:
    print("Odd Number")
    print("Is Prime:", prime(digit_sum))
