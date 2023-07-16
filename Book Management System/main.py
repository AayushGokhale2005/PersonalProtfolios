import mysql.connector
import tkinter as tk

# Establish connection for SQL
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
window.config()


#Creating Frames 
menu = tk.Frame(window)
add_books = tk.Frame(window)
search_books = tk.Frame(window)



#functions 
def show_home():
    add_books.pack_forget()
    search_books.pack_forget()
    menu.pack()

def show_books():
    menu.pack_forget()
    add_books.pack()

def show_search():
    menu.pack_forget()
    add_books.pack_forget()
    search_books.pack()


#creating buttons and labels for MENU SCENE
title = tk.Label(menu,text="BOOK MANAGEMENT SYSTEM",font=("Bebas Neue",18),justify="center")
title.grid(row=0,column=0,padx=10,pady=10,)


addBooks = tk.Button(menu,text="ADD BOOKS",command=show_books)
addBooks.grid(row=1,column=0,padx=10,pady=10)

searchBooks = tk.Button(menu,text="SEARCH BOOKS",command=show_search)
searchBooks.grid(row=2,column=0,padx=10,pady=10)

#Creating Buttons and Labels for ADD BOOKS scene
lName = tk.Label(add_books,text="Name of Book : ")
lauthor = tk.Label(add_books,text="Author of Book : ")
Nentry = tk.Entry(add_books)
AuEntry = tk.Entry(add_books)



#Creating Buttons and labels for SEARCH BOOKS scene
test1 = tk.Label(search_books,text="worked")
test1_b = tk.Button(search_books,text="GO BACK",command=show_home)
test1.pack()
test1_b.pack()
show_home()

#app loop
window.mainloop()