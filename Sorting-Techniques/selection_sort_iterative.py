def selection_sort_recursive(arr, start_idx=0):
    if start_idx >= len(arr):
        return arr

    min_idx = start_idx
    for i in range(start_idx + 1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i

    arr[start_idx], arr[min_idx] = arr[min_idx], arr[start_idx]
    selection_sort_recursive(arr, start_idx + 1)
    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort_recursive(arr)
print("Sorted array:", sorted_arr)
