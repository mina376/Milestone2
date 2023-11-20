# Ian Flynn
# Varikeel
# CS 361
# Program handles a task management system

import tkinter as tk
from tkinter import messagebox
# ----------------------------------------------------------------------------------
import requests
# ----------------------------------------------------------------------------------

def save_tasks():
    """Saves tasks to text file"""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task[0]},{task[1]},{task[2]},{task[3]}\n")

def validate_date_input(P):
    """Validate date input"""
    if P == "" or (not any(char.isalpha() for char in P)):
        return True
    return False


def add_task_popup():
    """Handles the task popup"""
    popup = tk.Toplevel(root)
    popup.title("Add Task")
    # Title Bar
    task_name_label = tk.Label(
        popup, text="*Name for task:", font=("Arial", 12))
    task_name_label.grid(row=0, column=0, padx=10, pady=5)
    task_name_entry = tk.Entry(popup, font=("Arial", 12))
    task_name_entry.grid(row=0, column=1, padx=10, pady=5)
    # Date Bar
    task_date_label = tk.Label(
        popup, text="Date (Optional):", font=("Arial", 12))
    task_date_label.grid(row=1, column=0, padx=10, pady=5)
    date_validation = root.register(validate_date_input)
    task_date_entry = tk.Entry(popup, font=(
        "Arial", 12), validate="key", validatecommand=(date_validation, "%P"))
    task_date_entry.grid(row=1, column=1, padx=10, pady=5)
    # Note Bar
    task_note_label = tk.Label(
        popup, text="Would you like to add a note? (You can add one later!):", font=("Arial", 12))
    task_note_label.grid(row=2, column=0, padx=10, pady=5)
    task_note_entry = tk.Entry(popup, font=("Arial", 12))
    task_note_entry.grid(row=2, column=1, padx=10, pady=5)
    # Confirmation
    confirm_button = tk.Button(popup, text="Confirm", command=lambda: save_new_task(
        popup, task_name_entry, task_date_entry, task_note_entry), font=("Arial", 12))
    confirm_button.grid(row=3, column=0, columnspan=2, pady=10)
    # Cancel
    cancel_button = tk.Button(popup, text="Cancel",
                              command=popup.destroy, font=("Arial", 12))
    cancel_button.grid(row=4, column=0, columnspan=2, pady=5)


def save_new_task(popup, task_name_entry, task_date_entry, task_note_entry):
    """Saves the task to the list"""
    task_name = task_name_entry.get()
    task_date = task_date_entry.get()
    task_note = task_note_entry.get()
    # Adds task information
    if task_name:
        if not task_date:
            task_date = ""
        if not task_note:
            task_note = ""
        tasks.append((task_name, task_date, task_note, False))
        save_tasks()
        update_task_list(tasks)
        popup.destroy()
    else:
        messagebox.showwarning("Incomplete Information",
                               "Please enter the task name.")


def delete_task(index):
    """Handles deleting a task"""
    confirm = messagebox.askyesno(
        "Confirm Deletion", "Are you sure you want to delete this task?")
    if confirm:
        tasks.pop(index)
        save_tasks()
        update_task_list(tasks)


def toggle_completion(index):
    """Handles task completion checking"""
    tasks[index] = (tasks[index][0], tasks[index][1],
                    tasks[index][2], not tasks[index][3])
    save_tasks()
    update_task_list(tasks)


