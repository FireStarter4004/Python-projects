#Kyler Brungerwood
#To-do list application
#the start date is 12/7/2025

import tkinter as tk
from tkinter import messagebox
import json as js




root=tk.Tk()
root.geometry("400x600")
root.configure(bg="purple")

def myGUI ():
    root.title("to-do list")
    titlelabel=tk.Label(root, text="to-do list", bg="white", fg="black", font=("Arial", 24))
    titlelabel.pack(pady=10)
    titlelabel2=tk.Label(root, text="for Kyler Brungerwood", bg="white", fg="black", font=("Arial", 14))
    titlelabel2.pack(pady=5)
    taskslabel=tk.Label(root, text="daily tasks", bg="purple", fg="black", font=("Arial", 18,"underline"))
    taskslabel.pack(pady=5)
    taskentry=tk.Entry(root, width=30, font=("Arial", 14))
    taskentry.pack(side="bottom", pady=30)
    taskentry.insert(0, "enter a new task  :")


myGUI()
root.mainloop()