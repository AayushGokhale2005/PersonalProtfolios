import mysql.connector
import tkinter as tk
import random
# Establish connection for SQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aayush12",
    database="bookmanagement"
)
#variables
words = []
book={}
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

def generate_isbn():
    # Generate the first nine digits (excluding check digit)
    digits = random.randint(0,9)
    return digits

def send_books():
    bname = Nentry.get()
    bauthor = AuEntry.get()
    isbn = generate_isbn()
    cursor.execute("INSERT INTO books (ISBN, NAME, AUTHOR) VALUES (%s, %s, %s)", (isbn, bname, bauthor))
    mydb.commit()
    Nentry.delete(0,tk.END)
    AuEntry.delete(0,tk.END)

def display_books():
    cursor.execute("SELECT*FROM books")
    rows = cursor.fetchall()
    display_search_results(rows)

def display_search_results(rows):
    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, f"ISBN: {row[0]}, Name: {row[1]}, Author: {row[2]}")

#creating buttons and labels for MENU SCENE
title = tk.Label(menu,text="BOOK MANAGEMENT SYSTEM",font=("Bebas Neue",18),justify="center")
title.grid(row=0,column=0,padx=10,pady=10,)


addBooks = tk.Button(menu,text="ADD BOOKS",command=show_books)
addBooks.grid(row=1,column=0,padx=10,pady=10)

searchBooks = tk.Button(menu,text="SEARCH BOOKS",command=show_search)
searchBooks.grid(row=2,column=0,padx=10,pady=10)

dispBooks = tk.Button(menu,text="DISPLAY BOOKS")
dispBooks.grid(row=3,column=0,padx=10,pady=10)
#Creating Buttons and Labels for ADD BOOKS scene
lName = tk.Label(add_books,text="Name of Book : ")
lName.grid(row=0,column=0,padx=10,pady=10)

lauthor = tk.Label(add_books,text="Author of Book : ")
lauthor.grid(row=1,column=0,padx=10,pady=10)

Nentry = tk.Entry(add_books)
Nentry.grid(row=0,column=1,padx=10,pady=10)

AuEntry = tk.Entry(add_books)
AuEntry.grid(row=1,column=1,padx=10,pady=10)

sbutton = tk.Button(add_books,text = "SEND DETAILS",command=send_books)
sbutton.grid(row=2,column=1, columnspan=8,padx=10,pady=10)

gback = tk.Button(add_books,text="GO BACK",command=show_home)
gback.grid(row=2,column=0,padx=10,pady=10)

listbox = tk.Listbox(add_books,width=60,justify="center")
listbox.grid(row=3,column=1)

#Creating Buttons and labels for SEARCH BOOKS scene
sbook = tk.Entry(search_books)
sbook.grid(row=0,column=0,padx=10,pady=10)

sbutton = tk.Button(search_books,text="SEARCH BOOKS")
sbutton.grid(row=0,column=1,padx=10,pady=10)

sback = tk.Button(search_books,text="GO BACK",command=show_home)
sback.grid(row=1,column=1,padx=10,pady=10)
show_home()

#app loop
window.mainloop()