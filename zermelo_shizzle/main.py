import zermelo
import calendar
import datetime
import time
from os import listdir

school = "maartenscollege"
cl = zermelo.Client(school) # defines client

def authenticate():
    user_info = dict();
    try:
        token = write_read_tk(False, 0)
        user_info['token'] = token
        user_info['user'] = cl.get_user(token)
        return user_info
    except:
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


    ctime = int(time.time())
    today00 = (ctime - ctime % 86400) - 7200

    Happointments = cl.get_appointments(user_info.get('token'), today00, today00 + 86400) # appointments kijgen

    Happointments = Happointments.get('response')   # MIKE heeft DE LIST IN DEZE DICTIONARY ERUITgeHAaLd
    appointments = Happointments.get('data') # deze python code zorgt ervoor dat hij de vakkken eruithaalt
    for appointment in appointments: # met deze
        print(appointment.get('subjects'), end='')
        print(appointment.get('teachers'))


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
