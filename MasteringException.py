'''try:
    a=int(input("Enter the value a : "))
    b=int(input("Enter the value b : "))
    c=a/b
    print(c)
except:
    pass
print("hello Ratnesh chauhan")'''


'''try:
    a=int(input("Enter the value a : "))
    b=int(input("Enter the value b : "))
    c=a/b
    print(c)
except Exception as e:
    print(e)
print("hello Ratnesh chauhan")
'''
#output
'''Enter the value a : 6
Enter the value b : 0
division by zero
hello Ratnesh chauhan'''

'''try:
    l=[10,20,30,50,70,90]
    l[10]
except Exception as e:
    print(e)


#output--list index out of range'''


'''try:
    a=int(input("Enter the value a : "))
    b=int(input("Enter the value b : "))
    c=a/b
    print(c)
except Exception as e:
    print(e)
else:
    print("It will excute only your block will excute successfully")

   #Enter the value a : 4
Enter the value b : 3
1.3333333333333333
It will excute only your block will excute successfully''' '''
'''

#(4)
'''try:
    a=int(input("Enter the value a : "))
    b=int(input("Enter the value b : "))
    c=a/b
    print(c)
except Exception as e:
    print(e)
else:
    print("It will excute only your block will excute successfully")

finally:
    print("This block is excute always")'''




#*******Attached file**********
'''try:
    file_Path="C:\Users\pr249\OneDrive\Desktop\Pictures"
    f=open(file_Path)
    f.read()
except Exception as e:
    print(e)

else:
    print("EDA stur") '''

'''
try:
    file_path = "C:\Users\pr249\OneDrive\Desktop\Pictures\example.txt"  # Use a full file path to a specific file
    with open(file_path, 'r') as f:  # Use 'with' to ensure proper file handling
        content = f.read()
        print(content)
except Exception as e:
    print(f"Error: {e}")
'''