#/r/DailyProgrammer Challenge #1 [Hard]
#Higher/Lower number guessing game

nums = []
for i in range(1, 101):
	nums.append(i)

while True:
	mid = len(nums)/2
	input = raw_input("Is your number [e]qual, [g]reater than, or [l]ess than " + str(nums[mid]) + "?\n")
	if input == "e":
		print "Number found!"
		exit()
	elif input == "g":
		nums = nums[mid:]
		continue
	elif input == "l":
		nums = nums[:mid]
		continue
	else:
		print "Invalid input"
		continue