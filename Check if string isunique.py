def areCharactersUnique(s):
	
	# An integer to store presence/absence
	# of 26 characters using its 32 bits
	checker = 0
	
	for i in range(len(s)):
		
		val = ord(s[i]) - ord('a')
		
		# If bit corresponding to current
		# character is already set
		if (checker & (1 << val)) > 0:
			return False
		
		# set bit in checker
		checker |= (1 << val)
		
	return True
	
