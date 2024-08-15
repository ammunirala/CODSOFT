import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    # Define character sets
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all selected character sets
    all_chars = lower_chars + upper_chars + digits + special_chars
    
    # Ensure there are characters to choose from
    if not all_chars:
        raise ValueError("At least one character set must be selected.")
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()
        
        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        password_entry.config(state=tk.NORMAL)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state=tk.DISABLED)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Initialize the main application window
app = tk.Tk()
app.title("Password Generator")

# Create and place widgets
tk.Label(app, text="Length:").grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(app)
length_entry.grid(row=0, column=1, padx=10, pady=5)
length_entry.insert(0, "12")

uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(app, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, column=0, columnspan=2, padx=10, pady=5)

digits_var = tk.BooleanVar(value=True)
tk.Checkbutton(app, text="Include Digits", variable=digits_var).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

special_chars_var = tk.BooleanVar(value=True)
tk.Checkbutton(app, text="Include Special Characters", variable=special_chars_var).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

tk.Button(app, text="Generate Password", command=on_generate).grid(row=4, column=0, columnspan=2, pady=10)

tk.Label(app, text="Generated Password:").grid(row=5, column=0, padx=10, pady=5)
password_entry = tk.Entry(app, width=50, state=tk.DISABLED)
password_entry.grid(row=5, column=1, padx=10, pady=5)

# Start the GUI event loop
app.mainloop()