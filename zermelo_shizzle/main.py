import functions
import time


def main():  # TODO the actual client
	"""
	this initializes everything
	"""
	print("to be completed")
	print("for now u will just get the usual prompt")
	time.sleep(1)
	user_info = functions.authenticate()
	functions.get_shedule(user_info)


if __name__ == "__main__":
    main()
