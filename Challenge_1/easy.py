#/r/DailyProgrammer Challenge #1 [Easy]
#Program that asks for the user's name, age, and reddit username

name = raw_input("Name: ")
age = raw_input("Age: ")
username = raw_input("Reddit Username: ")

print "Your name is", name, "you are", age, "years old, and your username is", username

#Extra credit: Log this information in a file to be accessed later

log_file = open("User_Info.txt", "w")
log_file.write("Name: %s\n" % name)
log_file.write("Age: %s\n" % age)
log_file.write("Reddit Username: %s\n" % username)
log_file.close()