import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Scene Manager")

# Function to switch to Scene 1
def show_scene1():
    frame2.pack_forget()  # Hide other frames if visible
    frame1.pack()  # Show Scene 1

# Function to switch to Scene 2
def show_scene2():
    frame1.pack_forget()  # Hide other frames if visible
    frame2.pack()  # Show Scene 2

# Create Scene 1 (Frame)
frame1 = tk.Frame(window, width=400, height=300, bg="lightblue")
label1 = tk.Label(frame1, text="Scene 1", font=("Arial", 24), pady=50)
button1 = tk.Button(frame1, text="Switch to Scene 2", command=show_scene2)

# Create Scene 2 (Frame)
frame2 = tk.Frame(window, width=400, height=300, bg="lightgreen")
label2 = tk.Label(frame2, text="Scene 2", font=("Arial", 24), pady=50)
button2 = tk.Button(frame2, text="Switch to Scene 1", command=show_scene1)

# Place widgets in Scene 1
label1.pack()
button1.pack()

# Place widgets in Scene 2
label2.pack()
button2.pack()

# Display the initial scene
show_scene1()

# Start the Tkinter event loop
window.mainloop()
