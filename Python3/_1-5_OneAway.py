def OneAway(str1, str2):
	max_length = 0
	if ( len(str1) > len(str2) ):
		max_length = len(str1)
	else:
		max_length = len(str2) 

	adv_a = 0
	adv_b = 0
	change_token = 1 # allow chance only 1 time
	i = 0
	while( i < max_length ):
		# Catch out of bound
		#print(i,adv_a,adv_b,change_token)
		if(i >= len(str1) or i >= len(str2)): # EOF insertion
			if(change_token > 0):
				change_token -= 1
				return True # E.g. pales, pale
				break
			if(str1[-1] == str2[-1] and change_token < 1):
				return True # E.g. pale, ple
		if(str1[i+adv_a] == str2[i+adv_b]): # Advance both
			i += 1	
		elif(i+adv_a+1 < len(str1) and str1[i+adv_a+1] == str2[i]): # Remove / Add operation
			adv_a += 1
			change_token -= 1
		elif(i+adv_b+1 < len(str2) and str2[i+adv_b+1] == str1[i]): # Remove / Add operation
			adv_b += 1
			change_token -= 1
		elif(str1[i+adv_a] != str2[i+adv_b] and len(str1) == len(str2)): # Assuming this is Replace operation
			change_token -= 1
			i += 1
		else:
			return False
	if(change_token == 0):
		return True
	else:
		return False
str1 = "pale"
str2 = "pales"
str3 = "bale"
str4 = "bake"
str5 = "ple"
print(OneAway(str1, str4))

