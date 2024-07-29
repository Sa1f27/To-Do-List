import tkinter as tk
from tkinter import font

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.config(bg="lightblue")

# Defining fonts and colors
header_font = font.Font(family="Helvetica", size=16, weight="bold")
task_font = font.Font(family="Arial", size=12)
button_font = font.Font(family="Helvetica", size=12, weight="bold")

header_bg = "darkblue"
header_fg = "white"
button_bg = "darkblue"
button_fg = "white"
listbox_bg = "white"
listbox_fg = "black"

# creating and placing the header label
header = tk.Label(root, text="To-Do List", bg=header_bg, fg=header_fg, font=header_font)
header.pack(pady=10)

# frame for adding tasks
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=25, font=task_font)
task_entry.grid(row=0, column=0, padx=10)

add_button = tk.Button(frame, text="Add Task", bg=button_bg, fg=button_fg, font=button_font, command=lambda: adding_task())
add_button.grid(row=0, column=1)

# listbox to display tasks
listbox = tk.Listbox(root, width=50, height=10, bg=listbox_bg, fg=listbox_fg, font=task_font, selectbackground="lightgray")
listbox.pack(pady=10)

# the delete button
delete_button = tk.Button(root, text="Delete Task", bg=button_bg, fg=button_fg, font=button_font, command=lambda: delete_task())
delete_button.pack(pady=5)

# the update button
update_button = tk.Button(root, text="Update Task", bg=button_bg, fg=button_fg, font=button_font, command=lambda: update_task())
update_button.pack(pady=5)

# the close button
close_button = tk.Button(root, text="Close", bg=button_bg, fg=button_fg, font=button_font, command=root.destroy)
close_button.pack(pady=5)

# Function to add a task
def adding_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

# Function to update the selected task
def update_task():
    try:
        selected_task_index = listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
    except IndexError:
        pass

# Fill the entry with the selected task when double-clicked
def fill_task_entry(event):
    try:
        selected_task_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_task_index)
        task_entry.delete(0, tk.END)
        task_entry.insert(0, selected_task)
    except IndexError:
        pass

listbox.bind('<Double-1>', fill_task_entry)

root.mainloop()
