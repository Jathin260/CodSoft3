import tkinter as tk
import random
import string

#Character
CHARACTERS = string.ascii_letters + string.digits + string.punctuation

def generate_password():
    # Clear previous password
    result_entry.delete(0, tk.END)
    try:
        length = int(entry_length.get())
        if length <= 0:
            result_entry.insert(0, "Length must be greater than 0")
            return

        # Generate the password
        password = ''.join(random.choices(CHARACTERS, k=length))
        result_entry.insert(0, password)
    except ValueError:
        result_entry.insert(0, "Invalid input! Please enter a number.")

# Main window
root = tk.Tk()
root.title("Password Generator")

# Frame setup
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Password length input
tk.Label(frame, text="Password Length:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_length = tk.Entry(frame, width=10)
entry_length.grid(row=0, column=1, padx=5, pady=5)

# Generate button
generate_button = tk.Button(frame, text="Generate", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Display generated password
result_entry = tk.Entry(frame, width=40, state="normal")
result_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
root.mainloop()