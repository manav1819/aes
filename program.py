import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font

# Importing different functionalities
from decryption import decrypt
from encryption import encrypt
from hex_expression_evaluator import evaluate_expression
from poly_addition import xor_hex_mod_11b
from poly_multiplication import gf2_multiply_and_mod

# Function: Handle Addition
def handle_addition():
    hex1 = normal_hex1.get().strip()
    hex2 = normal_hex2.get().strip()

    try:
        result = xor_hex_mod_11b(hex1, hex2)
        normal_result.set(result)
    except Exception as e:
        messagebox.showerror("Error", f"Addition failed: {e}")


# Function: Handle Multiplication
def handle_multiplication():
    hex1 = normal_hex1.get().strip()
    hex2 = normal_hex2.get().strip()

    try:
        result = gf2_multiply_and_mod(hex1, hex2)
        normal_result.set(result)
    except Exception as e:
        messagebox.showerror("Error", f"Multiplication failed: {e}")


# Function: Handle Decryption
def handle_decryption():
    ciphertext = decrypt_ciphertext.get().strip()
    round_key = decrypt_round_key.get().strip()

    if len(ciphertext) != 32 or len(round_key) != 32:
        messagebox.showerror("Error", "Ciphertext and Round Key must be 32 hex characters long!")
        return

    hex_result, ascii_result = decrypt(ciphertext, round_key)
    if hex_result and ascii_result:
        decrypt_result_hex.set(hex_result)
        decrypt_result_ascii.set(ascii_result)

# Main Window
root = tk.Tk()
root.title("Polynomial Arithmetic in GF(2^8)")
root.geometry("800x500")

# Define custom font sizes
default_font = font.Font(family="Helvetica", size=18)  # Default font
header_font = font.Font(family="Helvetica", size=22, weight="bold")  # Headers
input_font = font.Font(family="Helvetica", size=20)  # Input fields

# Toolbar with Menus
menu_bar = tk.Menu(root)

# Preferences Menu
def preferences_action():
    messagebox.showinfo("Preferences", "Preferences are currently under development.")

preferences_menu = tk.Menu(menu_bar, tearoff=0)
preferences_menu.add_command(label="Edit Preferences", command=preferences_action)
menu_bar.add_cascade(label="Preferences", menu=preferences_menu)

# Themes Menu
def apply_theme(theme_name):
    if theme_name == "Light":
        root.configure(bg="white")
    elif theme_name == "Dark":
        root.configure(bg="black")
    messagebox.showinfo("Theme Applied", f"{theme_name} theme has been applied!")

themes_menu = tk.Menu(menu_bar, tearoff=0)
themes_menu.add_command(label="Light Theme", command=lambda: apply_theme("Light"))
themes_menu.add_command(label="Dark Theme", command=lambda: apply_theme("Dark"))
menu_bar.add_cascade(label="Themes", menu=themes_menu)

# About Menu
def about_us_action():
    messagebox.showinfo("About Us", "Created by: Manav Patel")

about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About Us", command=about_us_action)
menu_bar.add_cascade(label="About Us", menu=about_menu)

# Attach the menu bar to the root window
root.config(menu=menu_bar)

# Notebook (Tabs)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Tab 1: Normal Arithmetic
tab_basic = ttk.Frame(notebook)
notebook.add(tab_basic, text="Normal Arithmetic")

