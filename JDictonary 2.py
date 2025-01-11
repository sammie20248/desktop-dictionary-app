from tkinter import Tk, Entry, Button, Label, StringVar, Toplevel

def italian_dictionary_app():
    window = Tk()
    window.geometry("700x250")
    window.title("Italian Dictionary")


    entry_text = Entry(window, font=('Arial', 14))
    entry_text.pack(pady=10)
    result = StringVar()
    result_label = Label(window, textvariable=result, font=('Arial', 14), fg='blue')
    result_label.pack(pady=10)


    italian_dictionary = {
        'Car': 'Coche',
        'Sister': 'Hermana',
        'Father': 'Padre',
        'Map': 'Mapa',
        'Beer': 'Cerveza',
        'Family': 'Familia',
        'Hello': 'Hola',
        'Taxi': 'Taxi',
        'Goodbye': 'Adios',
        'Four': 'Cuatro',
        'Music': 'Musica',
        'Three': 'Tres',
        'Mother': 'Madre',
        'Thank You': 'Gracias',
        'Bus': 'Autobus',
        'Party': 'Fiesta',
        'One': 'Uno',
        'Food': 'Comida',
        'Brother': 'Hermano'
    }


    def search(word):
        word = word.capitalize()
        if word in italian_dictionary:
            result.set(f"The translation is: {italian_dictionary[word]}")
        else:
            result.set("Word not found in the dictionary.")


    search_btn = Button(window, text="Search", command=lambda: search(entry_text.get()), font=('Arial', 14), bg='lightblue')
    search_btn.pack(pady=10)


    window.mainloop()


italian_dictionary_app()
