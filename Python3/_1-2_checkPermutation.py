''' Given two strings, write a method to decide if one is a permutation of the other'''
from _binary_tree import Node

# Using ascii approach

str1 = 'cabc'
str2 = 'bcac'

''' Grab the first letter for init tree'''

tree1 = Node(ord(str1[0])-97)
tree2 = Node(ord(str2[0])-97)

for i in range(1,len(str1)):
	tree1.insert(ord(str1[i])-97)

for j in range(1,len(str2)):
	tree2.insert(ord(str2[j])-97)

sorted_perm1 = tree1.print_tree([])
sorted_perm2 = tree2.print_tree([])

print('Sorted permutation 1: ', sorted_perm1)
print('_____')
print('Sorted permutation 2: ', sorted_perm2)

if(sorted_perm1 == sorted_perm2):
	print('String 1 and String 2 have same permutation')


### Not really efficient way: O(n log n) ###
