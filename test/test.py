
class Simple:

	def __init__(self):
		self.name = ''	

	def get_name(self):
		self.name = input('Enter you name: ')
		print('Hello ', self.name)

	def count_vowels(self):
		vowels = ['a','e','i','o','u']
		nvowels = 0
		for vowel in vowels: 
			nvowels += self.name.count(vowel)
		print('You have %d vowels in your name ' % nvowels )

