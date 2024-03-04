def binarySearch(arr, beginIndex, endIndex, target):

	while beginIndex <= endIndex:

		mid = beginIndex + (endIndex - beginIndex) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			beginIndex = mid + 1
		else:
			endIndex = mid - 1
	return -1

arr = [10, 20, 30, 40]
target = 300

result = binarySearch(arr, 0, len(arr)-1, target)

if result != -1:  
	print("Element found at ",result)
else:
	print("Search failed")

