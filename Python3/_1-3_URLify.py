input_str = "Mr John Smith     "

''' Start trimming at the end of the string first '''
rev_str = ''
eof_space = True

for i in range(1, len(input_str)+1): # Print this in reverse
	if(input_str[-i] == " " and eof_space == True):
		pass #ignore EOF space
	elif(input_str[-i] == " " and eof_space == False):
		rev_str += "02%" # Somewhat bruteforce way, but you can declare reversed desire string on top too
	else:
		rev_str += input_str[-i]
		eof_space = False



print(rev_str[::-1])
