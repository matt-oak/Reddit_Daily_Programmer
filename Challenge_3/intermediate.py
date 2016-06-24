#/r/DailyProgrammer Challenge #3 [Intermediate]
#Better encryption than Challenge #3 [Easy]
#RSA Encryption Implementation
#Usage: python intermediate.py [number_of_bits]

#Imports
import sys
import math
import time
from random import getrandbits

#Extended Euclid Algorithm
def extended_euclid(a, b):
	x, y, xprime, yprime = 0, 1, 1, 0
	while b != 0:
		q, r = divmod(a, b)
		a, b = b, r
		x, xprime = xprime - q * x, x
		y, yprime = yprime - q * y, y
	return xprime, yprime

#Find the multiplicative inverse
def inverse(e, n):
	x, y = extended_euclid(e, n)
	if x < 0:
		return n + x
	return x

def main(argv):
	bits = int(sys.argv[1])
	pstopper = True
	qstopper = True
	estopper = True
	looper = True
	
	#Generate random prime with n bits, p
	while looper == True:
		start1 = time.time()
		while pstopper == True:
			pnum = getrandbits(bits)
			if pnum == 0 or pnum == 1:
				continue
			if pnum == 2:
				pstopper = False
			if pnum == 4:
				continue
			for i in range(3, pnum):
				if (pnum % i) == 0:
					break
			else:
				pstopper = False
		
		#Generate random prime with n bits, q		
		while qstopper == True:
			qnum = getrandbits(bits)
			if qnum == 0 or qnum == 1: 
				continue
			if qnum == 2:
				qstopper = False
			if qnum == 4:
				continue
			for i in range(3, qnum):
				if (qnum % i) == 0:
					break
			else:
				qstopper = False
		
		#Ensure p and q are different
		if pnum == qnum:
			continue
		
		#The message we want to send
		x = 1337

		#Calculate n
		n = qnum * pnum

		#Ensure n is greater than the message we want to send
		if n < 1337:
			continue
		pnumm = pnum - 1
		qnumm = qnum - 1
		totient = pnumm * qnumm
		
		#Generate random prime with n bits, e
		while estopper == True:
			enum = getrandbits(bits)
			if enum > totient or enum == 0 or enum == 1:
				continue
			if enum == 2:
				estopper = False
			if enum == 4:
				continue
			for i in range (3, enum):
				if (enum % i) == 0:
					break
			else:
				estopper  = False
				
		#Generate multiplicative inverse of e and (p - 1)(q - 1)
		d = inverse(enum, totient)	
		end1 = time.time()
		time1 = end1 - start1
		start2 = time.time()

		#Encrypt
		y = (x**enum)%n
		end2 = time.time()
		time2 = end2 - start2
		start3 = time.time()

		#Decrypt
		decrypted = (y**d)%n
		end3 = time.time()
		time3 = end3 - start3
		
		print "P is: ", pnum
		print "Q is: ", qnum
		print "N is: ", n
		print "E is: ", enum
		print "Inverse is: ", d
		print "Message is: ", x
		print "Encrypted message is: ", y
		print "Decrypted message is: ", decrypted
		print ("Time to generate public and private keys: %f %s" %(time1, 'seconds'))
		print ("Time to encrypt message: %f %s" %(time2, 'seconds'))
		print ("Time to decrypt message: %f %s" %(time3, 'seconds'))
		looper = False
		break
	return
	
if __name__ == "__main__":
	main(sys.argv)
