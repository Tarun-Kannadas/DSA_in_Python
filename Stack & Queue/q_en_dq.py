MAX = 6
intArray = [0] * MAX
front = 0
rear = -1
itemCount = 0

def isFull():
    return itemCount == MAX

def isEmpty():
    return itemCount == 0

def peek():
    return intArray[front]

def insert(data):
    global rear, itemCount
    if not isFull():
        rear = rear + 1
        intArray[rear] = data
        itemCount = itemCount + 1    
    else:
        print("\nQueue is full! Cannot insert the value:", data)

def removeData():
    global front, itemCount
    if not isEmpty():
        data = intArray[front]
        intArray[front] = 0
        front = front + 1
        itemCount = itemCount - 1
        print(f"Removed: {data}")
        return data
    else:
        print("\nQueue is empty! Cannot remove.")

insert(3)
insert(5)
insert(9)
insert(1)
insert(12)
insert(15)

print("\nPrinting the front Element: ",peek())

print("\nQueue:")
for i in range(front, rear + 1):
    print(intArray[i], end = " ")

print("\nUpdated Queue...", intArray)
while not isEmpty():
    removeData()

removeData()

print("\nQueue: ", intArray)

front = 0
rear = -1

insert(3)
insert(5)
insert(9)
insert(1)
insert(12)
insert(15)

print("\nQueue: ", intArray)