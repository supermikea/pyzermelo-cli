import zermelo
import datetime
import time

school = "maartenscollege" # my school currently *you can change it*
cl = zermelo.Client(school) # defines client

def authenticate(): # authenticate and try to read from file
    user_info = dict();
    try: # try to use token in token file
        token = write_read_tk(False, 0)
        user_info['token'] = token
        user_info['user'] = cl.get_user(token)
        return user_info
    except: # token in token file seems invalid so request key again
        key = input("key: ")
        token = cl.authenticate(key)
        print(token)
        user = cl.get_user(token.get('access_token'))
        print(user)
        user_info['token'] = token.get('access_token')
        write_read_tk(True, user_info.get('token'))
        user_info['user'] = user
        return user_info
        

def get_shedule(user_info):

    order = []
    ctime = int(time.time())
    today00 = (ctime - ctime % 86400) - 7200

    Happointments = cl.get_appointments(user_info.get('token'), today00, today00 + 86400) # get appointment

    Happointments = Happointments.get('response')   # extracting response out of the list
    #print(Happointments)
    appointments = Happointments.get('data') # this extracts the date out of the response
    for appointment in appointments: # with this code
        order.append(appointment.get('start'))
    order.sort() # search for the appointment time in appointment and if match then print the subject, locations, etc.
    for i in order:
        for appointment in appointments:# TODO check if appointment already is there, then use the latest appointment (creating date)
            if i != appointment.get('start'):
                pass
            else: # printing only non cancelled stuff and printing information
                if not appointment.get('cancelled'):
                    print(appointment.get('subjects'), end='')
                    print(appointment.get('teachers'), end='')
                    print(appointment.get('locations'), end='   ')
                    print(datetime.datetime.fromtimestamp(int(appointment.get('start')))
                    .strftime('%H:%M:%S') + " - ", end='')
                    print(datetime.datetime.fromtimestamp(int(appointment.get('end')))
                    .strftime('%H:%M:%S'))




def write_read_tk(option, token): # write or read token from token file
    if option:
        file = open("zermelo_shizzle/token", "w")
        print(token)
        file.write(token)
        file.close()
        return 0
    else:
        file = open("zermelo_shizzle/token", "r")
        token = file.read()
        file.close()
        return token

get_shedule(authenticate())
