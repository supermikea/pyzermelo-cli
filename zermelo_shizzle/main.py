import zermelo
import calendar
import datetime
import time

# INITIALISATION
school = "YOUR SCHOOL HERE"
token = cl.authenticate("YOUR KEY HERE") # gets token
token = "YOUR TOKEN HERE" # zermelo token
cl = zermelo.Client(school) # defines client
user = cl.get_user(token) # defines user
ctime = int(time.time())
yesterday = ctime - 96400

Happointments = cl.get_appointments(token, yesterday, ctime) # appointments kijgen

Happointments = Happointments.get('response')   # MIKE heeft DE LIST IN DEZE DICTIONARY ERUITgeHAaLd
appointments = Happointments.get('data') # deze python code zorgt ervoor dat hij de vakkken eruithaalt
for appointment in appointments: # met deze
    print(appointment.get('subjects'), end='')
    print(appointment.get('teachers'))