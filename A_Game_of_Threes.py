#/r/DailyProgrammer Challenge #239
#A Game of Threes

from sys import exit

def game_of_threes(num):
	if num == 1:
		print num
		exit(0)
	num_plus_1 = num + 1
	num_minus_1 = num - 1
	if num % 3 == 0:
		new_num = num / 3
		print num, " 0"
		game_of_threes(new_num)
	elif num_plus_1 % 3 == 0:
		new_num = num_plus_1 / 3
		print num, " 1"
		game_of_threes(new_num)
	elif num_minus_1 % 3 == 0:
		new_num = num_minus_1 / 3
		print num, " -1"
		game_of_threes(new_num)

start_num = 100
game_of_threes(start_num)