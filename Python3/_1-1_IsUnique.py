import string
input_unique = "abcdefghijk"
input_not_unique = "abbcdeff"

unique = set()
is_unique = True

''' test unique '''
for i in range(0, len(input_unique)):
	if input_unique[i] in unique:
		is_unique = False
		break
	else: # is still unique / new character
		unique.add(input_unique[i])

print('String contains unique character? ', is_unique)

is_unique = True

''' Test not unique '''
for i in range(0, len(input_not_unique)):
	if input_not_unique[i] in unique:
		is_unique = False
		break
	else: # is still unique / new character
		unique.add(input_not_unique[i])


print('String contains unique character? ' , is_unique)
