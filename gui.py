import os

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = os.path.dirname(os.path.abspath('__file__'))
ASSETS_PATH = os.path.join(OUTPUT_PATH, os.getcwd(), 'assets', 'frame0')

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)

window = Tk()

window.wm_title("Eternity vpn")
window.geometry("437x626")
window.configure(bg = "#202020")


canvas = Canvas(
    window,
    bg = "#202020",
    height = 626,
    width = 437,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    155.0,
    45.0,
    anchor="nw",
    text="Eternity VPN",
    fill="#FFFFFF",
    font=("Inter Regular", 36 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    78.0,
    69.0,
    image=image_image_1
)

canvas.create_text(
    48.0,
    247.0,
    anchor="nw",
    text="Password",
    fill="#7F7F7F",
    font=("Inter Regular", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    233.0,
    202.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Inter Regular", 15 * -1)
)
entry_1.place(
    x=88.0,
    y=180.0,
    width=300.0,
    height=40.0
)

canvas.create_text(
    48.0,
    144.0,
    anchor="nw",
    text="Username",
    fill="#7F7F7F",
    font=("Inter Regular", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    233.0,
    305.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    show="*",
    font=("Inter Regular", 15 * -1)
)
entry_2.place(
    x=88.0,
    y=283.0,
    width=300.0,
    height=40.0
)


canvas.create_text(
    27.0,
    393.0,
    anchor="nw",
    text="Status",
    fill="#FFFFFF",
    font=("Inter Regular", 15 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    196.0,
    491.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    169.0,
    438.0,
    image=image_image_3
)

canvas.create_text(
    27.0,
    483.0,
    anchor="nw",
    text="Traffic",
    fill="#817E7E",
    font=("Inter Regular", 13 * -1)
)

canvas.create_text(
    27.0,
    431.0,
    anchor="nw",
    text="Ip address",
    fill="#817E7E",
    font=("Inter Regular", 13 * -1)
)


status=canvas.create_text(
    119.0,
    393.0,
    anchor="nw",
    text="......................",
    fill="#817E7E",
    font=("Inter Regular", 13 * -1)
)

message=canvas.create_text(
    107,
    539.0,
    anchor="nw",
    width=291,
    text="",
    fill="#FFFFFF",
    font=("Inter Regular", 13 * -1)
)
ip_=canvas.create_text(
    119.0,
    430.0,
    anchor="nw",
    text="_._._._",
    fill="#000000",
    font=("Inter Regular", 13 * -1)
)

traffic=canvas.create_text(
    119.0,
    483.0,
    anchor="nw",
    text="0.00 B/s ⬇ 0.00 B/s ⬆",
    fill="#000000",
    font=("Inter Regular", 13 * -1)
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_1.place(
    x=275.0,
    y=386.0,
    width=123.0,
    height=38.0
)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))

button_image_hover_con = PhotoImage(
    file=relative_to_assets("button_1_hover_con.png"))

button_image_hover_dis = PhotoImage(
    file=relative_to_assets("button_1_hover_dis.png"))


