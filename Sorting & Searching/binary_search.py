def binary_search(a, low, high, key):
    mid = (low+high) // 2
    if (low<=high):
        if (a[mid] == key):
            print("The number's index is at ",mid+1)
        elif(key<a[mid]):
            binary_search(a,low,mid-1,key)
        elif(key>a[mid]):
            binary_search(a,mid+1,high,key)
    if(low>high):
        print("Unsuccessful Search")

a = [7,10,12,18,22,34,45]
n =len(a)
low = 0
high = n-1
key = 34
binary_search(a,low,high,key)
key = 10
binary_search(a,low,high,key)
key = 8
binary_search(a,low,high,key)