#/r/DailyProgrammer Challenge #4 [Easy]
#Basic password generator

from random import randint

num_passwords = int(raw_input('How many passwords would you like to make: '))
len_passwords = int(raw_input('How long would you like the passwords to be: '))

for i in range(0, num_passwords):
	password = ''
	for j in range(0, len_passwords):
		if j % 2 == 0:
			char = chr(randint(65, 90))
		else:
			char = chr(randint(97, 122))
		password = password + char
	print 'Password #' + str(i + 1) + ":", password