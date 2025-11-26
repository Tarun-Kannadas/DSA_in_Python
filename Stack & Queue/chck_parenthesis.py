open_list = ["(","{","["]
close_list = [")","}","]"]

def check(mystr):
    stack = []
    for ls in mystr:
        if ls in open_list:
            stack.append(ls)
        elif ls in close_list:
            length = len(stack)
            pos = close_list.index(ls)
            if (length>0 and open_list[pos] == stack[length-1]):
                stack.pop()
            else:
                return "unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
    
my_str1 = "{[]{()}}"
print(my_str1,"-", check(my_str1))
my_str2 = "{([])"
print(my_str2,"-",check(my_str2))