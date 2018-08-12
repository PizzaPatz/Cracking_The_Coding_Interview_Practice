input_str1 = "aTact jCoaa"
input_str2 = "taco cat"
input_str3 = "very taco cat"
input_str4 = "very very taco cat"

input_str4 = input_str4.lower()

alpha_dict = dict()

def check_palindrome(input_str):	
	mirror_chars = False
	mid_char_exists = False
	for i in range(0,len(input_str)):
		if input_str[i] is not " ":
			if input_str[i] not in alpha_dict:
				alpha_dict[input_str[i]] = 1
			else:
				alpha_dict[input_str[i]] += 1

	for e in alpha_dict:
			if(alpha_dict[e] % 2 == 0):
				mirror_chars = True
			elif(alpha_dict[e] == 1 and not mid_char_exists):
				mid_char_exists = True
			else:
				return False
	return True


print(check_palindrome(input_str4))
