# json convert the python dictionary
# above into a json
import json
import turtle

# urllib.request fetch URLs using
# a variety of different protocols
import urllib.request
import time

# webbrowser provides a high-level interface
# to allow displaying Web-based documents
# to users
import webbrowser

# geocoder takes the data and locate these
# locations in the map
import geocoder

# using datetime module
import datetime

# ct stores current time
ct = datetime.datetime.now()
print("current time:-", ct)

# ts store timestamp of current time
ts = ct.timestamp()
print("timestamp:-", ts)



url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("There are currently " +
           # prints number of astronauts
           str(result["number"]) + " astronauts on the ISS: \n\n")

people = result["people"]

# prints names of crew
for p in people :
    file.write('Crew Name: {} || Craft: {}'.format(p['name'], p['craft'])+"\n\n")

# prints names of craft

# print long and lat
g = geocoder.ip('me')
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
screen.bgpic("C:/Users/NazmiDaiki/PycharmProjects/whereiss/map.gif")
screen.register_shape("C:/Users/NazmiDaiki/PycharmProjects/whereiss/iss.gif")
iss = turtle.Turtle()
iss.shape("C:/Users/NazmiDaiki/PycharmProjects/whereiss/iss.gif")
iss.setheading(45)
iss.penup()

while True:
    # load the current status of the ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract the ISS location
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    # Ouput lon and lat to the terminal
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # Update the ISS location on the map
    iss.goto(lon, lat)

    # Refresh each 5 seconds
    time.sleep(5)
