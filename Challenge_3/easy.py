#/r/DailyProgrammer Challenge #3 [Easy]
#Basic Caesar cipher program

def encrypt(user_string):
	enc_char_list = []
	for i in range(0, len(user_string)):
		char = user_string[i]
		if char == " ":
			enc_char_list.append(" ")
		else:
			ascii_char = ord(char) - 97
			new_char = (ascii_char + 3) % 26
			new_char = chr(new_char + 97)
			enc_char_list.append(new_char)
	enc_char_string = ''.join(enc_char_list)
	print "Encrypted:", enc_char_string
	return enc_char_string

def decrypt(enc_string):
	dec_char_list = []
	for i in range(0, len(enc_string)):
		char = enc_string[i]
		if char == " ":
			dec_char_list.append(" ")
		else:
			ascii_char = ord(char) - 97
			new_char = (ascii_char - 3) % 26
			new_char = chr(new_char + 97)
			dec_char_list.append(new_char)
	dec_char_string = ''.join(dec_char_list)
	print "Decrypted:", dec_char_string

user_string = raw_input("Enter the string you'd like to encrypt: ")
enc = encrypt(user_string)
decrypt(enc)