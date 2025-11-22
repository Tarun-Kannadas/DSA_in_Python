def shell_sort(arr,size):
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j=j-gap
            arr[j] = temp
        gap = gap // 2

arr=[25,15,42,7,56,5]
n = len(arr)
print("Array before Sorting: ", arr)
shell_sort(arr,n)
print("Array after Sorting: ", arr)