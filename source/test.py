name = input('Enter you name: ')
print('Hello ', name)

vowels = ['a','e','i','o','u']
nvowels = 0
for vowel in vowels: 
	nvowels += name.count(vowel)
print('You have %d vowels in your name ' % nvowels )

nconsonants = len(name) - nvowels 
print('You have %d consonants in your name ' %nconsonants)
