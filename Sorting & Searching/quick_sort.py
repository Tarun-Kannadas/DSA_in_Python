def quick_sort(arr):
    n=len(arr)
    if (n <=1 ):
        return arr
    
    pivot = arr[n//2]
    left=[]
    middle=[]
    right=[]

    # compare values, not indexes
    for value in arr:
        if value < pivot:
            left.append(value)
        elif value == pivot:
            middle.append(value)
        else:
            right.append(value)

    # recursively sort left and right
    return quick_sort(left) + middle + quick_sort(right)

arr = [12,45,56,5,9]
n = len(arr)
print("Original Array: ", arr)
sorted_arr = quick_sort(arr)
print("Sorted Array: ", sorted_arr)