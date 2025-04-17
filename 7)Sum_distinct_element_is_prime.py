#from import math sqrt
def prime(n):
    if n < 0:
        return 1
    i = 2
    #end = int(sqrt(n))
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
            sum = sum + k
    print(prime(sum))


# Driver code 

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
result = dist_sum_prime(n, arr)

# Print the result
print("Prime_Number:", result)

''' OUTPUT
Enter number of elements: 6
Enter the elements: 2 4 2 4 2 4
2
4
False
Prime_Number: None'''