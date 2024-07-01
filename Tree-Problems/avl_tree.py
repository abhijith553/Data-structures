class Node:
	def __init__(self, data = None)
		self.data = data
		self.next = None
		self.prev = None

class avl_tree:
	def fix_RR(): # to fix RR we rotate the parent and the immediate right child anti-clockwise 
		pass
	def fix_LL(): # to fix LL we rotate parent and immediate left child clock-wise from the point of unbalance
		pass
	def fix_RL(): # to fix RL we pick the leaf node and the immediate parent and rotate clock-wise and use the RR fix ( two rotations total )
		pass
	def fix_LR(): # to fix LR we pick the lead node and immediate parent and perform a anti-clockwise rotation to obtain LL, use LL fix then ( two rotations total )
		pass
	def check_height():
		allowed_heights = [-1, 0, 1]
		pass
	def balance_factor(): # immediately during insertion of elements to tree we are fixing the balance factor issue, as this is the preferred method
		pass

def inorder_traversal():
	pass

def insert_to_avl():
	pass

for j in range(n):
	e = int(input("Pass in the nodes in order: "))
	insert_to_avl(e)

obj = Node()
value_list = []
tree = avl_tree()
tree.insert_node(value_list)

def search_for_node(whichNode):
