#/r/DailyProgrammer Challenge #2 [Intermediate]
#Basic dungeon-crawler game

import time
import random

items = 0
enemies_killed = 0
first_room = 0


def intro():
	print "------------------------------------------------------------------------------"
	print "M'Lord! We've been seiged by our enemies but we've managed to defend them off!"
	time.sleep(3)
	print "They've retreated into Aisun Cave."
	time.sleep(2)
	while True:
		decision = raw_input("Shall we storm the cave, m'lord? [y]es / [n]o\n")
		if decision == "n":
			print "Understood, m'lord. [Swears you off under his breath]"
			time.sleep(2)
			exit()

		elif decision == "y":
			print "Understood, m'lord, I'll gather the men. We leave at nightfall."
			for i in range(0, 5):
				print " . ",
				time.sleep(1)
			print "\n"
			break

		else:
			print "M'lord! Have you been poisoned by our enemies!? I can't understand you!"
			time.sleep(2)

def room():
	global first_room

	if first_room == 0:	
		print "You and your men enter Aisun Cave. You can sense movement in the darkness..."
		time.sleep(3)
		first_room = first_room + 1

	while True:
		door_choice = raw_input("There are 2 doors. Which do you choose? [l]eft / [r]ight\n")
		door_int = random.randint(1, 3)
		if door_int == 1 and door_choice == "l":
			item_room()
		else:
			encounter()


def encounter():
	global items
	global enemies_killed

	print "ENEMIES!!!"
	time.sleep(.5)

	my_health = 100
	enemy_health = 85

	while True:
		if enemy_health <= 0 and my_health <= 0:
			print "Both you and the enemy were killed in combat! Game over!"
			time.sleep(2)
			print "You killed", enemies_killed, "total enemies!"
			time.sleep(2)
			exit()

		elif enemy_health <= 0:
			print "You defeated the enemy! Time to move onto the next room."
			enemies_killed = enemies_killed + 1
			time.sleep(2)
			room()
		elif my_health <= 0:
			print "You've been killed in battle! Game over!"
			time.sleep(2)
			print "You killed", enemies_killed, "total enemies!"
			time.sleep(2)
			exit()


		decision = raw_input("What do you choose to do? [a]ttack / [i]tem\n")

		if decision == "i":
			if items == 0:
				print "You don't have any items! You must attack with your sword!"
				time.sleep(2)
				continue
			else:
				print "You throw your item at the enemy!"
				time.sleep(1)
				print "You dealt 30 DMG to the enemy!"
				time.sleep(1)
				enemy_health = enemy_health - 30
				items = items - 1
				print "Your health: ", my_health
				print "Enemy health: ", enemy_health
				time.sleep(1.5)

		elif decision == "a":
			my_attack = random.randint(15, 25)
			enemy_attack = random.randint(10, 30)

			print "You dealt", my_attack, "DMG to the enemy!"
			enemy_health = enemy_health - my_attack
			time.sleep(1)
			print "The enemy dealt", enemy_attack, "DMG to you!"
			my_health = my_health - enemy_attack
			time.sleep(1)
			if my_health <= 0 and enemy_health <= 0:
				print "Your health: ", 0
				print "Enemy health: ", 0
				enemies_killed = enemies_killed + 1
			elif enemy_health <= 0:
				print "Your health: ", my_health
				print "Enemy health: ", 0
			elif my_health <= 0:
				print "Your health: ", 0
				print "Enemy health: ", enemy_health
			else:
				print "Your health: ", my_health
				print "Enemy health: ", enemy_health



def item_room():
	global items

	print "Ah! It seems as though there's no enemies in this room."
	time.sleep(2)
	print "What is this? An item?"
	time.sleep(1.5)
	rand_item = random.randint(1, 4)
	if rand_item == 1:
		print "You received a BOMB!"
		items = items + 1
	elif rand_item == 2:
		print "You received a SPEAR!"
		items = items + 1
	else:
		print "You received an AXE!"
		items = items + 1


intro()
room()
