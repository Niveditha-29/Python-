import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import backend  # Assume backend.py contains database functions above

def add_item():
    name = entry_name.get()
    category = entry_category.get()
    quantity = entry_quantity.get()
    expiry = entry_expiry.get()
    purchase = datetime.today().strftime("%Y-%m-%d")
    
    backend.add_food(name, category, quantity, purchase, expiry)
    messagebox.showinfo("Success", f"{name} added successfully!")
    entry_name.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_expiry.delete(0, tk.END)

root = tk.Tk()
root.title("Food Expiry Alert System")
root.geometry("400x300")

tk.Label(root, text="Food Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Category").pack()
entry_category = tk.Entry(root)
entry_category.pack()

tk.Label(root, text="Quantity").pack()
entry_quantity = tk.Entry(root)
entry_quantity.pack()

tk.Label(root, text="Expiry Date (YYYY-MM-DD)").pack()
entry_expiry = tk.Entry(root)
entry_expiry.pack()

tk.Button(root, text="Add Food Item", command=add_item).pack(pady=20)

root.mainloop()
