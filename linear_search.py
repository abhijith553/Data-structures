def linear_search(array, target):
    temp = array
    for j in range(0, len(temp) + 1):
        if temp[j] == target:
            return j
    else:
        return -1

arr = [13, 3, 82, 90, 45]
target = 82
result = linear_search(arr, target)
if linear_search != -1:
    print(f"Element found at index position {result}")
else:
    print(f"Linear search has failed")