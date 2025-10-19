MAXSIZE = 8
stack = [0] * MAXSIZE
top = -1;

def isempty():
    if(top == -1):
        return 1
    else:
        return 0
    
def isfull():
    if(top == MAXSIZE):
        return 1
    else:
        return 0
    
def peek():
    return stack[top]

def pop():
    global data, top
    if(isempty() != 1):
        data = stack[top];
        top = top - 1;
        return data
    else:
        print("Could not retrieve data, Stack is empty.")
    return data

def push(data):
    global top
    if(isfull() != 1):
        top = top + 1
        stack[top] = data
    else:
        print("Could not insert data, Stack is full.")
    return data

push(44)
push(10)
push(62)
push(123)
push(15)
print("Element at top of the stack: ", peek())
print("Elements: ")

while(isempty() != 1):
    data = pop();
    print(data, end = " ")
