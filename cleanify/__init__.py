# Cleanify 0.1 beta
# Program to create clean, profanity free UUIDs.


class uuid:
	#To search for a match in the db (txt file).
	def filter(string,file):
		import re
		string = string.lower()
		with open(file, 'r') as fin:
			for lines in fin:
				if re.findall(lines, string):
					return True


	def write(string,file):
		with open(file, 'a') as fout:
			fout.write(string)
			
