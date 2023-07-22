import tkinter as tk

def on_category_select(event):
    selected_category = selected_category_var.get()
    # Add your code here to perform actions based on the selected category
    print(f"Selected category: {selected_category}")

# Define the list of categories
categories = ["Food", "Transportation", "Housing", "Entertainment", "Utilities", "Others"]

# Create the main application window
root = tk.Tk()
root.title("Expense Manager")

# Variable to store the selected category
selected_category_var = tk.StringVar()
selected_category_var.set(categories[0])  # Set the default category as the first one in the list

# Create the label for the dropdown menu
label_category = tk.Label(root, text="Select Category:")
label_category.pack()

# Create the dropdown menu
category_dropdown = tk.OptionMenu(root, selected_category_var, *categories)
category_dropdown.pack()

# Bind the function to the dropdown menu
category_dropdown.bind("<Configure>", on_category_select)

# Run the Tkinter main loop
root.mainloop()
