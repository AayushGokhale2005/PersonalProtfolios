import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("BASIC CALCULATOR")

# Create the entry widget for displaying the numbers
entry = tk.Entry(root, width=25, justify="left")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to handle the equal button
def button_equal():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

# Create number buttons
for i in range(9):
    button = tk.Button(root, text=str(i+1), padx=20, pady=10, command=lambda num=i+1: button_click(num))
    button.grid(row=i//3+1, column=i%3, padx=5, pady=5)

# Create operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(root, text=operator, padx=20, pady=10, command=lambda op=operator: button_click(op))
    button.grid(row=i+1, column=3, padx=5, pady=5)

# Create the equal button
equal_button = tk.Button(root, text="=", padx=20, pady=10, command=button_equal)
equal_button.grid(row=4, column=2, padx=5, pady=5)

# Create the clear button
clear_button = tk.Button(root, text="AC", padx=20, pady=10, command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=4, column=0, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
