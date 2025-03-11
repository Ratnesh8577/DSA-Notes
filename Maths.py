#(1) Sum of 1+2+3+4+5-------
"""Sum=0
n=int(input("Enter the value: "))
diff=int(input("Enter the value: "))
for i in range(1,n+1):
    Sum=Sum+diff
    print(Sum,"+",end=" ")"""


#(2)10+9+8+7------+2+1
'''n=int(input("Enter the value: "))
for i in range(n,0,-1):
    print(i,"+",end=" ")'''

#Output=Enter the value: 11
#11 + 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 



#(3) 
"""
n = int(input("Enter the value: "))  # Input the number of terms
x = int(input("Enter the base number: "))  # Input the base number as an integer
a = 1
total_sum = 0

for i in range(1, n + 1):
    total_sum += pow(x, a)  # Calculate x^a and add it to total_sum
    a += 1  # Increment the exponent
    print(total_sum)
#print("The total sum is:", total_sum)"""
'''
n = int(input("Enter the value: "))  # Number of terms
x = input("Enter the string: ")  # Input string
a = 1
total_sum = 0

for i in range(1, n + 1):
    total_sum += pow(len(x), a)  # Use the length of the string for calculations
    a += 1  # Increment the exponent

    print( total_sum,end=" ")
'''

'''
x=int(input("Enter the value: "))
n=int(input("Enter the value: "))

for i in range(1,n+1):
    print(f"x^{i} + ",end=" ")
    
    ''''''  output  Enter the value: 2
Enter the value: 5
x^1 +  x^2 +  x^3 +  x^4 +  x^5 +  
'''

'''a=2
sum=0
n=int(input("Enter the value: "))
for i in range(2,n,2):
    sum+=a
    a+=2
    print(f"{i}^x +",end=" ")

#print()
output
Enter the value: 10
2^x + 4^x + 6^x + 8^x + 
'''

#(4)

"""sum=0
a=1
n=int(input("Enter the value: "))
for i in range(1,n,2):
    sum+=a
    a+=2
    print(f"{i}^3/x +",end=" ")

Output=
Enter the value: 22
1^3/x + 3^3/x + 5^3/x + 7^3/x + 9^3/x + 11^3/x + 13^3/x + 15^3/x + 17^3/x + 19^3/x + 21^3/x + 

"""
"""sum=0
a=2
n=int(input("Enter the value: "))
for i in range(2,n):
    sum=a
    a*=2
    print(sum,"+",end=" ")

output
Enter the value: 12
2 + 4 + 8 + 16 + 32 + 64 + 128 + 256 + 512 + 1024 + 


"""
"""
sum=0
a=10
n=int(input("Enter the value: "))
for i in range(1,n+1):
    sum=a
    a*=3
    print(sum,"+",end=" ")

output
Enter the value: 5
10 + 30 + 90 + 270 + 810 + 


"""




#(6)

a=1
n=int(input("Enter the value: "))
for i in range(2,n):
    a*=2
    
    
    print(f"x/{a} +",end=" ")



