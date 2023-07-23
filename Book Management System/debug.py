import tkinter as tk
import mysql.connector

# Function to add a book to the database
def add_book():
    isbn = entry_isbn.get()
    name = entry_name.get()
    author = entry_author.get()
    cursor.execute("INSERT INTO books (ISBN, NAME, AUTHOR) VALUES (%s, %s, %s)", (isbn, name, author))
    connection.commit()
    clear_fields()
    display_books()

# Function to search books by name or author
def search_books():
    keyword = entry_search.get()
    cursor.execute("SELECT * FROM books WHERE NAME LIKE %s OR AUTHOR LIKE %s", ('%' + keyword + '%', '%' + keyword + '%'))
    rows = cursor.fetchall()
    display_search_results(rows)

# Function to display all books in the database
def display_books():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    display_search_results(rows)

# Function to display search results in the ListBox
def display_search_results(rows):
    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, f"ISBN: {row[0]}, Name: {row[1]}, Author: {row[2]}")

# Function to delete the selected book from the database
def delete_book():
    selected_item = listbox.curselection()
    if selected_item:
        isbn = listbox.get(selected_item)[6:16]  # Extract the ISBN from the ListBox item
        cursor.execute("DELETE FROM books WHERE ISBN=%s", (isbn,))
        connection.commit()
        display_books()

# Function to clear the entry fields
def clear_fields():
    entry_isbn.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_search.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Book Management System")

# Create the database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aayush12",
    database="bookmanagement"
)
cursor = connection.cursor()

# Create the table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS books (ISBN VARCHAR(255), NAME VARCHAR(255), AUTHOR VARCHAR(255))")

# Create the entry fields and labels
label_isbn = tk.Label(window, text="ISBN")
label_isbn.grid(row=0, column=0)
entry_isbn = tk.Entry(window)
entry_isbn.grid(row=0, column=1)

label_name = tk.Label(window, text="Name")
label_name.grid(row=1, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=1, column=1)

label_author = tk.Label(window, text="Author")
label_author.grid(row=2, column=0)
entry_author = tk.Entry(window)
entry_author.grid(row=2, column=1)

# Create the buttons
button_add = tk.Button(window, text="Add Book", command=add_book)
button_add.grid(row=3, column=0, columnspan=2, pady=10)

button_search = tk.Button(window, text="Search", command=search_books)
button_search.grid(row=4, column=0, columnspan=2)

button_view_all = tk.Button(window, text="View All Books", command=display_books)
button_view_all.grid(row=5, column=0, columnspan=2, pady=10)

button_delete = tk.Button(window, text="Delete Book", command=delete_book)
button_delete.grid(row=6, column=0, columnspan=2)

# Create the search entry field and ListBox
label_search = tk.Label(window, text="Search by Name or Author")
label_search.grid(row=7, column=0, columnspan=2)

entry_search = tk.Entry(window)
entry_search.grid(row=8, column=0, columnspan=2)

listbox = tk.Listbox(window, width=60)
listbox.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Display all books initially
display_books()

# Run the Tkinter event loop
window.mainloop()

# Close the database connection when the application is closed
connection.close()
