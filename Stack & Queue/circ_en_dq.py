size = 5
queue = [0] * size
front = -1
rear = -1

def enqueue(item):
    global front, rear

    if (rear + 1) % size == front:
        print("\nQueue is full! Cannot enqueue the value: ",item)
        return
    
    if front == -1:
        front = 0
    
    rear = (rear + 1) % size
    queue[rear] = item
    print(f"\nEnqueued: {item}")

def dequeue():
    global front, rear
    if front == -1:
        print("\nQueue is empty! Cannot dequeue.")
        return
    
    item = queue[front]
    queue[front] = 0

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size
    
    print(f"\nDequeued: {item}")

def display():
    if front == -1:
        print("Queue is empty!")
        return
    
    print("\nfront operation: ",queue[front])
    print("rear operation: ",queue[rear])
    
    print("\nCircular Queue:", end=" ")
    i = front
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % size
    print()

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(12)
enqueue(45)
enqueue(56)
display()

dequeue()
enqueue(40)
display()
