def bubbleSort(arr):
    m = len(arr)
    for u in range(m):
        for v in range(m-u-1):
            if arr[v] > arr[v+1]:
                arr[v],arr[v+1] = arr[v+1],arr[v]
    print(arr)

arr = [2,1,7,6,5,3,4,9,8]
bubbleSort(arr)