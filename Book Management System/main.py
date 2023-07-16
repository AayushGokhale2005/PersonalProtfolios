import mysql.connector
import tkinter as tk

# Establish connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aayush12",
    database="bookmanagement"
)
#variables
words = []
# Create cursor
cursor = mydb.cursor()
#creating tkinter window
window = tk.Tk()
window.geometry("500x500")
window.title("BOOK MANAGEMENT SYSTEM")
#creating buttons and labels
entry = tk.Entry(window)
entry.grid(row=0,column=1,padx=10,pady=10)
buttons = tk.Button(window, text="ENTER", command=lambda: print("worked") if entry.get() == "69" else None)
buttons.grid(row=0,column=2,padx=10,pady=10)



#app loop
window.mainloop()