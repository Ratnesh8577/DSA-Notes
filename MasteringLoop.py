
"""(!)str1="Ratnesh"
for i in str1:
    print(i)"""

#find even number
"""(2)List=[1,22,3,4,5,13,45,12,66,12]
for i in List:
    if i%2==0:
        print(i)"""


#(3) Appand in string
"""List=[1,22,3,4,5,13,45,12,66,12]
List2=[]
for i in List:
    if i%2==0:
        List2.append(i)
print(List2)
"""
"""#Factorial 
num=int(input("Enter the number"))
factorial=1
while num>0:
    factorial*=num
    num-=1
print(factorial)"""

"""#Factorial 
num=int(input("Enter the number"))
factorial=1
while num>0:
    if num==0 or num==1:
        print("1")
    else:
        factorial*=num
        num-=1
print(factorial)"""
#list=[2,4,6,22,6,7,8]
#output=[8,7,6,22,6,4,2]

list=[2,4,6,22,6,7,8]
low=0
high=len(list)-1
while low<high:
    #swap list[low] with the list[high]
    list[low],list[high]=list[high],list[low]
    #increment low value and drecrement the high value
    low+=1
    high-=1
print(list)
   

#write a code to check wheather the num is a prime number or not?

