class MIT(object):
	'''base class 
	https://www.youtube.com/watch?v=NUfpzbZkFf4'''
	first_name = ''
	last_name = ''

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

class mit_ta(MIT):

	awesome_factor = 0

	def __init__(self, first_name, last_name, awesome_factor):
		self.awesome_factor = awesome_factor
		MIT.__init__(self, first_name, last_name)

	def retstr(self):
		return f"{self.first_name} {self.last_name}'s score is {self.awesome_factor}"

nitin = mit_ta('nitin', 'mittal', 100)

print(nitin.retstr())
