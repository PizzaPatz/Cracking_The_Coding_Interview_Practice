''' 
current is current node BUT not an element

'''

class Node():
	def __init__(self, val, left=None, right=None, arr=[]):
		self.val = val
		self.left = left
		self.right = right
		self.arr = arr
	''' inserting element '''
	def insert(self, new_val):
		''' If the input val is less than current node '''
		if(new_val <= self.val):
			if(self.left != None): # new val is less or equal AND there's still left node
				self.left.insert(new_val) # iterate to the left, no add yet
			else: # new val is less than AND there's NO left node, add new val to the left
				self.left = Node(new_val)
		else: # (new_val > tree.current)
			if(self.right != None): # new val is more AND there's still right node
				self.right.insert(new_val) # iterate to the right, no add yet
			else: # new val is more than AND there's NO right node, add new val to the right
				self.right = Node(new_val)
		pass	
	
	''' printing tree // also return string or sorted tree'''
	def print_tree(self, arr):
		if(self.left != None):
			self.left.print_tree(arr)
		#print(self.val)
		arr.append(str(self.val))
		if(self.right != None):
			self.right.print_tree(arr)
		return (''.join(arr))
		


	''' check exist '''
	def search(self, val):
		found = False;
		if(val < self.val and self.left != None):
			found = self.left.search(val)
		elif(val > self.val and self.right != None):
			found = self.right.search(val)
		elif(val == self.val): # Found
			found = True
		else: # Not Found
			found = False
		return found
	