def edit_task(index):
    """Edits a task"""
    def update_task(popup, task_name_entry, task_date_entry, task_note_entry):
        """Helper to update an edited task"""
        task_name = task_name_entry.get()
        task_date = task_date_entry.get()
        task_note = task_note_entry.get()
        # Edit task info
        if task_name:
            if not task_date:
                task_date = ""
            if not task_note:
                task_note = ""
            tasks[index] = (task_name, task_date, task_note, tasks[index][3])
            save_tasks()
            update_task_list(tasks)
            popup.destroy()
        else:
            messagebox.showwarning(
                "Incomplete Information", "Please enter the task name.")
    # Handles edit pop-up
    popup = tk.Toplevel(root)
    popup.title("Edit Task")
    # Title
    task_name_label = tk.Label(
        popup, text="Edit task name:", font=("Arial", 12))
    task_name_label.grid(row=0, column=0, padx=10, pady=5)
    task_name_entry = tk.Entry(popup, font=("Arial", 12))
    task_name_entry.grid(row=0, column=1, padx=10, pady=5)
    # Date
    task_date_label = tk.Label(popup, text="Edit date:", font=("Arial", 12))
    task_date_label.grid(row=1, column=0, padx=10, pady=5)
    date_validation = root.register(validate_date_input)
    task_date_entry = tk.Entry(popup, font=(
        "Arial", 12), validate="key", validatecommand=(date_validation, "%P"))
    task_date_entry.grid(row=1, column=1, padx=10, pady=5)
    # Note
    task_note_label = tk.Label(
        popup, text="Edit the note:", font=("Arial", 12))
    task_note_label.grid(row=2, column=0, padx=10, pady=5)
    task_note_entry = tk.Entry(popup, font=("Arial", 12))
    task_note_entry.grid(row=2, column=1, padx=10, pady=5)
    task_name_entry.insert(0, tasks[index][0])
    task_date_entry.insert(0, tasks[index][1])
    task_note_entry.insert(0, tasks[index][2])
    # Confirm
    confirm_button = tk.Button(popup, text="Confirm", command=lambda: update_task(
        popup, task_name_entry, task_date_entry, task_note_entry), font=("Arial", 12))
    confirm_button.grid(row=3, column=0, columnspan=2, pady=10)
    # Cancel
    cancel_button = tk.Button(popup, text="Cancel",
                              command=popup.destroy, font=("Arial", 12))
    cancel_button.grid(row=4, column=0, columnspan=2, pady=5)


def update_task_list(task_list):
    """Updates task list"""
    for widget in task_frame.winfo_children():
        widget.destroy()
    # Task titles
    task_name_title = tk.Label(
        task_frame, text="Task Name", font=("Arial", 14, "bold"))
    task_name_title.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    task_date_title = tk.Label(
        task_frame, text="Date", font=("Arial", 14, "bold"))
    task_date_title.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    task_note_title = tk.Label(
        task_frame, text="Note", font=("Arial", 14, "bold"))
    task_note_title.grid(row=0, column=3, padx=10, pady=5, sticky="w")
    task_completed_title = tk.Label(
        task_frame, text="Completed", font=("Arial", 14, "bold"))
    task_completed_title.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    # Task list
    for i, task in enumerate(task_list):
        task_completed_checkbox = tk.Checkbutton(
            task_frame, variable=task[0], command=lambda i=i: toggle_completion(i))
        task_completed_checkbox.grid(
            row=i + 1, column=0, padx=10, pady=5, sticky="w")
        task_name_label = tk.Label(
            task_frame, text=task[0], font=("Arial", 12))
        task_name_label.grid(row=i + 1, column=1, padx=10, pady=5, sticky="w")
        task_date_label = tk.Label(
            task_frame, text=task[1], font=("Arial", 12))
        task_date_label.grid(row=i + 1, column=2, padx=10, pady=5, sticky="w")
        task_note_label = tk.Label(
            task_frame, text=task[2], font=("Arial", 12))
        task_note_label.grid(row=i + 1, column=3, padx=10, pady=5, sticky="w")
        # Trash icon
        trash_button = tk.Button(
            task_frame, text="🗑", command=lambda i=i: delete_task(i), font=("Arial", 12))
        trash_button.grid(row=i + 1, column=4, padx=10, pady=5, sticky="w")
        # Edit icon
        edit_button = tk.Button(
            task_frame, text="✎", command=lambda i=i: edit_task(i), font=("Arial", 12))
        edit_button.grid(row=i + 1, column=5, padx=10, pady=5, sticky="w")


def search_tasks():
    """Searches for tasks"""
    query = search_entry.get().lower()
    filter_text = filter_var.get().lower()
    filtered_tasks = []
    # Search
    for task in tasks:
        task_name = task[0].lower()
        task_note = task[2].lower()
        # Filter for completion
        if (filter_text == "all" or (filter_text == "completed" and task[3]) or (filter_text == "incomplete" and not task[3])):
            if query in task_name:
                filtered_tasks.append(task)
    update_search_results(filtered_tasks)


