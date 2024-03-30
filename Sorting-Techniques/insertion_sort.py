def insertionSort(a):
	n  = len(arr)
	for i in range(1, n):
		temp = a[i]
		j = i - 1
		while j >=0 and a[j] > temp:
			a[j + 1] = a[j]
			j = j - 1
		a[j + 1] = temp
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)