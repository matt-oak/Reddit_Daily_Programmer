#/r/DailyProgrammer Challenge #1 [Intermediate]
#Event organizer program

import numpy as np

event_list = []
for i in range(0, 24):
	event_list.append(0)

def add_event():
	global event_list
	hour = int(raw_input("Hour you'd like to schedule the event: "))
	option = raw_input("AM or PM: ")
	info = raw_input("Event information: ")
	if option == "am" or option == "AM" or hour == 12:
		if event_list[hour] != 0:
			print "\n"
			print "Event already scheduled at this time"
		else:
			event_list[hour] = info
	elif option == "pm" or option == "PM":
		hour = hour + 12
		if event_list[hour] != 0:
			print "\n"
			print "Event already scheduled at this time"
		else:
			event_list[hour] = info
	else:
		print "Invalid input"

def del_event():
	global event_list
	hour = int(raw_input("Hour of event you'd like to delete: "))
	option = raw_input("AM or PM: ")
	if option == "am" or option == "AM" or hour == 12:
		if event_list[hour] == 0:
			print "\n"
			print "No event to delete"
		else:
			event_list[hour] = 0
	elif option == "pm" or option == "PM":
		hour = hour + 12
		if event_list[hour] == 0:
			print "\n"
			print "No event to delete"
		else:
			event_list[hour] = 0
	else:
		print "Invalid input"

def edit_event():
	global event_list
	hour = int(raw_input("Hour of event you'd like to edit: "))
	option = raw_input("AM or PM: ")
	new_info = raw_input("Event's new information: ")
	if option == "am" or option == "AM" or hour == 12:
		if event_list[hour] == 0:
			print "\n"
			print "No event to edit"
		else:
			event_list[hour] = new_info
	elif option == "pm" or option == "PM":
		hour = hour + 12
		if event_list[hour] == 0:
			print "\n"
			print "No event to edit"
		else:
			event_list[hour] = new_info

print "Daily Event Organizer"
print "Program to add, delete, and edit events on a day-to-day basis"
print "-------------------------------------------------------------"
print "User Input Key:"
print " [a] - Add Event"
print " [d] - Delete Event"
print " [e] - Edit Event"
print " [q] - Quit"

while True:
	user_input = raw_input("Action: ")
	if user_input == "q":
		exit()
	elif user_input == "a":
		add_event()
	elif user_input == "d":
		del_event()
	elif user_input == "e":
		edit_event()
	else:
		print "Invalid input, please refer to User Input Key"
	
	print "\n"
	print "---------------------------------------------------------"
	print "                        EVENTS                           "
	for i in range(0, 24):
		if event_list[i] != 0:
			if i >= 12:
				if i == 12:
					print i, "PM: ", event_list[i]
				else:
					hour = i % 12
					print hour, "PM: ", event_list[i]
			else:
				print i, "AM: ", event_list[i]
	print "---------------------------------------------------------\n"		