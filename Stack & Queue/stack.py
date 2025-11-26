maxsize = 5
stack = [0]*maxsize
top = -1

def isEmpty():
    if top == -1:
        return 1
    else:
        return 0
    
def peek():
    return stack[top]
    
def isFull():
    if top == maxsize-1:
        return 1
    else:
        return 0

def push(data):
    global top
    if(isFull() == 0):
        top = top + 1
        stack[top] = data
    else:
        print(f"\nStack is Full! Can't Insert the value '{data}'")

def pop():
    global top
    if(isEmpty() == 0):
        data = stack[top]
        stack[top] = 0
        top = top - 1
        print("\nElement Popped: ", data)
    else:
        print("\nStack is Empty!")

push(25)
push(56)
push(32)
push(5)
push(18)
push(15)

n=len(stack)

for i in range(n):
    print(stack[i], end = " ")

print("\nStack's Top elements is: ", peek())

while (isEmpty() == 0):
    pop()

print("\nStack after popping elements: ")
for i in range(n):
    print(stack[i], end = " ")