from userlib import UserLib

class Exclusive(UserLib):
	
	def __help__(self):
		usage = '''Usage: cat
	Concatenate files and print on the standard output

cat <file> - To print the contents of a file
cat -v     - To print the version of the command
cat help   - To get this help screen
'''
		print(usage)

	def run(self, args:list=None):
		if args[0] == 'help':
			self.__help__()
			
		elif args[0] == '':
			print('cat: error: file name required!')
		
		else:
			with open(args[0], 'r') as f:
				f2 = [i.rstrip('\n') for i in f.readlines()]
				for i in f2:
					print(i)

