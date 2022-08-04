arr1 = [1,2,3,4,5]
mn = arr1[0]
for i in range(1, len(arr1)):
    mn = min(mn, arr1[i])
print(mn)

mx = arr1[0]
for i in range(1, len(arr1)):
    mx = max(mx, arr1[i])
print(mx)

arr2 = [1,2,3,3,4,4,5,5]
arr2 = list(set(arr2))
arr2.sort()
print(arr2[-2])

arr2 = [1,2,2,3,3]
mx = max(arr2)
mx2 = min(arr2)
for i in arr2:
    if i > mx2 and i!=mx:
        mx2 = i
print(mx2)

# MaX Salary
class Emp:
    sal = 0
    def __init__(self, sal):
        self.sal = sal

emp = []
emp.append(Emp(100))
emp.append(Emp(200))
emp.append(Emp(300))
emp.append(Emp(400))
mx = -1
for e in emp:
    mx = max(e.sal, mx)
print(mx)

# linkedList
class Node:
    # data = 0
    # next = None
    def __init__(self, data):
        self.data = data
        self.next = None
head = None

for i in range(6):
    newNode = Node(i)
    if head == None:
        head = newNode
        ll = newNode
    else:
        ll.next = newNode
        ll = ll.next
slow = head
fast = head
while(fast!= None and fast.next!= None):
    slow = slow.next
    fast = fast.next.next
print(slow.data)    

# even lenght list
arr3 = [900, 232, 1111, 42442, 142142, 5252, 24242]
evenList = []
for i in arr3:
    if len(str(i)) % 2 == 0:
        evenList.append(i)
print(evenList)

#Count Number of duplicates
arr4 = [1,1,2,3,2,4,5,6,7]
hashmap = {}
for i in arr4:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1
print(hashmap)

data ={
    "Name" : ['A', 'B', 'C'],
    "Age" : [10, 20, 30],
    "Sal" : [5, 5, 5]
}
import pandas as pd
data1 = pd.DataFrame(data)
print(data1)

# quick sort
arr4 = [9,8,7,6,5,4]
def partition(low, high):
    i = low
    pivot = arr4[high]
    for j in range(low, high):
        if arr4[j] <= pivot:
            arr4[j], arr4[i] = arr4[i], arr4[j]
            i += 1
    arr4[high], arr4[i] = arr4[i], arr4[high]
    return i

def quick(low, high):
    if low <= high:
        p = partition(low, high)
        quick(low, p - 1)
        quick(p + 1, high)

quick(0,len(arr4) - 1)
print(arr4)

# Bubble Sort
arr5 = [5,4,3,2,1]
for i in range(0, 4):
    for j in range(0, 5-i-1):
        if arr5[j] > arr5[j+1]:
            arr5[j], arr5[j+1] = arr5[j+1], arr5[j]
print(arr5)


# Insertion Sort
for i in range(1, len(arr5)):
    key = arr5[i]
    j = i - 1
    while j>=0 and key > arr5[j]:
        arr5[j], arr5[j+1] = arr5[j+1], arr5[j]
        j -=1
    arr5[j+1] = key
print(arr5)

# Selection sort

for i in range(len(arr5)):
    mn = i
    for j in range(i + 1, len(arr5)):
        if arr5[mn] > arr5[j]:
            mn = j
    arr5[i], arr5[mn] = arr5[mn], arr5[i]

print(arr5)

# Prime
prime = []
for i in range(2, 101):
    if i%2 == 0 and i != 2:
        continue
    num = 2
    flag = 0
    while num < i/2:
        if i % num == 0:
            flag = 1
            break
        num+=1
    if flag == 1:
        continue
    prime.append(i)
print(prime)