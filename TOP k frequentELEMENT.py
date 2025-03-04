#TOP K FREQUENT ELEMENT
#USE of heapq
from collections import Counter
import heapq
#function definition
def topfrequentelement(arr,k):
    if k==len(arr):
        return set(arr)
    count=Counter(arr)
#Count is dictionary which contain unique values as the frequency of those unique element as the value 
    #print(count)
    return heapq.nlargest(k,count.keys(),key=count.get)
#Driver code
arr=[1,1,1,1,2,2,3]
k=2
result = topfrequentelement(arr,k)
print("The topfrequentelement are",result)


