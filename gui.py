from pathlib import Path
from defs import *
import jdatetime , time
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image , ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def get_city(city):
    return requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=12239f87290f21f468bac3f5c34fceea')


def start_fetching_network():
    global canvas , network , window
    canvas.itemconfig(network, text=connected())
    window.after(5000, start_fetching_network)

def time_update():
    global canvas , time_element , window
    canvas.itemconfig(time_element, text=time.strftime('time: %H:%M:%S'))
    window.after(1000, time_update)
def get_data_from_api():
    global entry_1 , datas
    city = entry_1.get()

    try:
        data = get_city(city).json()

        if data['cod'] == 404:
            text = 'City not found!'

        else:
            text = f'''\
Lat & Long : {data['coord']['lat']} , {data['coord']['lon']}
Weather : {data['weather'][0]['main']} ({data['weather'][0]['description']})
Temperature : {round(data['main']['temp']-273)}° C
Humidity : {data['main']['humidity']}

'''

    except:
        text = 'Network Error'

    
    

    canvas.itemconfig(datas, text=text)





window = Tk()

window.geometry("600x200")
window.configure(bg = "#FFFFFF")



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 200,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    600.0,
    200.0,
    fill="#D9D9D9",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    74.0,
    119.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    300.0,
    20.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    300.0,
    22.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    531.0,
    89.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    532.0,
    76.0,
    image=image_image_5
)

network = canvas.create_text(
    484.0,
    104.0,
    anchor="nw",
    text=connected(),
    fill="#000000",
    font=("Inter", 15 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    531.0,
    166.0,
    image=image_image_6
)

time_element = canvas.create_text(
    484.0,
    156.0,
    anchor="nw",
    text="time:",
    fill="#292929",
    font=("Inter", 16 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    189.0,
    64.0,
    image=image_image_7
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    294.0,
    64.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#5ECDA5",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=246.0,
    y=48.0,
    width=96.0,
    height=31.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=get_data_from_api,
    relief="flat"
)
button_1.place(
    x=357.0,
    y=48.0,
    width=60.0,
    height=33.0
)

datas = canvas.create_text(
    149.0,
    89.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Inter", 16 * -1)
)

window.after(2000, start_fetching_network)
window.after(0, time_update)
window.resizable(False, False)
window.title('daradege weather app')
window.wm_iconphoto(False,ImageTk.PhotoImage(Image.open(relative_to_assets('image_1.png'))))
window.mainloop()
