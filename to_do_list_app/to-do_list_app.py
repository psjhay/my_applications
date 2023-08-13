import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Load an image for a background
        image = Image.open("background.jpg")  # Replace with your image file
        self.background = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(root, image=self.background)
        self.background_label.place(relwidth=1, relheight=1)

        # Set up header
        self.header_label = tk.Label(root, text="Dashboard To-Do List", font=("Helvetica", 20))
        self.header_label.pack(pady=20)

        # Create task list
        self.task_list = tk.Listbox(root, selectmode=tk.SINGLE, bg="#f0f0f0", bd=0)
        self.task_list.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Create task input field
        self.task_entry = tk.Entry(root, bg="white", font=("Helvetica", 12))
        self.task_entry.pack(padx=20, fill=tk.BOTH)

        # Add Task button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4caf50", fg="white", bd=0)
        self.add_button.pack(padx=20, pady=10, fill=tk.BOTH)

        # Delete Task button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#ff3d00", fg="white", bd=0)
        self.delete_button.pack(padx=20, pady=10, fill=tk.BOTH)

        # Set up initial tasks
        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            index = selected_task[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
