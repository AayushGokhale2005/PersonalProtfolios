import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Create an instance of Style
style = Style(theme='superhero')  # Replace 'superhero' with the desired theme name

# Create the main application window
root = style.master
root.title("My Themed Application")
# Add your widgets and application logic here

# Start the main event loop
root.mainloop()
