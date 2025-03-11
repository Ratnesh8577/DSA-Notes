#12345
i=1
while i<=10:
    print(i,end=" ")
    if i==5:
        break
    i+=1
else:
    print("you ar in alse")
#output:-12345

#12345
i=1
while i<=10:
    print(i,end=" ")
#10 tak hi chalega
    if i==12:
        break
    i+=1
else:
    print("you ar in alse")
 #output
 # :-   1 2 3 4 5 1 2 3 4 5 6 7 8 9 10 you ar in alse
'''
for i in range(10):
    print(i,end=" ")
    if i==12:
        break

else:
    ptint("You are in else")
'''



