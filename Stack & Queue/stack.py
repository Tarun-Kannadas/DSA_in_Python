maxsize = 5
stack = [0]*maxsize
top = -1

def isEmpty():
    if (top == -1):
        return 1
    else:
        return 0

def isFull():
    if (top == maxsize-1):
        return 1
    else:
        return 0

def peek():
    return stack[top]

def push(data):
    global top
    if(isFull() == 0):
        top = top + 1
        stack[top] = data
    else:
        print("Cannot enter element, Stack is full!")
    return data

def pop():
    global data,top
    if(isEmpty() == 0):
        data = stack[top]
        top = top - 1
        return data
    else:
        print("Stack is Empty")
    return data

push(44)
push(59)
push(123)
push(31)
push(90)

print("My Stack is:", stack)

print("\nElement at the top of stack: ", peek())

print("\nPopping Elements...")

while (isEmpty() == 0):
    data = pop()
    print("Popping Elements:",data,end=" \n") 