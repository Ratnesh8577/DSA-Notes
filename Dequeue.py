from collection import dequeue

lst = dequeue([])
lst.append(100)
lst.append(12)
lst.append(22)
lst.append(44)
lst.append(55)
lst.appendleft(1)
lst.appendright(8)
print(lst)
lst.popleft()
print(lst)