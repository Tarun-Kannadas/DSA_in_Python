def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

n = int(input("Enter how many numbers needed: "))
arr = []
for i in range(n):
    val = int(input(f"Enter the value {i+1}: "))
    arr.append(val)

# arr = [45,56,12,23,5]
print(arr)
bubble_sort(arr)
print(arr)