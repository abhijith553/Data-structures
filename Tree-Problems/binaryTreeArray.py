array = [None] * 10

def root(element):
	if array[0] == None:
		array[0] = element
	else:
		print("Binary tree already contains a root, try again")

def setLeft(element, parentIndex):
	if array[parentIndex] != None:
		array[(2*parentIndex) + 1] = element
	else:
		print("Specified parentIndex was not found, try again")

def setRight(element, parentIndex):
	if array[parentIndex] != None:
		array[(2*parentIndex) + 2] = element
	else:
		print("Specified parentIndex was not found, try again")

root('a')
setLeft('b', 0)
setRight('c', 0)
setLeft('d', 1)
setRight('e', 1)
setRight('f', 2)

print(array)
