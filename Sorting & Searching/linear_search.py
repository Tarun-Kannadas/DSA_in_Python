def selection_sort(arr,size):
    for i in range(size-1):
        first_val = i
        for j in range(i+1,size):
            if arr[j]<arr[first_val]:
                first_val = j
        temp = arr[i]
        arr[i] = arr[first_val]
        arr[first_val] = temp

def linear_search(key,size):
    for i in range(size):
        if arr[i] == key:
            print(f"Element {arr[i]} is found at the position {i} in the array")
            return
    print(f"Element {key} not found")

arr = [12,45,23,56,5]
n = len(arr)
print("Array before Sorting: ", arr)
selection_sort(arr,n)
print("Array after Sorting: ", arr)
linear_search(23,n)
linear_search(7,n)