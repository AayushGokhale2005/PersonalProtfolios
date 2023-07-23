from tkinter import *
import ttkbootstrap as tb
import tkinter as tk
root = tk.Tk()

style = tb.Style(theme="darkly")  # Create an instance of Style
root = style.master  # Get the main application window
root.title("Test")
root.geometry("500x500")

# functions

# buttons, labels, etc.
label = tb.Label(root, text="test", font=("Arial", 24))  # Create a themed label
label.grid(row=0, column=1, padx=10, pady=10)  # Place the label using grid layout

root.mainloop()
