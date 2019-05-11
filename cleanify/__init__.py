#usr/bin/env python3
# Cleanify 0.1 beta
# Program to create clean, profanity free UUIDs.


class uuid:

	def __init__(self):
		pass
	#To search for a match in the bad words db (txt file).
	def filter_uuid(self, string, file='bad_words.txt'):
		import re
		string = string.lower()
		with open(file, 'r') as fin:
			counter = 0
			for lines in fin:
				if re.findall(lines, string):
					counter += 1
					break
			#Checking the counter to see if the for loop encountered any bad words.
			if counter == 0:
				return False
			else:
				return True


	def write_uuid(self, string, file):
		with open(file, 'a') as fout:
			fout.write(string)
			
	def random_uuid(algo, length):
		import string, random
		algorithms = {base64:string.ascii_letters+string.digits+"-_"}
		
		#To check if the user has selected the correct algoritm
		if algo not in algorithms:
			print("yes")
			return False
		else:
			random_uuid = "".join(random.SystemRandom().choices(algorithms[algo], k=length))
			return random_uuid



if __name__ == '__main__':
	algo = input("algo:")
	length = int(input("length"))
	uuid.random_uuid()