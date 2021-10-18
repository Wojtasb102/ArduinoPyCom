import serial
import time
from  tkinter import *

root = Tk()

canvas = Canvas(root, width = 400, height = 300)
canvas.grid()
ser = serial.Serial('COM3', 9600)


def led_on_off():
    user_input = input("\n Wpisz on / off/ quit: ")
    if user_input == "on":
        print ("zapalono diode")
        time.sleep(0.1)
        ser.write(b'H')
    elif user_input == "off":
        print("zgaszono")
        time.sleep(0.1)
        ser.write(b'L')
    elif user_input=="quit":
        print("nara")
        time.sleep(0.1)
        ser.write(b'H')
        ser.close()
    else:
        print("Coś nie halo")


def led_on():
    print("zapalono diode")
    time.sleep(0.1)
    ser.write(b'H')


def led_off():
    print("Zgaszono diode")
    time.sleep(0.1)
    ser.write(b'L')


onButton = Button(root,text= "On", command=led_on)
offButton = Button(root, text = "Off", command=led_off)
onButton.grid(row=0, column=0)
offButton.grid(row=1, column=0)




root.mainloop()