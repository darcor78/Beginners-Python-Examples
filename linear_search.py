# Linear Search or Sequential Search Algorithm

def linear_search(array, to_find):
	pos = 1				
	for i in array:			
		if i != to_find:	
			pos += 1
		else: 
			return pos 	
	return
	
nums = [12, 34, 54, 88, 21]			
print(linear_search(nums, 65))
