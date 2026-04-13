def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(0, arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

print(bubble_sort([21,14,27,18]))