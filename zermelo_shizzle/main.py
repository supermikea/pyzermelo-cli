import functions
import time
import os
import requests.exceptions

def main():  # TODO the actual client
	"""
	this initializes everything
	"""
	print("to be completed")
	print("for now u will just get the usual prompt")
	os.system('clear')
	try:
		user_info = functions.authenticate()
	except ConnectionError:
		print("Please connect to the internet\nType \"y\" when connected")
		while True:
			temp = input("> ")
			if temp == "y" or "Yes" or "Y" or "yes":
				break
	
	print("when in numbers:")
	choice = input("> ")
	try:
		choice = int(choice)
	except ValueError:
		choice = 0
	
	os.system('clear')
	functions.get_shedule(user_info, choice)


if __name__ == "__main__":
	main()
