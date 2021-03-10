import gpg
import logging
import os
import random

def inknow():
	uip = int(input("What would you like to do? \n 1)Make a new entry \n 2)View an Entry \n 3)View Files \n Enter #: "))
	if uip == 1:
		global ft, fu, fp, fn, com
		ft = raw_input("What will the File be Called? \n (Will Format to Lowercase) \n (This Will OVERWRITE Files of the SAME NAME):  ").lower()
		fn = ft + ".txt"
		print(fn)
		com = raw_input("Is there a Comment you'd like to add?:   ")
		fu = raw_input("What's the Username?:  ")
		fp = raw_input("Whats the Password? Enter To Generate(35):  ")
		if fp == "":
			generator()
			fp = password
			create()
		else:
			create()
		logger.info("User Made a New File: %s" % (fn))
		raw_input("Enter To Encryption and End...")
		encryption()
	elif uip == 2:
		nx = raw_input("What's the Entries Name(Lowercase, exclude .asc from Entry):  ")
		fn = nx
		logger.info("User Opened %s File" % (nx))
		decryption()

	elif uip == 3:
		xn = os.listdir("/home/user/Desktop/Testing/Projects/PwManager/")
		os.system('cls' if os.name == 'nt' else 'clear')
		print(xn)
		inknow()

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?></';|][=-()*&^%$#@!`~"
def generator():
	global password
	passlen = 35
	password = ""
	for x in range(0, passlen):
		password_char = random.choice(chars)
		password = password + password_char
	print("Here is your Password:  %s" % (password))
	logger.info("User Generated a Password for %s." % (fn))

global logger 
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "pwman.log", level = logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()

def encryption():
	a_key = "YOURKEYIDHERE"
	with open(fn, "rb") as afile:
    		text = afile.read()
		c = gpg.core.Context(armor=True)
		rkey = list(c.keylist(pattern=a_key, secret=False))
		ciphertext, result, sign_result = c.encrypt(text, recipients=rkey,
                                            always_trust=True,
                                            add_encrypt_to=True)
	with open("{0}.asc".format(fn), "wb") as bfile:
    		bfile.write(ciphertext)	
	os.remove(fn)
	os.system('cls' if os.name == 'nt' else 'clear')
	inknow()

def create():
	with open(fn, 'w+') as filen:
		text = str(ft + '\n' + fu + '\n' + fp + '\n' + com)
		filen.write(text)

def decryption():
	a_key = "YOURKEYIDHERE"
	with open("{0}.asc".format(fn), "rb") as cfile:
    		plaintext, result, verify_result = gpg.Context().decrypt(cfile)
    		print(plaintext)
    		inknow()

inknow()
