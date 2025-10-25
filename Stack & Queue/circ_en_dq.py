size = 3
queue = [None] * size
front = -1
rear = -1

def enqueue(item):
    global front, rear

    if (rear + 1) % size == front:
        print("Queue is full! Cannot enqueue.")
        return
    
    if front == -1:
        front = 0
    
    rear = (rear + 1) % size
    queue[rear] = item
    print(f"Enqueued: {item}")

def dequeue():
    global front, rear
    if front == -1:
        print("Queue is empty! Cannot dequeue.")
        return
    
    item = queue[front]

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size
    
    print(f"Dequeued: {item}")

def display():
    if front == -1:
        print("Queue is empty!")
        return
    
    print("Circular Queue:", end=" ")
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
display()

dequeue()
enqueue(40)
display()
