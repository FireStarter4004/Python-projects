
import tkinter as tk
from tkinter import messagebox
import json as js
import To_do_list as tdl

tasks=open("tasks.txt")
listoftasks=tasks.readlines()


def add_task(task_listbox, task_entry):
    task_text = task_entry.get()
    if task_text:
        tasks=open("tasks.txt","a")
        tasks.write(task_text.strip("enter a new task  :") + "\n")
        tasks.close()
        task_listbox.insert(tk.END, task_text)

        task_entry.delete(0, tk.END)
        #task_entry.insert(0, "enter a new task  :")
  