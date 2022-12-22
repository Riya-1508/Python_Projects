from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("890x500+280+170")
root.resizable(False,False)

def getWeather():
    # try:
        city = textfield.get()

        geolocator = Nominatim(user_agent ="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home = pytz.timezone(result)
        localtime = datetime.now(home)
        current_time = localtime.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER:")

    #weather
        api = "https://api.openweathermap.org/data/2.5/weather?q="+ city+"&appid=95d602dde82494fe35ec1497d5418d74"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
#
# except Exception as e:
#     messagebox.showerror("invalid")

#search box in app
#for jpeg image insertion
search_image = Image.open("photo2.jpeg")
photo = ImageTk.PhotoImage(search_image)
img_label = Label(image=photo, height=10, width=10, bg="white", borderwidth=2)
img_label.place(x=18,y=20)

textfield = tk.Entry(root,justify="center",width=10,font=("poppins",20,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=117,y=25)
textfield.focus()

# Serch_icon
img = Image.open("searchicon.png")
resized_img = img.resize((32,32),Image.ANTIALIAS)
new_img =ImageTk.PhotoImage(resized_img)

img_icon = Button(image=new_img,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
img_icon.place(x=268,y=25)

#logo
logo_img = Image.open("weather_logo.jpg")
resizedlogo = logo_img.resize((250,210),Image.ANTIALIAS)
logoimage = ImageTk.PhotoImage(resizedlogo)
logo_label = Label(image=logoimage)
logo_label.place(x=160,y=100)

#Bottom box
box_img = PhotoImage(file="blue_box.png")
label = Label(image=box_img,width=1000,height=200)
label.pack(padx=5,pady=5,side=BOTTOM)

#time
name = Label(root,font=('arial',14,'bold'))
name.place(x=30,y=100)
clock = Label(root,font=('Helvetica',20))
clock.place(x=30,y=130)

#label
label1 = Label(root,text="WIND",font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
label1.place(x=120,y=400)

label2 = Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
label2.place(x=250,y=400)
label3 = Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
label3.place(x=430,y=400)

label4 = Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
label4.place(x=650,y=400)

t = Label(font=('arial',70,'bold'),fg='#ee666d')
t.place(x=400,y=150)
c=Label(font=('arial',15,'bold'))
c.place(x=400,y=250)

w= Label(text="....",font=('arial',21,'bold'),bg='#1ab5ef')
w.place(x=120,y=430)

h= Label(text="....",font=('arial',21,'bold'),bg='#1ab5ef')
h.place(x=280,y=430)

d= Label(text="....",font=('arial',21,'bold'),bg='#1ab5ef')
d.place(x=450,y=430)

p= Label(text="....",font=('arial',21,'bold'),bg='#1ab5ef')
p.place(x=670,y=430)
root.config(bg="#E1BEE7")
root.mainloop()
