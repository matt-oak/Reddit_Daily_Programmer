#/r/DailyProgrammer Challenge #2 [Hard]
#Stopwatch program

import time

print "Basic stopwatch program"
init_input = raw_input("Enter [s]tart to begin stopwatch: ")

if init_input == "s":
	print "Enter [l] to lap or [e] to stop the stopwatch"
	log_file = open("Stopwatch_Info.txt", "w")
	start = time.time()
	num_laps = 0
	while True:
		input = raw_input()
		if input == "l":
			num_laps = num_laps + 1
			lap = time.time()
			dif = str(lap - start)
			dif = dif[:5]
			print "Lap #" + str(num_laps) + ":", dif, "seconds"
			log_file.write("Lap #%d: %s seconds\n" % (num_laps, dif))
		elif input == "e":
			end = time.time()
			dif = str(end - start)
			dif = dif[:5]
			print "Total time:", dif, "seconds"
			log_file.write("Total time: %s seconds" % dif)
			log_file.close()
			exit()
		else:
			print "Invalid input, please enter [l] for lap or [e] to stop"
			
else:
	print "Invalid input"