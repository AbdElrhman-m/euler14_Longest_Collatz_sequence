#superBido solution

def is_even(num):
	if num % 2 == 0:
		return True 
	return False 

def generator(num):
	ls=[num]
	
	while num != 1:
		if is_even(num) == True:
	 		num = num / 2
	 		ls.append(num)
	 	else:
	 		num = 3 * num	 + 1
	 		ls.append(num)
	return ls		
def longest_chain():
	the_longest = 0
	the_main = 0
	for n in range(1,1000000):
		biggest = len(generator(n))		
		if biggest > the_longest:
			the_longest = biggest
			the_main = n
			print the_main, the_longest
	return the_longest , the_main


print longest_chain()