# Normal Arithmetic UI
tk.Label(tab_basic, text="Enter First Hexadecimal Number (e.g., 0E):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
normal_hex1 = tk.StringVar()
tk.Entry(tab_basic, textvariable=normal_hex1, width=30).grid(row=0, column=1, padx=10, pady=5)

tk.Label(tab_basic, text="Enter Second Hexadecimal Number (e.g., 09):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
normal_hex2 = tk.StringVar()
tk.Entry(tab_basic, textvariable=normal_hex2, width=30).grid(row=1, column=1, padx=10, pady=5)

tk.Label(tab_basic, text="Answer:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
normal_result = tk.StringVar()
tk.Entry(tab_basic, textvariable=normal_result, state="readonly", width=30).grid(row=2, column=1, padx=10, pady=5)

# Buttons
tk.Button(tab_basic, text="Addition", command=handle_addition).grid(row=0, column=2, padx=10, pady=5)
tk.Button(tab_basic, text="Multiplication", command=handle_multiplication).grid(row=1, column=2, padx=10, pady=5)


# Tab 2: Hex Expression Evaluator
tab_evaluator = ttk.Frame(notebook)
notebook.add(tab_evaluator, text="Hex Expression Evaluator")

# Hex Expression Evaluator UI
evaluator_label = tk.Label(tab_evaluator, text="Hex Expression Evaluator", font=("Helvetica", 16))
evaluator_label.pack(pady=10)

# User Input for Expression
tk.Label(tab_evaluator, text="Enter Hex Expression:").pack()
evaluator_expression = tk.StringVar()
evaluator_expression_entry = tk.Entry(tab_evaluator, textvariable=evaluator_expression, width=50)
evaluator_expression_entry.pack(pady=5)

# Evaluate Button
def handle_evaluation():
    expression = evaluator_expression.get().strip()

    try:
        # Evaluate the expression
        result = evaluate_expression(expression)
        evaluator_result.set(result)
    except Exception as e:
        messagebox.showerror("Error", f"Evaluation failed: {e}")


evaluator_button = tk.Button(tab_evaluator, text="Evaluate", command=handle_evaluation)
evaluator_button.pack(pady=10)

# Evaluation Result
tk.Label(tab_evaluator, text="Result:").pack()
evaluator_result = tk.StringVar()
evaluator_result_label = tk.Entry(tab_evaluator, textvariable=evaluator_result, state="readonly", width=50)
evaluator_result_label.pack(pady=5)

# Tab 3: Encryption
tab_encryption = ttk.Frame(notebook)
notebook.add(tab_encryption, text="Encryption")

# Encryption UI
encryption_label = tk.Label(tab_encryption, text="Encryption Panel", font=("Helvetica", 16))
encryption_label.pack(pady=10)

# Plaintext Input
tk.Label(tab_encryption, text="Plain Text (ASCII):").pack()
encrypt_plaintext = tk.StringVar()
encrypt_plaintext_entry = tk.Entry(tab_encryption, textvariable=encrypt_plaintext, width=50)
encrypt_plaintext_entry.pack(pady=5)

# Round Key Input
tk.Label(tab_encryption, text="Round Key (Hex):").pack()
encrypt_round_key = tk.StringVar()
encrypt_round_key_entry = tk.Entry(tab_encryption, textvariable=encrypt_round_key, width=50)
encrypt_round_key_entry.pack(pady=5)

# Encrypt Button
def handle_encryption():
    plaintext = encrypt_plaintext.get().strip()
    round_key = encrypt_round_key.get().strip()

    # Validate inputs
    if not plaintext:
        messagebox.showerror("Error", "Plaintext cannot be empty!")
        return

    if len(round_key) != 32:
        messagebox.showerror("Error", "Round Key must be 32 hex characters!")
        return

    try:
        ciphertext = encrypt(plaintext, round_key)
        encryption_result.set(ciphertext)
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")


encrypt_button = tk.Button(tab_encryption, text="Encrypt", command=handle_encryption)
encrypt_button.pack(pady=10)

# Encryption Result
tk.Label(tab_encryption, text="Ciphertext (Hex):").pack()
encryption_result = tk.StringVar()
encryption_result_label = tk.Entry(tab_encryption, textvariable=encryption_result, state="readonly", width=50)
encryption_result_label.pack(pady=5)

# Tab 4: Decryption
tab_decryption = ttk.Frame(notebook)
notebook.add(tab_decryption, text="Decryption")

# Decryption UI
decrypt_label = tk.Label(tab_decryption, text="Decryption Panel", font=("Helvetica", 16))
decrypt_label.pack(pady=10)

# Ciphertext Input
tk.Label(tab_decryption, text="Cipher Text:").pack()
decrypt_ciphertext = tk.StringVar()
decrypt_ciphertext_entry = tk.Entry(tab_decryption, textvariable=decrypt_ciphertext, width=50)
decrypt_ciphertext_entry.pack(pady=5)

# Round Key Input
tk.Label(tab_decryption, text="Round Key:").pack()
decrypt_round_key = tk.StringVar()
decrypt_round_key_entry = tk.Entry(tab_decryption, textvariable=decrypt_round_key, width=50)
decrypt_round_key_entry.pack(pady=5)

# Decrypt Button
decrypt_button = tk.Button(tab_decryption, text="Decrypt", command=handle_decryption)
decrypt_button.pack(pady=10)

# Decryption Results
tk.Label(tab_decryption, text="Decrypted Hex:").pack()
decrypt_result_hex = tk.StringVar()
decrypt_result_hex_label = tk.Entry(tab_decryption, textvariable=decrypt_result_hex, state="readonly", width=50)
decrypt_result_hex_label.pack(pady=5)

tk.Label(tab_decryption, text="Decrypted ASCII:").pack()
decrypt_result_ascii = tk.StringVar()
decrypt_result_ascii_label = tk.Entry(tab_decryption, textvariable=decrypt_result_ascii, state="readonly", width=50)
decrypt_result_ascii_label.pack(pady=5)

# Run the Application
root.mainloop()
