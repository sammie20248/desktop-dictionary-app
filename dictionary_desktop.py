import tkinter as tk
from tkinter import ttk, messagebox

# Spanish dictionary
SPANISH_DICT = {
    "greetings": {
        "hello": "hola",
        "goodbye": "adiós",
        "please": "por favor",
        "thank_you": "gracias",
        "you're_welcome": "de nada"
    },
    "colors": {
        "red": "rojo",
        "blue": "azul",
        "green": "verde",
        "yellow": "amarillo",
        "black": "negro",
        "white": "blanco"
    },
    "numbers": {
        1: "uno",
        2: "dos",
        3: "tres",
        4: "cuatro",
5: "cinco"
    }
}

# Function to get translations
def get_spanish_translations():
    category = category_var.get()
    words = word_entry.get().split(",")  # Split words by commas
    words = [word.strip() for word in words]  # Remove extra spaces

    if category not in SPANISH_DICT:
        messagebox.showerror("Error", f"Category '{category}' not found.")
        return

    translations = {}
    for word in words:
        translation = SPANISH_DICT[category].get(word, f"'{word}' not found")
        translations[word] = translation

    # Display translations
    result_text.set("\n".join([f"{word}: {translation}" for word, translation in translations.items()]))

# Tkinter setup
root = tk.Tk()
root.title("English to Spanish Translator")

# Widgets
tk.Label(root, text="Select a category:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

category_var = tk.StringVar(value="greetings")
category_menu = ttk.Combobox(root, textvariable=category_var, state="readonly")
category_menu["values"] = list(SPANISH_DICT.keys())
category_menu.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter words (comma-separated):").grid(row=1, column=0, padx=10, pady=10, sticky="w")

word_entry = tk.Entry(root, width=40)
word_entry.grid(row=1, column=1, padx=10, pady=10)

translate_button = tk.Button(root, text="Translate", command=get_spanish_translations)
translate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", anchor="w")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# Run the application
root.mainloop()