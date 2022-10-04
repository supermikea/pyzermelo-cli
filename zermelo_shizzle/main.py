import zermelo
import calendar
import datetime
import time

school = "maartenscollege"
cl = zermelo.Client(school) # defines client

def authenticate(key):
    user_info = dict();
    token = cl.authenticate(key)
    print(token)
    user = cl.get_user(token.get('access_token'))
    print(user)
    user_info['token'] = token.get('access_token')
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

get_shedule(authenticate(input("key: ")))
