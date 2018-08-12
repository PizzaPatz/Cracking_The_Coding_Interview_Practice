import string
input_unique = "abcdefghijk"
input_not_unique = "abbcdeff"

test1 = "acd"
test1 = list(test1)

iter_list = list(range(0,26))
char_list = string.ascii_lowercase[:26]
#print(iter_list)
# Let's use binary tree

''' Convert string to list of char '''
for i in range(0, len(test1)):
	print(string.ascii_lowercase.index(test1[i]))
#print(string.ascii_lowercase.index('b'))
