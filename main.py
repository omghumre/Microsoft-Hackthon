from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root=Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

def getWeather():
    city=textfield.get()
    geolocator= Nominatim (user_agent="geoapi Exercises")
    location= geolocator.geocode (city)
    obj = TimezoneFinder()
    result = obj.timezone_at (lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)
    long_lat.config(text=f"{round(location. latitude,4)}°N,{round(location. longitude,4)}°E")  #° or deg

    home=pytz.timezone (result)
    local_time = datetime.now(home)
    current_time=local_time.strftime ("%I:%M %p          %A %x")
    clock.config(text=current_time)
    # clock.after(1000,getWeather)

    #whether
    long = str(location.longitude)
    lat = str(location.latitude)
    print("lat="+lat+"long="+long)
    api = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+long+"&units=metric&appid=010af782a9276348b27610f54aae35ea"

    json_data = requests.get(api).json()

    temp = json_data['main']['temp']
    humidity = json_data['main']['humidity']
    pressure =  json_data['main']['pressure']
    wind= json_data['wind']['speed']
    description = json_data['weather'][0]['main']

    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=description)
    

    #first cell
    firstdayimage= json_data['weather'][0]['icon']
    # print(firstdayimage)
    photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    tempday1 = json_data['main']['temp_max']
    tempnight1=json_data['main']['temp_min']
    day1temp.config(text=f"Max: {tempday1}°C\n Min: {tempnight1}°C")


    #days
    first  = datetime.now()
    day1.config(text=first.strftime("%A"))

    return





##icon
image_icon = PhotoImage(file="download.png")
root.iconphoto (False,image_icon)

Round_box=PhotoImage(file="logos/box-hori.png")
Label (root, image=Round_box, bg="#57adff").place(x=30, y=280)

#label

label1=Label (root, text="Temperature", font=('Helvetica',11),fg="white", bg="#203243")
label1.place(x=50, y=290)

label2=Label (root, text="Humidity", font=('Helvetica',11),fg="white", bg="#203243")
label2.place(x=50, y=310)

label3=Label (root, text="Pressure", font=('Helvetica',11),fg="white", bg="#203243")
label3.place(x=50, y=330)

label4=Label (root, text="Wind Speed", font=('Helvetica',11),fg="white", bg="#203243")
label4.place(x=50, y=350)

label5=Label (root, text="Description", font=('Helvetica',11),fg="white", bg="#203243")
label5.place(x=50, y=370)

##search box                                                           edit require
Search_image=PhotoImage (file="logos/search-bar.png")
myimage=Label(image=Search_image, bg="#57adff")
myimage.place(x=270, y=120)

textfield=tk.Entry (root, justify='center',width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0,fg="white")
textfield.place(x=330,y=130) 
textfield.focus()

Search_icon=PhotoImage (file="logos/search-icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243",command=getWeather)
myimage_icon.place(x=605,y=133)

##Bottom box
# frame=Frame (root, width=900,height=180, bg="#212120")
# frame.pack(side=BOTTOM)

#bottom boxes                                                    image of box to be added (22:31)
firstbox=PhotoImage(file="logos/bottom-box-hori.png")
secondbox = PhotoImage (file="logos/bottom-box-ver.png")
Label(root, image=firstbox, bg="#ffffff").place(x=300, y=280)

#clock (here we will place time)
clock=Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=20)

#timezone
timezone=Label (root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)
long_lat=Label (root, font=("Helvetica", 10), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)




#thpwd
t=Label (root, font=("Helvetica",11),fg="white", bg="#203243")
t.place(x=150, y=290)
h=Label (root, font=("Helvetica",11), fg="white", bg="#203243")
h.place(x=150, y=310)
p=Label(root, font=("Helvetica",11),fg="white", bg="#203243")
p.place(x=150, y=330)
w=Label (root, font=("Helvetica", 11),fg="white", bg="#203243")
w.place(x=150, y=350)
d=Label (root, font=("Helvetica", 11),fg="white", bg="#203243")
d.place(x=150, y=370)


#first cell
firstframe=Frame (root, width=230, height=132, bg="#282829")
firstframe.place (x=305, y=285)
day1=Label(firstframe, font="arial 20", bg="#282829",fg="#fff")
day1.place(x=100, y=5)
firstimage=Label(firstframe, bg="#282829")
firstimage.place(x=1, y=15)
day1temp=Label (firstframe, bg="#282829", fg="#57adff", font="arial 15 bold")
day1temp.place(x=100, y=50)


root.mainloop()