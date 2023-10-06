from tkinter import *
from unittest import result
from geopy import distance
from geopy.geocoders import Nominatim

font_family = "Helvetica 17 bold"
blue = "#1F2B8F"
white = "#FAFAFA"
explosive = "#C4C4C4"
american_grey = "#808080"


def distance_find():
    try:
        geolocator = Nominatim(user_agent="geoLocation")

        city1 = geolocator.geocode(str(geo1.get()))
        city2 = geolocator.geocode(str(geo2.get()))

        Loc1_let, Loc1_lon = (city1.latitude), (city1.longitude)
        Loc2_let, Loc2_lon = (city2.latitude), (city2.longitude)

        location1 = (Loc1_let, Loc1_lon)
        location2 = (Loc2_let, Loc2_lon)

        dist = (str(distance.distance(location1, location2).km) + " Km")

        result.set(dist)
    except:
        result.set("Something Went Wronge....!")


csa = Tk()
csa.title("Distance Finder App")
csa.config(bg=explosive)

txt = Label(csa, text="Python App for Distace Measurment",
            font=font_family, bg=explosive, fg=american_grey)
txt.grid(row=1, column=0, columnspan=3, rowspan=4, padx=20, pady=4)

result = StringVar()

Label(csa, text="Enter First Place Name :", bg=explosive,
      fg=american_grey).grid(row=5, sticky=W)
Label(csa, text="Enter Second Place Name :", bg=explosive,
      fg=american_grey).grid(row=6, sticky=W)
Label(csa, text="Result :", bg=explosive).grid(row=7, sticky=W)
Label(csa, text="", textvariable=result, bg=explosive).grid(
    row=7, column=1, sticky=W)

geo1 = Entry(csa, width=50)
geo1.grid(row=5, column=1)
geo2 = Entry(csa, width=50)
geo2.grid(row=6, column=1)

btn = Button(csa, text="Search", bg=explosive,
             fg=american_grey, command=distance_find)
btn.grid(row=5, column=2, columnspan=3, rowspan=2, padx=5, pady=5)

csa.mainloop()
