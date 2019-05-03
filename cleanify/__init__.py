# Cleanify 0.1 beta
# Program to create clean, profanity free UUIDs.


class uuid:
	#To search for a match in the db (txt file).
	def filter(string, file):
		import re
		string = string.lower()
		with open(file, 'r') as fin:
			for lines in fin:
				if re.findall(lines, string):
					return True


	def write(string, file):
		with open(file, 'a') as fout:
			fout.write(string)
			
	def random(algo, length):
		import string, random
		algorithms = {base64:string.ascii_letters+string.digits+"-_"}
		
		#To check if the user has selected the correct algoritm
		if algo not in algorithms:
			return False
			break
		else:
			continue

		random_uuid = "".join(random.SystemRandom().choices(algorithms[algo], k=length))

		return random_uuid