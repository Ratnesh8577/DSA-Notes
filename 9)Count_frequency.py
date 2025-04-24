"""
l= [1,2,1,3,5,3,6,4,2,1,1]
n=len (l)
freq_map=dict()
for i in range(0,n):
    if l[i] in freq_map:
        freq_map[l[i]]+=1
    else:
        freq_map[l[i]]=1
print(freq_map)

"""
# 2nd Method 
l= [1,2,1,3,5,3,6,4,2,1,1]
hash_map=dict()
n = len(l)
for i in range(0,n):
    hash_map[l[i]]=hash_map.get(l[i],0)+1
print(hash_map)