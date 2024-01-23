from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import *

root=Tk()
root.title("Weather App")
root.geometry("1000x600")
root.resizable(False,False)
def getWeather():
    try:
        city=textfield.get()
        geolocator=Nominatim(user_agent="geoapi Exercises")
        location=geolocator.geocode(city)
        obj = TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        n.config(text="CURRENT TIME")
        name.config(text="CURRENT TEMPERATURE")

       #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        visibility=json_data['visibility']
        minimumtemp=int(json_data['main']['temp_max']-273.15)
        maximumtemp=int(json_data['main']['temp_max']-273.15)
        feels_like=int(json_data['main']['feels_like']-273.15)
        country=json_data['sys']['country']
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"*"))
        c.config(text=(condition,"|","FEELS","LIKE",feels_like,"*C"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
        v.config(text=visibility)
        mint.config(text=minimumtemp)
        maxt.config(text=maximumtemp)
        con.config(text=country)

        

        # 
        
        if(condition=="Rain"):
            Logo_image =PhotoImage(file="rain.png") 
            logo.configure(image=Logo_image)
            logo.image = Logo_image
            logo.place(x=350,y=123)
            
        elif(condition=="Clouds" or condition=="Mist"):
            Logo_image =PhotoImage(file="cloud.png") 
            logo.configure(image=Logo_image)
            logo.image = Logo_image
        
        elif(condition=="Clear"):
            Logo_image =PhotoImage(file="clear.png") 
            logo.configure(image=Logo_image)
            logo.image = Logo_image
        
        elif(condition=="Thunderstrom"):
            Logo_image =PhotoImage(file="thunder.png") 
            logo.configure(image=Logo_image)
            logo.image = Logo_image
            
        elif(condition=="Haze"):
            Logo_image =PhotoImage(file="haze.png") 
            logo.configure(image=Logo_image)
            logo.image = Logo_image
        
        else:
            Logo_image =PhotoImage(file="sunny.png") 
            logo.configure(image=Logo_image)
            logo.image = Logo_image


        label11=Label(root,text="MAX TEMP.",font=("Helvetica",15,'bold'),fg="black")
        label11.place(x=20,y=320)

        label12=Label(root,text="MAX TEMP.",font=("Helvetica",15,'bold'),fg="black")
        label12.place(x=170,y=320)

        label13=Label(root,text="COUNTRY:",font=("Helvetica",15,'bold'),fg="black")
        label13.place(x=60,y=400)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry !!  or No Internet connection")

#search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=250,y=20)
textfield=tk.Entry(root,justify="center",width=15,font=("poppins",25,"bold"),border=0,fg="white",bg="#404040")
textfield.place(x=360,y=40)
textfield.focus()
Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)#
myimage_icon.place(x=670,y=34)

#logo
from cProfile import label
from tkinter import BOTTOM, Frame, Label, PhotoImage, font

# Logo_image =PhotoImage() 
# logo = Label(image=Logo_image)
# logo.place(x=340,y=123)

Logo_image =PhotoImage() 
logo = Label(image=Logo_image)
logo.place(x=340,y=123)

#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
n=Label(root,font=("arial",15,"bold"))
n.place(x=70,y=150)
clock=Label(root,font=("Helvetica",20),fg="#273c75")
clock.place(x=85,y=180)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="black",bg="#1ab5ef")
label1.place(x=90,y=500)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="black",bg="#1ab5ef")
label2.place(x=220,y=500)

label3=Label(root,text="DISCRIPTION",font=("Helvetica",15,'bold'),fg="black",bg="#1ab5ef")
label3.place(x=400,y=500)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="black",bg="#1ab5ef")
label4.place(x=620,y=500)

label5=Label(root,text="VISIBILITY",font=("Helvetica",15,'bold'),fg="black",bg="#1ab5ef")
label5.place(x=810,y=500)

name=Label(root,font=("arial",15,"bold"))
name.place(x=650,y=200)
t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=650,y=230)
c=Label(font=("arial",15,"bold"),fg="#273c75")
c.place(x=650,y=330)

w=Label(text="",font=("arial",20,"bold"),bg="#1ab5ef",fg="white")
w.place(x=90,y=530)
h=Label(text="",font=("arial",20,"bold"),bg="#1ab5ef",fg="white")
h.place(x=250,y=530)
d=Label(text="",font=("arial",20,"bold"),bg="#1ab5ef",fg="white")
d.place(x=400,y=530)
p=Label(text="",font=("arial",20,"bold"),bg="#1ab5ef",fg="white")
p.place(x=650,y=530)
v=Label(text="",font=("arial",20,"bold"),bg="#1ab5ef",fg="white")
v.place(x=810,y=530)

maxt=Label(text="",font=("arial",20),fg="#273c75")
maxt.place(x=40,y=350)

mint=Label(text="",font=("arial",20),fg="#273c75")
mint.place(x=200,y=350)

con=Label(text="",font=("arial",15),fg="#273c75")
con.place(x=170,y=400)

root.mainloop()



