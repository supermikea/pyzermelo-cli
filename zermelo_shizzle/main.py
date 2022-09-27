import zermelo
import calendar
import datetime
import time

def is_key():
    try:
        f = open("key.txt", "x")
        f.close()
        print("succes")
        key = False
        return key
    except:
        key = True
        print("not succeed")
        return key
# INITIALISATION
school = "maartenscollege"
cl = zermelo.Client(school) # defines client
if is_key(): # if there is no key present ask for key
    pass
else:
    key = input('your key') # TODO check if key is aviable if not ask for key
    f = open("key.txt", "w")
    f.write(key)

try:
    f = open("key.txt", "r")
    print("succees")
except:
    print("not succeed")
    pass
key = f.readline()
token = cl.authenticate(key) # gets token
f.close()
f = open("zermelo_shizzle/token.txt", "w")
f.write(str(token))
print(token)
f = open("zermelo_shizzle/token.txt", "r") # TODO fix dit stukje en kijk naar deze website: https://www.w3schools.com/python/python_dictionaries_access.asp en token.txt hoe
token = f.readline()
token = token
user = cl.get_user(token) # defines user
token.close() # closes token file
ctime = int(time.time())
yesterday = ctime - 96400

Happointments = cl.get_appointments(token, yesterday, ctime) # appointments kijgen

Happointments = Happointments.get('response')   # MIKE heeft DE LIST IN DEZE DICTIONARY ERUITgeHAaLd
appointments = Happointments.get('data') # deze python code zorgt ervoor dat hij de vakkken eruithaalt
for appointment in appointments: # met deze
    print(appointment.get('subjects'), end='')
    print(appointment.get('teachers'))