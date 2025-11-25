def heapify(heap,n,i):
    maximum = i
    l = i*2 + 1
    r = i*2 + 2
    # Checks for left child
    if (l<n and heap[i]<heap[l]):
        maximum = l
    # Check for right child
    if (r<n and heap[maximum]<heap[r]):
        maximum = r
    # For Root Node
    if (maximum != i):
        temp = heap[i]
        heap[i] = heap[maximum]
        heap[maximum] = temp
        heapify(heap,maximum,n)

def heapSort(heap):
    n = len(heap)
    # Maxheap
    for i in range(n,-1,-1):
        heapify(heap, n, i)
    # Swaps the element found in the name of element extraction
    for i in range(n-1,0,-1):
        temp = heap[i]
        heap[i] = heap[0]
        heap[0] = temp
        heapify(heap, i, 0)

heap = [4,3,1,0,2]
n = len(heap)

print("Array before Sorting: ")

for i in range(n):
    print(heap[i], end = " ")

heapSort(heap)

print("\nArray after Sorting: ")

for i in range(n):
    print(heap[i], end = " ")