def update_search_results(task_list):
    """Updates tasks on search page"""
    for widget in search_results_frame.winfo_children():
        widget.destroy()
    # Task Titles
    task_name_title = tk.Label(
        search_results_frame, text="Task Name", font=("Arial", 14, "bold"))
    task_name_title.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    task_date_title = tk.Label(
        search_results_frame, text="Date", font=("Arial", 14, "bold"))
    task_date_title.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    task_note_title = tk.Label(
        search_results_frame, text="Note", font=("Arial", 14, "bold"))
    task_note_title.grid(row=0, column=3, padx=10, pady=5, sticky="w")
    task_completed_title = tk.Label(
        search_results_frame, text="Completed", font=("Arial", 14, "bold"))
    task_completed_title.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    # Task list
    for i, task in enumerate(task_list):
        task_completed_checkbox = tk.Checkbutton(
            search_results_frame, variable=task[0], command=lambda i=i: toggle_completion(i))
        task_completed_checkbox.grid(
            row=i + 1, column=0, padx=10, pady=5, sticky="w")
        task_name_label = tk.Label(
            search_results_frame, text=task[0], font=("Arial", 12))
        task_name_label.grid(row=i + 1, column=1, padx=10, pady=5, sticky="w")
        task_date_label = tk.Label(
            search_results_frame, text=task[1], font=("Arial", 12))
        task_date_label.grid(row=i + 1, column=2, padx=10, pady=5, sticky="w")
        task_note_label = tk.Label(
            search_results_frame, text=task[2], font=("Arial", 12))
        task_note_label.grid(row=i + 1, column=3, padx=10, pady=5, sticky="w")
        # Trash icon
        trash_button = tk.Button(search_results_frame, text="🗑",
                                 command=lambda i=i: delete_task(i), font=("Arial", 12))
        trash_button.grid(row=i + 1, column=4, padx=10, pady=5, sticky="w")
        # Edit icon
        edit_button = tk.Button(search_results_frame, text="✎",
                                command=lambda i=i: edit_task(i), font=("Arial", 12))
        edit_button.grid(row=i + 1, column=5, padx=10, pady=5, sticky="w")


def switch_to_home():
    """Handles switching to home page"""
    search_frame.grid_forget()
    search_results_frame.grid_forget()
    task_frame.grid(row=1, column=0)
    update_task_list(tasks)


def switch_to_search():
    """Handles switch to search page"""
    task_frame.grid_forget()
    search_results_frame.grid(row=1, column=0)
    search_frame.grid(row=2, column=0)
    # Search button
    search_button = tk.Button(
        search_frame, text="Search", command=search_tasks, font=("Arial", 12))
    search_button.grid(row=0, column=4)
    search_tasks()


# ----------------------------------------------------------------------------------
def import_tasks_from_microservice():
    response = requests.get("http://localhost:5001/import_tasks")
    data = response.json()
    return data["tasks"]


def export_tasks_to_microservice(tasks):
    payload = {"tasks": tasks}
    response = requests.post("http://localhost:5001/export_tasks", json=payload)
    data = response.json()
    print(data["message"])


tasks = import_tasks_from_microservice()


def save_tasks():
    export_tasks_to_microservice(tasks)
# ----------------------------------------------------------------------------------


# Initialize Main
root = tk.Tk()
root.title("Task Manager")

# Default window size
root.geometry("900x900")

# Store tasks
tasks = []

# Frame for task list
task_frame = tk.Frame(root)
task_frame.grid(row=1, column=0)

# Home page button
home_button = tk.Button(
    root, text="Home", command=switch_to_home, font=("Arial", 14))
home_button.grid(row=4, column=0, padx=10, pady=20, sticky="sw")

# Adding task button
add_task_button = tk.Button(
    root, text="+", font=("Arial", 20), command=add_task_popup)
add_task_button.grid(row=3, column=2, padx=20, pady=20, sticky="se")

# Search page button
search_button = tk.Button(
    root, text="Search", command=switch_to_search, font=("Arial", 14))
search_button.grid(row=4, column=2, padx=10, pady=20, sticky="se")

# Search results frame
search_results_frame = tk.Frame(root)

# Create a frame for the search bar and filter
search_frame = tk.Frame(root)
search_frame.grid_forget()

# Search labels
search_label = tk.Label(search_frame, text="Search", font=("Arial", 12))
search_label.grid(row=0, column=0, sticky="w")
search_entry = tk.Entry(search_frame, font=("Arial", 12))
search_entry.grid(row=0, column=1)

# Dropdown filter and options
filter_label = tk.Label(search_frame, text="Filter", font=("Arial", 12))
filter_label.grid(row=0, column=2, sticky="w")
filter_options = ["All", "Completed", "Incomplete"]
filter_var = tk.StringVar()
filter_var.set(filter_options[0])
filter_menu = tk.OptionMenu(search_frame, filter_var, *filter_options)
filter_menu.grid(row=0, column=3)

# Intialize home page
switch_to_home()

# Run
root.mainloop()
