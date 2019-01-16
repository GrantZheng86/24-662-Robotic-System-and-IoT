'''
Created on Jan 15, 2019

@author: Grant Zheng
'''

import tkinter as tk
from tkinter import DoubleVar

tempC = None
tempF = None

def convert():
    global tempC
    global tempF
    
    try:
        userInput = tempF.get()
        converted = (userInput - 32) * 5.0 / 9.0
        tempC.set(converted)
    except:
        pass
    
master = tk.Tk()
master.title("Temperature Unit Conversion")

tempC = DoubleVar()
tempF = DoubleVar()

userF = tk.Entry(master, textvariable = tempF)
labelUI = tk.Label(master, text = "Enter Degree in F")
labelResult = tk.Label(master, text = " Result")
labelC = tk.Label(master, textvariable = tempC)
button = tk.Button(master, text = "convert", command = convert)

labelUI.grid(row = 0)
userF.grid(row = 0, column = 1)
labelResult.grid(row = 1, column = 0)
labelC.grid(row = 1, column = 1)
button.grid(row = 2, columnspan = 4)

master.mainloop()