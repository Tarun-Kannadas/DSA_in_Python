def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        curr_data = arr[i]
        j = i-1

        while j>=0 and arr[j]>curr_data:
            arr[j+1] = arr[j]
            j=j-1

        arr[j+1] = curr_data

arr=[45,12,56,89,2]
print(arr)
insertion_sort(arr)
print(arr)