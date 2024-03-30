'''
time complexity is O(n^2)
space complexity is O(1)
'''

def bubbleSort(arr):
	n = len(arr)
	for j in range(n-1, 0, -1):
		swapped = 0
		for i in range(j):
			if arr[i] > arr[i+1]:
				swapped = 1
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
		print("Array after each pass", arr)
		if not swapped:
			return
arr = [50, 4, 31, 17, 80]
bubbleSort(arr)
print("\nAfter sorting", arr)