#/r/DailyProgrammer Challenge #2 [Easy]
#Basic Physics Calculator

from __future__ import division

def find_force(mass, acceleration):
	force = mass * acceleration
	print "\n%.3f N" % force

def find_mass(force, acceleration):
	mass = force / acceleration
	print "\n%.3f kg" % mass

def find_acceleration(force, mass):
	acceleration = force / mass
	print "\n%.3f m/s^2" % acceleration

print "Basic Physics Calculator [BPC]\n"
print "Given 2 knowns, finds the unknown value regarding Force, Mass, and Acceleration\n"
print "Input 2 known values and press [Enter] for unknown value"
print "--------------------------------------------------------------------------------\n"

force = raw_input("Force: ")
mass = raw_input("Mass: ")
acceleration = raw_input("Acceleration: ")

if force == "" and mass != "" and acceleration != "":
	find_force(int(mass), int(acceleration))
elif mass == "" and force != "" and acceleration != "":
	find_mass(int(force), int(acceleration))
elif acceleration == "" and force != "" and mass != "":
	find_acceleration(int(force), int(mass))	
else:
	print "Invalid input. Please provide 2 known values and 1 unknown\n"