import datetime
import sys
import time

import zermelo


def authenticate(): # authenticate and try to read from file
	global user_info
	global cl
	user_info = {};
	try: 
		school = write_read_f(False, 0, "/school")
		cl = zermelo.Client(school) # defines client
	except:
		school = input("school: ")
		cl = zermelo.Client(school) # defines client
		write_read_f(True, school, "/school")
		user_info['school'] = school
		token = write_read_f(False, 0, "/token")
	try: # try to use token in token file
		token = write_read_f(False, 0, "/token")
		user_info['token'] = token
		user_info['user'] = cl.get_user(token)
		return user_info
	except: # token in token file seems invalid so request key again
		key = input("key: ")
		token = cl.authenticate(key)
		user = cl.get_user(token.get('access_token'))
		user_info['token'] = token.get('access_token')
		write_read_f(True, user_info.get('token'), "/token")
		user_info['user'] = user
		return user_info


		

def get_shedule(userinfo, *args):
	"""
	gets the shedule from the the API with the information given by authenticate
	"""
	time_choice = args[0]

	

	order = []
	ctime = int(time.time())
	today00 = ctime - ctime % 86400 - 7200

	#print(args)
	try:
		m_today00 = today00 + time_choice * 86400
	except ValueError:
		# assume input was 0
		# TODO maybe this is bad code idk mike check it some other day
		m_today00 = today00

	Happointments = cl.get_appointments(user_info.get('token'), m_today00, m_today00 + 86400) # get appointment

	Happointments = Happointments.get('response')   # extracting response out of the list
	#print(Happointments)
	appointments = Happointments.get('data') # this extracts the date out of the response
	for appointment in appointments: # with this code
		order.append(appointment.get('start'))
	order.sort() # with this remove duplicates and sort AND DO NOT TOUCH, PLEASE FOR UR SAFETY
	order = set(order)
	order = sorted(order)
	#print(order)
	for i in order: # search for the appointment time in appointment and if match then print the subject, locations, etc.
		for appointment in appointments:
			if i != appointment.get('start') or not appointment.get('valid'):
				pass
			else: # printing only non cancelled stuff and printing information
				if not appointment.get('cancelled'):
					#print(appointment.get('valid', '\n'))
					print(appointment.get('subjects'), end='')
					print(appointment.get('teachers'), end='')
					print(appointment.get('locations'), end='   ')
					print(datetime.datetime.fromtimestamp(int(appointment.get('start')))
						.strftime('%H:%M:%S') + "  -  ", end='')
					print(datetime.datetime.fromtimestamp(int(appointment.get('end')))
						.strftime('%H:%M:%S'))
					
	




def write_read_f(option, token, location): # write or read token from token file
	if option:
		file = open(sys.path[0] + location, "w")
		file.write(token)
		file.close()
		return 0
	# if option is not True then this is automatically executed
	file = open(sys.path[0] + location, "r")
	token = file.read()
	file.close()
	return token
