def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        first_val = i
        for j in range(i+1,n):
            if arr[j]<arr[first_val]:
                first_val = j
        temp = arr[i]
        arr[i] = arr[first_val]
        arr[first_val] = temp


n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    val = int(input(f"Entered element {i+1}: "))
    arr.append(val)

# data = len(arr)
# for i in range(data):
#     print(arr[i], end=" ")
print(arr)
selection_sort(arr)
print(arr)
# for i in range(data):
#     print(arr[i], end=" ")