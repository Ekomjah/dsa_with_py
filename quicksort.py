def quick_sort(arr):
    if len(arr) < 1:
        return []
    if len(arr) == 1:
        print("base case", arr)
        return arr
    end_arr = len(arr) - 1
    pivot = arr[end_arr]
    sorted_arr = arr.copy() 
    i = -1
    for j in range(len(sorted_arr)):
        if j==end_arr:
            print("landing")
            sorted_arr[i+1],sorted_arr[j] = sorted_arr[j],sorted_arr[i+1]
            print(i+1, sorted_arr[i+1],j, sorted_arr[j],sorted_arr)
        elif sorted_arr[j] < pivot:
            i+=1
            sorted_arr[i],sorted_arr[j] = sorted_arr[j], sorted_arr[i]
            print(f"swapping {sorted_arr[i]} and {sorted_arr[j]}-{sorted_arr}")
    left_part = sorted_arr[:sorted_arr.index(pivot)]
    print("left side", left_part)
    right_part = sorted_arr[sorted_arr.index(pivot)+1:]
    print("right side", right_part)
    return quick_sort(left_part) + [pivot] + quick_sort(right_part)

sort_arr = [20, 3, 14, 1, 5]
print(quick_sort(sort_arr))