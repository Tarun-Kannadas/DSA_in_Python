MAX = 6
intArray = [0] * MAX
front = 0
rear = -1
itemCount = 0

def isFull():
    return itemCount == MAX

def isEmpty():
    return itemCount == 0

def insert(data):
    global rear, itemCount
    if not isFull():
        rear = rear + 1
        intArray[rear] = data
        itemCount += 1
    else:
        print("Queue is full! Cannot insert.")

def removeData():
    global front, itemCount
    if not isEmpty():
        data = intArray[front]
        front += 1
        itemCount -= 1
        return data
    else:
        print("Queue is empty! Cannot remove.")
        return None

insert(3)
insert(5)
insert(9)
insert(1)
insert(12)
insert(15)

print("Queue:")
for i in range(front, rear + 1):
    print(intArray[i], end = " ")

print("\n\nDeleting elements...")
while not isEmpty():
    n = removeData()
    print("Got Removed",n,"")