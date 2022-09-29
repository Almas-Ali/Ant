class UserLib:
	'''Ant library maker class.'''
	
	def __init__(self):
		pass
	
	def __help__(self):
		usege = '''Ant user library
version 1.0
'''
		print(usege)
	
	def run(self, args: list = None):
		use = '''Congratulations!
Your library works!
'''
		if args[0] == 'help':
			self.__help__()
		else:
			print(use)

	def __repr__(self):
		return '<Ant Library Object>'
