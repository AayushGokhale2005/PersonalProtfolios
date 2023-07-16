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
    digits = [random.randint(0, 9) for _ in range(9)]
    
    # Calculate the check digit
    check_digit = sum((i + 1) * digits[i] for i in range(9)) % 11
    check_digit = 'X' if check_digit == 10 else str(check_digit)
    
    # Combine the digits and check digit to form the ISBN
    isbn = ''.join(str(digit) for digit in digits) + check_digit
    
    return isbn
def send_books(bname,bauthor):
    #cursor.execute("INSERT INTO books(ISBN, NAME, AUTHOR) VALUES('{0}', '{1}', '{2}')".format(0, bname, bauthor))
    Nentry.delete(0,tk.END)
    AuEntry.delete(0,tk.END)

#creating buttons and labels for MENU SCENE
title = tk.Label(menu,text="BOOK MANAGEMENT SYSTEM",font=("Bebas Neue",18),justify="center")
title.grid(row=0,column=0,padx=10,pady=10,)


addBooks = tk.Button(menu,text="ADD BOOKS",command=show_books)
addBooks.grid(row=1,column=0,padx=10,pady=10)

searchBooks = tk.Button(menu,text="SEARCH BOOKS",command=show_search)
searchBooks.grid(row=2,column=0,padx=10,pady=10)

#Creating Buttons and Labels for ADD BOOKS scene
lName = tk.Label(add_books,text="Name of Book : ")
lName.grid(row=0,column=0,padx=10,pady=10)

lauthor = tk.Label(add_books,text="Author of Book : ")
lauthor.grid(row=1,column=0,padx=10,pady=10)

Nentry = tk.Entry(add_books)
Nentry.grid(row=0,column=1,padx=10,pady=10)

AuEntry = tk.Entry(add_books)
AuEntry.grid(row=1,column=1,padx=10,pady=10)

sbutton = tk.Button(add_books,text = "SEND DETAILS",command=send_books(Nentry.get(),AuEntry.get()))
sbutton.grid(row=2,column=1, columnspan=8,padx=10,pady=10)

gback = tk.Button(add_books,text="GO BACK",command=show_home)
gback.grid(row=2,column=0,padx=10,pady=10)

succLabel = tk.Label(add_books,text="Books Added sucessfully")
succLabel.grid(row=3,column=0,padx=10,pady=10)
#Creating Buttons and labels for SEARCH BOOKS scene
test1 = tk.Label(search_books,text="worked")
test1_b = tk.Button(search_books,text="GO BACK",command=show_home)
test1.pack()
test1_b.pack()
show_home()

#app loop
window.mainloop()