#importing all neccessory libraries
import tkinter as tk
import mysql.connector
#creating mysql connection
sql = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd="aayush12",
    database="expensemanager"
)
cursor = sql.cursor()
#global variables 
categories = ["Food", "Transportation", "Housing", "Entertainment", "Utilities", "Others"]
curUser = ''
#creating application window
window = tk.Tk()
window.geometry("500x500")
window.title("Expense tracker 1.0")
#creating frames
login = tk.Frame(window)
menu = tk.Frame(window)
newuser = tk.Frame(window)
addincome = tk.Frame(window)
# Variable to store the selected category
selected_category_var = tk.StringVar()
selected_category_var.set(categories[0])  # Set the default category as the first one in the list
#functions
def show_login():
    login.pack()
    menu.pack_forget()
    newuser.pack_forget()
def show_menu():
   login.pack_forget()
   menu.pack()

def new_user():
    login.pack_forget()
    menu.pack_forget()
    newuser.pack()

def show_addincome():
    login.pack_forget()
    menu.pack_forget()
    newuser.pack_forget()
    addincome.pack()

def record_new_data():
    name = nameData.get()
    passw = passwordData.get()
    cursor.execute("INSERT INTO userdata VALUES(%s,%s)",(name,passw))
    sql.commit()
    print("data Added !")
    nameData.delete(0,tk.END)
    passwordData.delete(0,tk.END)


def show_menu():
    username.pack_forget()
    login.pack_forget()
    newuser.pack_forget()
    menu.pack()
def user_login():
    cursor.execute("SELECT*FROM userdata")
    row = cursor.fetchall()
    
    for data in row:
        if data[0] == username.get() and data[1]==passwd.get():
            curUser=data[0]
            show_addincome()   
    username.delete(0,tk.END)
    passwd.delete(0,tk.END)

def add_income(event):
    # Clear the contents of the table_display Listbox before updating
    table_display.delete(0, tk.END)
    selected_category = selected_category_var.get()
    cursor.execute("SELECT*FROM expenses")
    row = cursor.fetchall()
    for data in row:
        table_display.insert(tk.END,"Category: {} MoneySpent : {}".format(data[0],data[1]))
    spent()

def insert_expense():
    selected_category = selected_category_var.get()
    amount_spent = menu_spent.get()
    cursor.execute("INSERT INTO expenses (category, expense) VALUES (%s, %s)", (selected_category, amount_spent))
    sql.commit()

def delete():
    cursor.execute("DELETE FROM expenses")

def spent():
    cursor.execute("SELECT*FROM expenses")
    row = cursor.fetchall()
    sum=0
    for data in row:
        sum = sum +int(data[1])
        money_spent.config(text="Money Spent : {}".format(sum))
#Creating Buttons , labels etc for --> login
welcomeMessage = tk.Label(login,text="Expense Tracker",font=("Bebas Neue",24))
welcomeMessage.grid(row=0,column=1,padx=10,pady=10)


USER_TEXT = tk.Label(login,text="Username:")
USER_TEXT.grid(row=1,column=0)
username = tk.Entry(login)
username.grid(row=1,column=1,padx=10,pady=10)


PASSWD_TEXT = tk.Label(login,text="Password:")
PASSWD_TEXT.grid(row=2,column=0)
passwd = tk.Entry(login)
passwd.grid(row=2,column=1,padx=10,pady=10)

loginButton = tk.Button(login,text="LOGIN",command=user_login)
loginButton.grid(row=3,column=1,padx=5,pady=10)

registerButton = tk.Button(login,text="NEW USER",command=new_user)
registerButton.grid(row=3,column=0,padx=5,pady=10)


#Creating buttons , labels ec for ---> newUser
name = tk.Label(newuser,text="Name:")
name.grid(row=0,column=0,padx=10,pady=10)


nameData = tk.Entry(newuser)
nameData.grid(row=0,column=1,padx=10,pady=10)

password = tk.Label(newuser,text="Password")
password.grid(row=1,column=0,padx=10,pady=10)

passwordData = tk.Entry(newuser)
passwordData.grid(row=1,column=1,padx=10,pady=10)

register = tk.Button(newuser,text="REGISTER",command=record_new_data)
register.grid(row=2,column=0)

goback = tk.Button(newuser,text="GO BACK",command=show_login)
goback.grid(row=2,column=1)



#Creating buttons , widgets etc for --> Add income
label_addincome = tk.Label(addincome,text="Add Expense",font=("Babas Neue",24))
label_addincome.grid(row=0,column=0,padx=10,pady=10)

menu_addincome = tk.OptionMenu(addincome,selected_category_var,*categories)
menu_addincome.grid(row=1,column=0,padx=10,pady=10)
menu_addincome.bind('<Configure>',add_income)


menu_spent = tk.Entry(addincome)
menu_spent.grid(row=1,column=1,padx=10,pady=10)

menu_send = tk.Button(addincome,text="ADD TO TABLE",command=insert_expense)
menu_send.grid(row=1,column=2,padx=10,pady=10)

table_display = tk.Listbox(addincome,width=60,justify="center")
# Creating a scrollbar for the listbox
scrollbar = tk.Scrollbar(addincome, orient=tk.VERTICAL, command=table_display.yview)
scrollbar.grid(row=2, column=4, rowspan=2, sticky="ns")

# Configure the listbox to use the scrollbar
table_display.config(yscrollcommand=scrollbar.set)

table_display.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

clear = tk.Button(addincome,text="CLEAR",command=lambda:table_display.delete(0,tk.END))
clear.grid(row=3,column=0,padx=10,pady=10)
perma_delete = tk.Button(addincome,text="DELETE ALL DATA",command=delete)
perma_delete.grid(row=3,column=1,padx=10,pady=10)

money_spent = tk.Label(addincome,text='Money spent : 0 ',font=("Babas Neue",18))
money_spent.grid(row=4,column=0,padx=10,pady=10)
#App loop 
show_login()
window.mainloop()