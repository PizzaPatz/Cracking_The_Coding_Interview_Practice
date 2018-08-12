''' Given two strings, write a method to decide if one is a permutation of the other'''
from _binary_tree import Node

# Using ascii approach

str1 = 'abc'
str2 = 'bca'

''' Grab the first letter for init tree'''

tree1 = Node(ord(str1[0])-97)
tree2 = Node(ord(str2[0])-97)

for i in range(1,len(str1)):
	tree1.insert(ord(str1[i])-97)

for j in range(1,len(str2)):
	tree2.insert(ord(str2[j])-97)

tree1.print_tree()
print('----')
tree2.print_tree()
